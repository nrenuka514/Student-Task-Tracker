from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)
FILE = "data.json"

# Load data from file
def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

# Save data to file
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

# Calculate progress stats
def get_progress_stats():
    data = load_data()
    if len(data) == 0:
        return {"total": 0, "completed": 0, "pending": 0, "percentage": 0}
    
    completed = sum(1 for record in data if record.get("status") == "Completed")
    total = len(data)
    pending = total - completed
    percentage = int((completed / total) * 100) if total > 0 else 0
    
    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "percentage": percentage
    }

# Home page
@app.route("/")
def home():
    progress = get_progress_stats()
    return render_template("index.html", progress=progress)

# Add data
@app.route("/add", methods=["POST"])
def add():
    data = load_data()

    name = request.form.get("name", "").strip()
    task = request.form.get("task", "").strip()
    status = request.form.get("status", "Pending")
    marks = request.form.get("marks", "").strip()

    if not name or not task:
        return "Error: Name and task are required!", 400

    if status == "Completed" and marks == "":
        return "Error: Marks are required for completed tasks.", 400

    record = {"name": name, "task": task, "status": status, "marks": marks}
    data.append(record)

    save_data(data)
    return redirect(url_for("view"))

# View data
@app.route("/view")
def view():
    data = load_data()
    progress = get_progress_stats()
    return render_template("view.html", records=data, progress=progress)

# Delete data
@app.route("/delete/<int:index>")
def delete(index):
    data = load_data()
    if 0 <= index < len(data):
        data.pop(index)
        save_data(data)
    return redirect(url_for("view"))

# Edit data
@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    data = load_data()
    
    # Bounds checking
    if not (0 <= index < len(data)):
        return redirect(url_for("view"))
    
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        task = request.form.get("task", "").strip()
        status = request.form.get("status", "Pending")
        marks = request.form.get("marks", "").strip()

        if not name or not task:
            return "Error: Name and task are required!", 400

        if status == "Completed" and marks == "":
            return "Error: Marks are required for completed tasks.", 400

        data[index]["name"] = name
        data[index]["task"] = task
        data[index]["status"] = status
        data[index]["marks"] = marks

        save_data(data)
        return redirect(url_for("view"))

    return render_template("edit.html", record=data[index], index=index)

if __name__ == "__main__":
    app.run(debug=True)