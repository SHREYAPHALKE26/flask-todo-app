from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Define the User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.DateTime, nullable=True)  # New field for due dates
    priority = db.Column(db.String(20), default="Medium")  # New field for priority
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
@login_required
def index():
    tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.due_date.asc()).all()  # Sort by due date
    today = datetime.today().strftime('%Y-%m-%d')  # Get today's date in YYYY-MM-DD format
    return render_template("index.html", tasks=tasks, today=today)

@app.route("/add", methods=["POST"])
@login_required
def add_task():
    task_name = request.form.get("task_name")
    due_date_str = request.form.get("due_date")
    priority = request.form.get("priority")

    # Convert due_date string to a datetime object
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None

    if task_name:
        new_task = Task(
            name=task_name,
            due_date=due_date,
            priority=priority,
            user_id=current_user.id
        )
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>")
@login_required
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task and task.user_id == current_user.id:
        task.completed = True
        db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
@login_required
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task and task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for("index"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("index"))
        else:
            flash('Login failed. Please check your username and password.', 'danger')
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)