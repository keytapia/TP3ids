import requests

API_BACKEND_URL = "http://127.0.0.1:5000"


def crear_reserva(
    nombre,
    apellido,
    email,
    telefono,
    cantidad_personas,
    fecha,
    horario,
    notas_adicionales,
    mesa_id
):

    datos_de_la_reserva = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "telefono": telefono,
        "fecha": fecha,
        "horario": horario,
        "cantidad_personas": cantidad_personas,
        "notas_adicionales": notas_adicionales,
        "mesa_id": mesa_id
    }

    try:
        response = requests.post(
            f"{API_BACKEND_URL}/api/reservas",
            json=datos_de_la_reserva,
            timeout=10
        )

        if response.status_code == 201:
            return {"ok": True, "data": response.json()}

        return {"ok": False, "error": response.text}

    except requests.exceptions.ConnectionError:
        return {"ok": False, "error": "No se pudo conectar con el backend."}

    except requests.exceptions.Timeout:
        return {"ok": False, "error": "El backend tardó demasiado en responder."}
    

def obtener_mesas_por_estado(fecha, horario, cantidad_personas):
    try:
        response = requests.get(
            f"{API_BACKEND_URL}/api/mesas-disponibles",
            params = {
                "fecha": fecha,
                "horario": horario,
                "cantidad_personas": cantidad_personas
            },
            timeout=10
        )

        if response.status_code == 200:
            return {"ok": True, "data": response.json()}

        return {"ok": False, "error": response.text}

    except requests.exceptions.ConnectionError:
        return {"ok": False, "error": "No se pudo conectar con el backend."}

    except requests.exceptions.Timeout:
        return {"ok": False, "error": "El backend tardó demasiado en responder."}