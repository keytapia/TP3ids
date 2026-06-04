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

        try:
            respuesta_json = response.json()
        except ValueError:
            respuesta_json = {"ok": False, "error": "Respuesta del backend no es JSON"}

        if response.status_code == 201:
            return {"ok": True, "data": respuesta_json}
        
        print(f"Error al crear reserva: {response.status_code} - {response.text}")

        return {"ok": False, "error": respuesta_json}

    except requests.exceptions.ConnectionError:
        return {"ok": False, "error": "No se pudo conectar con el backend."}

    except requests.exceptions.Timeout:
        return {"ok": False, "error": "El backend tardó demasiado en responder."}
    

def obtener_mesas_por_estado(fecha, horario, cantidad_personas):
    try:
        params = {
            "fecha": fecha,
            "horario": horario,
            "cantidad_personas": cantidad_personas
        }
        response = requests.get(
            f"{API_BACKEND_URL}/api/mesas-disponibles",
            params=params,
            timeout=10
        )

        if response.status_code == 200:
            return {"ok": True, "data": response.json()}
        
        print(f"Error al obtener mesas por estado: {response.status_code} - {response.text}")
        return {"ok": False, "error": response.json()}

    except requests.exceptions.ConnectionError:
        return {"ok": False, "error": "No se pudo conectar con el backend."}

    except requests.exceptions.Timeout:
        return {"ok": False, "error": "El backend tardó demasiado en responder."}