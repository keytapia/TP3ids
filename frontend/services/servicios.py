import os
import requests

API_BACKEND_URL = os.getenv("API_BACKEND_URL")


def obtener_servicios():

    try:
        response = requests.get(f"{API_BACKEND_URL}/api/admin/servicios", timeout=10)

        if response.status_code == 200:
            return {"ok": True, "data": response.json()}
        
        return {"ok": False, "error": response.text}
    
    except requests.exceptions.ConnectionError:
        return {"ok": False, "error": "No se pudo conectar con el backend."}

    except requests.exceptions.Timeout:
        return {"ok": False, "error": "El backend tardo demasiado en responder."}
    

def obtener_servicio_por_id(id):

    try:

        response = requests.get(f"{API_BACKEND_URL}/api/admin/servicios/{id}", timeout=10)

        if response.status_code == 200:
            return {"ok": True,"data": response.json()}

        return {"ok": False, "data": None, "error": response.text}

    except requests.exceptions.ConnectionError:
        return {"ok": False, "data": None, "error": "No se pudo conectar con el backend."}

    except requests.exceptions.Timeout:
        return {"ok": False, "data": None, "error": "El backend tardó demasiado en responder."}


def crear_servicio(
        nombre,
        disponible
):
    datos_del_servicio = {
        "nombre": nombre,
        "disponible": disponible
    }

    try:
        response = requests.post(f"{API_BACKEND_URL}/api/admin/servicios", json=datos_del_servicio, timeout=10)

        if response.status_code == 201:
            return {"ok": True, "data": response.json()}

        return {"ok": False, "error": response.text}

    except requests.exceptions.ConnectionError:
        return {"ok": False, "error": "No se pudo conectar con el backend."}

    except requests.exceptions.Timeout:
        return {"ok": False, "error": "El backend tardo demasiado en responder."}


def editar_servicio(id, nombre, disponible):

    datos_del_servicio = {
        "nombre": nombre,
        "disponible": disponible
    }

    try:
        response = requests.put(f"{API_BACKEND_URL}/api/admin/servicios/{id}", json=datos_del_servicio, timeout=10)

        if response.status_code == 200:
            return {"ok": True, "data": response.json()}

        return {"ok": False, "error": response.text, "data": None}


    except requests.exceptions.ConnectionError:
        return {"ok": False, "error": "No se pudo conectar con el backend.", "data": None}

    except requests.exceptions.Timeout:
        return {"ok": False, "error": "El backend tardo demasiado en responder.", "data": None}
    

def eliminar_servicio(id):

    try:

        response = requests.delete(f"{API_BACKEND_URL}/api/admin/servicios/{id}", timeout=10)

        if response.status_code == 200:
            return {"ok": True}

        return {"ok": False, "error": response.text}

    except requests.exceptions.ConnectionError:
        return {"ok": False, "error": "No se pudo conectar con el backend."}

    except requests.exceptions.Timeout:
        return {"ok": False, "error": "El backend tardó demasiado en responder."}