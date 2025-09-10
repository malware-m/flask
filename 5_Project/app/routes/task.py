from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from app import db
from app.models import Task

# Create the blueprint object for task routes
task_bp = Blueprint('task', __name__)

# 📝 View all tasks (home page)
@task_bp.route('/')
def view_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))  # 🔐 Redirect to login if user not logged in

    tasks = Task.query.all()  # 📥 Fetch all tasks from DB
    return render_template('task.html', tasks=tasks)  # 📤 Send tasks to template

# 📝 Create task object, add it to database, and redirect to task list
@task_bp.route('/add', methods=['POST'])
def add_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))  # 🔐 Must be logged in to add task

    title = request.form.get('title')  # 🧾 Get task title from form
    if title:
        new_task = Task(title=title, status='Pending')  # 🆕 Create task with default status
        db.session.add(new_task)        # 🧠 Add to session
        db.session.commit()             # 💾 Commit to DB
        flash('Task added successfully', 'success')  # ✅ Flash success message

    return redirect(url_for('task.view_task'))  # 🔄 Redirect to task list view

# 🔄 Toggle task status from Pending ➝ Working ➝ Done ➝ Pending
@task_bp.route('/toggle/<int:task_id>', methods=['POST'])  # 🧠 Handle toggle logic for status
def toggle_status(task_id):
    task = Task.query.get(task_id)  # 🔍 Find task by ID
    if task:
        if task.status == 'Pending':
            task.status = 'Working'  # ✅ Update status
        elif task.status == 'Working':
            task.status = 'Done'
        else:
            task.status = 'Pending'
        
        db.session.commit()  # 💾 Save changes to DB

    return redirect(url_for('task.view_task'))  # 🔄 Redirect to task list

# 🗑️ Delete all tasks from database
@task_bp.route('/delete', methods=['POST'])
def delete_task():
    Task.query.delete()            # 🧹 Delete all tasks
    db.session.commit()            # 💾 Commit changes
    flash('All tasks cleared', 'info')  # 📝 Show info message
    return redirect(url_for('task.view_task'))  # 🔄 Go back to task list
