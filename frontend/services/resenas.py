import requests

API_BACKEND_URL = "http://127.0.0.1:5000"

def obtener_resenas():

    try:

        response = requests.get(
            f"{API_BACKEND_URL}/api/resenas",
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
            "error": "No se pudo conectar al backend"
        }
    
def obtener_resena_por_id(id_resena):

    try:

        response = requests.get(
            f"{API_BACKEND_URL}/api/resenas/{id_resena}",
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
            "error": "No se pudo conectar al backend"
        }


def crear_resena(
    nombre_usuario,
    reserva_id,
    comentario,
    puntuacion
):

    datos = {
        "nombre_usuario": nombre_usuario,
        "reserva_id": reserva_id,
        "comentario": comentario,
        "puntuacion": puntuacion
    }

    try:

        response = requests.post(
            f"{API_BACKEND_URL}/api/resenas",
            json=datos,
            timeout=10
        )

        if response.status_code == 201:

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
            "error": "No se pudo conectar al backend"
        }
    

