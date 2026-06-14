from flask import Flask, render_template, Blueprint, request, redirect, url_for, flash

from services.login import (iniciar_sesion, registrar_usuario)

login_bp = Blueprint('login', __name__)
registro_bp = Blueprint('registro', __name__)

#LOGIN CLIENTES
@login_bp.route("/login", methods=["GET", "POST"])
def login_cliente():

    if request.method == "POST":
        email = request.form["email"]
        contrasena = request.form["contrasena"]
        usuario = iniciar_sesion(email, contrasena)
        
        if usuario:
            print(usuario)
            if usuario["rol"] == "admin":
                return redirect(url_for("login.login_exitoso"))
            return redirect(url_for("inicio.inicio"))
    return render_template("login_cliente.html")


# Login-admin
@login_bp.route("/login/admin", methods=["GET", "POST"])
def login_admin():

    if request.method == "POST":
        email = request.form["email"]
        contrasena = request.form["contrasena"]
        usuario = iniciar_sesion(email, contrasena)
        if usuario and usuario["rol"] == "admin":
            return redirect(url_for("login.login_exitoso"))
        flash("No tenés permisos de administrador")
    return render_template("login_administrador.html")


@login_bp.route("/login-exitoso")
def login_exitoso():
    return render_template("login_exitoso.html")

@registro_bp.route("/login/registrate", methods=["GET", "POST"])
def registro():
    
    if request.method == "POST":

        nombre = request.form["nombre"]
        email = request.form["email"]
        contrasena = request.form["contrasena"]
        confirmar_contrasena = request.form["confirmar"]

        if contrasena != confirmar_contrasena:
            flash("Las contraseñas no coinciden")
            return redirect(url_for("registro.registro"))

        usuario = registrar_usuario(
            nombre,
            email,
            contrasena
        )
        
        print(usuario)
        if "error" in usuario:
            flash(usuario["error"])
            return redirect(url_for("registro.registro"))
        return redirect(url_for("inicio.inicio"))

    return render_template("registrar_cuenta.html")