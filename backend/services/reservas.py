from datetime import date, timedelta

from utils.constants import (
    DIAS_DISPONIBILIDAD,
    HORARIOS_POSIBLES,
)

from services.usuarios import (
    buscar_usuario_por_email,
    crear_usuario_cliente
)

from services.qr import (
    crear_qr_reserva
)

from services.email import (
    enviar_email_confirmacion
)

from repositories.reservas import (
    obtener_todas_las_reservas_db,
    obtener_reservas_por_estado_db,
    obtener_reserva_por_id_db,
    buscar_mesa_disponible_db,
    buscar_mesa_disponible_para_horario_db,
    obtener_mesas_por_estado_db,
    cancelar_reserva_db,
    crear_reserva_db
)


# Mostrar todas las reservas
def listar_reservas():

    reservas = obtener_todas_las_reservas_db()

    for reserva in reservas:
        if reserva.get("fecha"):
            reserva["fecha"] = str(reserva["fecha"])

        if reserva.get("horario"):
            reserva["horario"] = str(reserva["horario"])

    return reservas


# Mostrar reservas por estado
def listar_reservas_por_estado(estado):

    reservas = obtener_reservas_por_estado_db(estado)

    for reserva in reservas:
        if reserva.get("fecha"):
            reserva["fecha"] = str(reserva["fecha"])

        if reserva.get("horario"):
            reserva["horario"] = str(reserva["horario"])

    return reservas


# Mostrar reserva por ID
def buscar_reserva_por_id(reserva_id):

    return obtener_reserva_por_id_db(reserva_id)


# Disponibilidad de reservas
def obtener_disponibilidad():

    disponibilidad = []

    for i in range(DIAS_DISPONIBILIDAD):

        fecha_actual = date.today() + timedelta(days=i)

        horarios_disponibles = []

        for horario in HORARIOS_POSIBLES:

            mesa_disponible = buscar_mesa_disponible_para_horario_db(
                fecha_actual,
                horario
            )

            if (
                mesa_disponible and
                mesa_disponible["capacidad_maxima"] is not None
            ):
                capacidad_maxima = mesa_disponible["capacidad_maxima"]

                horarios_disponibles.append({
                    "horario": horario,
                    "capacidad_maxima_personas_por_mesa_disponibles":
                        list(range(1, capacidad_maxima + 1))
                })

        if horarios_disponibles:
            disponibilidad.append({
                "fecha": fecha_actual.strftime("%Y-%m-%d"),
                "horarios": horarios_disponibles
            })

    return disponibilidad


# Buscar mesa disponible
def buscar_mesa_disponible(fecha, horario, cantidad_personas):

    return buscar_mesa_disponible_db(
        fecha,
        horario,
        cantidad_personas
    )


# Obtener mesas por estado
def obtener_mesas_por_estado(fecha, horario, cantidad_personas):

    mesas = obtener_mesas_por_estado_db(
        fecha,
        horario,
        cantidad_personas
    )

    for mesa in mesas:

        mesa["reservada"] = bool(mesa["reservada"])
        mesa["capacidad_suficiente"] = bool(
            mesa["capacidad_suficiente"]
        )

        mesa["seleccionable"] = (
            mesa["estado"] == "disponible"
            and not mesa["reservada"]
            and mesa["capacidad_suficiente"]
        )

    return mesas


# Cancelar reserva
def cancelar_reserva(reserva_id):

    return cancelar_reserva_db(reserva_id)


# Crear reserva
def crear_reserva(
    nombre,
    apellido,
    email,
    telefono,
    mesa_id,
    fecha,
    horario,
    cantidad_personas,
    notas_adicionales=""
):

    usuario = buscar_usuario_por_email(email)

    if not usuario:
        usuario = crear_usuario_cliente(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono
        )

    if not usuario:
        return None

    usuario_id = usuario["id"]

    nueva_reserva = crear_reserva_db(
        usuario_id=usuario_id,
        mesa_id=mesa_id,
        fecha=fecha,
        horario=horario,
        cantidad_personas=cantidad_personas,
        notas_adicionales=notas_adicionales
    )

    if not nueva_reserva:
        return None

    reserva = {
        "id": nueva_reserva["id"],
        "usuario_id": usuario_id,
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "telefono": telefono,
        "mesa_id": mesa_id,
        "fecha": fecha,
        "horario": horario,
        "cantidad_personas": cantidad_personas,
        "notas_adicionales": notas_adicionales,
        "estado": "confirmada"
    }

    qr_buffer = crear_qr_reserva(reserva)

    email_enviado = enviar_email_confirmacion(
        reserva,
        qr_buffer
    )

    reserva["email_enviado"] = email_enviado

    return reserva