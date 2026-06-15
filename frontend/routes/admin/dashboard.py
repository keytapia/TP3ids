from flask import Flask, render_template, Blueprint, redirect
from utils.auth import requiere_admin
dashboard_bp = Blueprint('dashboard', __name__)

# Dashboard
@dashboard_bp.route("/admin/dashboard")
@requiere_admin
def dashboard():

    return render_template("admin/dashboard.html")