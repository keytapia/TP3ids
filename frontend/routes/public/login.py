from flask import Flask, render_template, Blueprint, request, redirect, url_for

from services.login import iniciar_sesion

login_bp = Blueprint('login', __name__)

# Login
@login_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form["email"]
        contrasena = request.form["contrasena"]
        usuario = iniciar_sesion(email, contrasena)
        if usuario:
            return redirect(url_for("login.login_exitoso"))

    return render_template("public/login.html")

# Login exitoso
@login_bp.route("/login-exitoso")
def login_exitoso():
    return render_template("public/login_exitoso.html")