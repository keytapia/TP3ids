import requests

API_BACKEND_URL = "http://localhost:5000"


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
            return response.json()

        print("Error backend:", response.status_code, response.text)
        return {}

    except requests.exceptions.ConnectionError:
        print("No se pudo conectar con el backend.")
        return {}

    except requests.exceptions.Timeout:
        print("El backend tardó demasiado en responder.")
        return {}