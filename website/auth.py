from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    flash('hewwo', category='success')
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"
