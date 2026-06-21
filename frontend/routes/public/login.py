from flask import Blueprint, render_template, request, redirect, url_for, flash, session

from services.login import (
    iniciar_sesion,
    registrar_usuario
)

login_bp = Blueprint("login", __name__)
registro_bp = Blueprint("registro", __name__)


# LOGIN CLIENTES
@login_bp.route("/login", methods=["GET", "POST"])
def login_cliente():

    if request.method == "POST":

        email = request.form["email"]
        contrasena = request.form["contrasena"]

        usuario = iniciar_sesion(email, contrasena)

        if usuario:

            if usuario["rol"] != "cliente":
                flash("Este acceso es sólo para clientes.", "error")
                return redirect(url_for("login.login_cliente"))

            session["usuario"] = usuario

            return redirect(url_for("inicio.inicio"))

        flash("Email o contraseña incorrectos.", "error")

    return render_template("public/login_cliente.html")


# LOGIN ADMIN
@login_bp.route("/login/admin", methods=["GET", "POST"])
def login_admin():

    usuario = session.get("usuario")

    if usuario:

        if usuario["rol"] == "admin":
            return redirect("/admin/dashboard")

        return redirect(url_for("inicio.inicio"))

    if request.method == "POST":

        email = request.form["email"]
        contrasena = request.form["contrasena"]

        usuario = iniciar_sesion(email, contrasena)

        if usuario:

            if usuario["rol"] != "admin":
                flash("No tenés permisos de administrador.", "error")
                return redirect(url_for("login.login_admin"))

            session["usuario"] = usuario

            return redirect(url_for("login.login_exitoso"))

        flash("Email o contraseña incorrectos.", "error")

    return render_template("public/login_administrador.html")


@login_bp.route("/login-exitoso")
def login_exitoso():

    return render_template("public/login_exitoso.html")


@registro_bp.route("/login/registrate", methods=["GET", "POST"])
def registro():

    if request.method == "POST":

        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        email = request.form["email"]
        telefono = request.form["telefono"]
        contrasena = request.form["contrasena"]
        confirmar_contrasena = request.form["confirmar"]

        if contrasena != confirmar_contrasena:

            flash("Las contraseñas no coinciden", "error")

            return redirect(url_for("registro.registro"))

        usuario = registrar_usuario(
            nombre,
            apellido,
            email,
            telefono,
            contrasena
        )

        if "error" in usuario:

            flash(usuario["error"], "error")

            return redirect(url_for("registro.registro"))

        flash("Cuenta creada con éxito. Ya podés iniciar sesión.", "exito")
        return redirect(url_for("login.login_cliente"))
    
    return render_template("public/registrar_cuenta.html")


@login_bp.route("/logout")
def logout():

    session.clear()

    return redirect("/")