import requests

API_BACKEND_URL = "http://127.0.0.1:5000"


def obtener_resenas():

    try:

        response = requests.get(f"{API_BACKEND_URL}/api/admin/resenas", timeout=10)

        if response.status_code == 200:
            return {
                "ok": True,
                "data": response.json()
            }

        return {
            "ok": False,
            "data": [],
            "error": response.text
        }

    except requests.exceptions.ConnectionError:
        return {
            "ok": False,
            "data": [],
            "error": "No se pudo conectar con el backend."
        }


def ocultar_mostrar_resena(id):

    try:

        response = requests.patch(f"{API_BACKEND_URL}/api/admin/resenas/{id}", timeout=10)

        return response.status_code == 200

    except requests.exceptions.ConnectionError:
        return False


def eliminar_resena(id):

    try:

        response = requests.delete(f"{API_BACKEND_URL}/api/admin/resenas/{id}", timeout=10)

        return response.status_code == 200

    except requests.exceptions.ConnectionError:
        return False