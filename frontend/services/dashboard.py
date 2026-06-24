import os
import requests

API_BACKEND_URL = os.getenv("API_BACKEND_URL")


def obtener_dashboard():

    try:
        response = requests.get(
            f"{API_BACKEND_URL}/api/admin/dashboard",
            timeout=10
        )

        if response.status_code == 200:
            return {
                "ok": True,
                "data": response.json()
            }

        return {
            "ok": False,
            "error": response.text
        }

    except requests.exceptions.ConnectionError:
        return {
            "ok": False,
            "error": "No se pudo conectar con el backend."
        }

    except requests.exceptions.Timeout:
        return {
            "ok": False,
            "error": "El backend tardó demasiado en responder."
        }