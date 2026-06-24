import os
import requests

API_BACKEND_URL = os.getenv("API_BACKEND_URL")


def obtener_configuracion():

    response = requests.get(
        f"{API_BACKEND_URL}/api/admin/configuracion"
    )

    return response.json()


def actualizar_configuracion(data):

    response = requests.put(
        f"{API_BACKEND_URL}/api/admin/configuracion",
        json=data
    )

    return response.json()