# Flask To-Do List Application

A simple and elegant To-Do List application built with **Flask**, **SQLAlchemy**, and **Bootstrap**. This application allows users to create, update, and manage their tasks with due dates and priorities.

![App Screenshot](https://via.placeholder.com/800x600?text=To-Do+List+App+Screenshot)

---

## Features

- **User Authentication**: Register, log in, and log out.
- **Task Management**:
  - Add tasks with a name, due date, and priority.
  - Mark tasks as completed.
  - Delete tasks.
- **Task Sorting**: Tasks are displayed in ascending order of their due dates.
- **Responsive Design**: Built with Bootstrap for a clean and modern UI.

---

## Technologies Used

- **Python**: Backend logic.
- **Flask**: Web framework.
- **SQLAlchemy**: Database management.
- **Bootstrap**: Frontend styling.
- **SQLite/PostgreSQL**: Database for storing tasks and user data.

---

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/flask-todo-app.git
   cd flask-todo-app

2. **Create a virtual environment (optional but recommended)**:

  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
 ```
3. **Install dependencies**:
  ```bash
  pip install -r requirements.txt
```
4. **Set up the database**:
- The app uses SQLite by default. To switch to PostgreSQL, update the SQLALCHEMY_DATABASE_URI in app.py.

5. **Run the application**:
  ```bash
  python app.py
```
6. **Access the app**:
- Open your browser and go to http://127.0.0.1:5000/.

---

**Project Structure**
```bash
flask-todo-app/
│
├── app.py                # Main application file
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Main page
│   ├── login.html        # Login page
│   └── register.html     # Registration page
└── static/               # Static files (CSS, JS, etc.)
    └── styles.css        # Custom CSS for styling
```

---

**Environment Variables**
- To run this project, you need to set the following environment variables:
**SECRET_KEY**: A secret key for Flask session management.
**SQLALCHEMY_DATABASE_URI**: The database connection string (e.g., sqlite:///todo.db or postgresql://username:password@hostname/database).

---

**Contributing**
- Contributions are welcome! Follow these steps:
Fork the repository.
- Create a new branch (git checkout -b feature/YourFeatureName).
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature/YourFeatureName).
- Open a pull request.

--- 

**License**
This project is licensed under the MIT License. See the LICENSE file for details.

---

**Acknowledgments**
- Flask: For the web framework.
- Bootstrap: For the responsive design.
- Render: For deployment guidance.
