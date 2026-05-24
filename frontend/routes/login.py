from flask import Flask, render_template, Blueprint

login_bp = Blueprint('login', __name__)

# Login
@login_bp.route("/login")
def index():
    return render_template("login.html")