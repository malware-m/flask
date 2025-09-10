from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__)  # create the blueprint object

# Dummy user for testing
User_credentials = {
    'username': 'admin',
    'password': 'admin'
}

@auth_bp.route('/login', methods=['GET', 'POST'])  # ✅ fixed typo
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == User_credentials['username'] and password == User_credentials['password']:
            session['user'] = username
            flash('Login successful', 'success')
            return redirect(url_for('auth.login'))  # optional redirect
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')  # ✅ handles GET and failed POST

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)  # remove session
    flash('Logged out', 'info')  # ✅ fixed category string
    return redirect(url_for('auth.login'))
