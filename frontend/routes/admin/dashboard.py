from flask import Flask, render_template, Blueprint

dashboard_bp = Blueprint('dashboard', __name__)

# Dashboard
@dashboard_bp.route("/dashboard")
def dashboard():
    return render_template("admin/dashboard.html")