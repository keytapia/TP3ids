# Acá va la lógica para comunicar con el backend

import requests

API_BACKEND_URL = "http://localhost:5000"

def iniciar_sesion(email, contrasena):

    credenciales = {"email": email, "contrasena": contrasena}

    try:

        response = requests.post(f"{API_BACKEND_URL}/api/auth/login", json=credenciales, timeout=10)
        if response.status_code == 200:
            return response.json()
        return {}
    except requests.exceptions.ConnectionError:
        return {}

def registrar_usuario(nombre, email, contrasena):

    credenciales = {
        "nombre": nombre,
        "email": email,
        "contrasena": contrasena
    }

    try:
        response = requests.post(f"{API_BACKEND_URL}/api/usuarios/registro", json=credenciales, timeout=10)
        if response.status_code == 201:
            return response.json()
        if response.status_code == 400:
            return {"error": "Ya existe una cuenta con ese email"}
        return{}
    except requests.exceptions.ConnectionError:
        return()