from flask import session, redirect
from functools import wraps


def requiere_admin(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        usuario = session.get("usuario")

        if not usuario:
            return redirect("/login/admin")

        if usuario["rol"] != "admin":
            return redirect("/")

        return func(*args, **kwargs)

    return wrapper