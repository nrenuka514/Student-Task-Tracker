📌 Overview

The Smart Data Manager Web App is a full-stack web application developed using Python Flask, HTML, CSS, and JavaScript. It is designed to help users manage tasks efficiently by performing operations like adding, viewing, updating, and deleting tasks.
This project demonstrates how frontend and backend work together to build a complete web application.

🎯 Objective

The main objective of this project is to:
Understand full-stack development
Implement CRUD operations
Learn frontend-backend integration using Flask
Handle data using Python and JSON

⚙️ Technologies Used

Frontend: HTML, CSS, JavaScript
Backend: Python (Flask Framework)
Data Storage: JSON file
Templating Engine: Jinja (Flask)
🔄 Workflow
User enters data (Name, Task, Status) in the HTML form
Form sends data to Flask backend using POST request
Flask processes the data using Python
Data is stored in a JSON file (data.json)
Backend sends data to frontend using render_template()
Data is displayed dynamically using a loop

🧩 Features

➕ Add new tasks
📋 View all tasks
✏️ Edit existing tasks
❌ Delete tasks
✔️ Form validation using JavaScript
💾 Persistent storage using JSON file

🧠 Concepts Implemented

Flask Routing (/, /add, /view, /edit, /delete)
CRUD Operations
Functions (load_data(), save_data())
Loop (for loop in Jinja template)
File Handling using JSON
Exception Handling
Frontend-Backend Integration
