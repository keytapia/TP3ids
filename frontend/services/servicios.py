import requests

API_BACKEND_URL = "http://127.0.0.1:5000"

def obtener_servicios():

    try:
        response = requests.get(f"{API_BACKEND_URL}/api/servicios", timeout=10)
        if response.status_code == 200:
            return {"ok": True, "data": response.json()}
        return {"ok": False, "error": response.text}



def crear_servicio(
        nombre,
        descripcion
):
    datos_del_servicio = {
        "nombre": nombre,
        "descripcion": descripcion
    }

    try:
        response = requests.post(f"{API_BACKEND_URL}/api/servicios", json=datos_del_servicio), timeout=10)

        if response.status_code == 201:
            return {"ok": True, "data": response.json()}

        return {"ok": False, "error": response.text}

    except requests.exceptions.ConnectionError:
        return {"ok": False, "error": "No se pudo conectar con el backend."}

    except requests.exceptions.Timeout:
        return {"ok": False, "error": "El backend tardo demasiado en responder."}

def eliminar_servicio(id):

    try:
        response = requests.delete(f"{API_BACKEND_URL}/api/servicios/{id}", timeout=10)

    if response.status_code == 200:
        return {"ok": True}

    return  {"ok": False, "error": response.text}

    except requests.exceptions.ConnectionError:
        return {"ok": False, "error": "No se pudo conectar con el backend."}

    except requests.exceptions.Timeout:
        return {"ok": False, "error": "El backend tardo demasiado en responder."}


def editar_servicio(id, data):

    try:
        response = requests.put(f"{API_BACKEND_URL}/api/servicios/{id}", json=data), timeout=10)

        if response.status_code == 200:
            return {"ok": True, "data": response.json()}

        return {"ok": False, "error": response.text, "data": None}


    except requests.exceptions.ConnectionError:
        return {"ok": False, "error": "No se pudo conectar con el backend.", "data": None}

    except requests.exceptions.Timeout:
        return {"ok": False, "error": "El backend tardo demasiado en responder.", "data": None}