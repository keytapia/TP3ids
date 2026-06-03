from datetime import datetime
import re

ERROR_CODE_DATOS_INVALIDOS = "DATOS_INVALIDOS"
ERROR_CODE_RESERVA_NO_CREADA = "RESERVA_NO_CREADA"

#validadores utiles para las rutas de reservas

def errores_api(code, message, description):
    return {
        "success": False,
        "error": {
            "code": message,
            "description": description
        }
    }, code

def validar_reserva(datos):
    #validamos el diccionario de datos, si hay un error retorna un error, si no retorna None
    if not datos.get("nombre"):
        return errores_api(
            code=400,
            message=ERROR_CODE_DATOS_INVALIDOS,
            description="Nombre inválido")

    if not datos.get("apellido"):
        return errores_api(
            code=400,
            message=ERROR_CODE_DATOS_INVALIDOS,
            description="Apellido inválido")

    if not validar_email(datos.get("email")):
        return errores_api(
            code=400,
            message=ERROR_CODE_DATOS_INVALIDOS,
            description="Email inválido")

    if not datos.get("telefono"):
        return errores_api(
            code=400,
            message=ERROR_CODE_DATOS_INVALIDOS,
            description="Teléfono inválido")

    if not validar_fecha(datos.get("fecha")):
        return errores_api(
            code=400,
            message=ERROR_CODE_DATOS_INVALIDOS,
            description="Fecha inválida")

    if not validar_horario(datos.get("horario")):
        return errores_api(
            code=400,
            message=ERROR_CODE_DATOS_INVALIDOS,
            description="Horario inválido")

    if not isinstance(datos.get("cantidad_personas"), int) or datos.get("cantidad_personas") <= 0:
        return errores_api(
            code=400,
            message=ERROR_CODE_DATOS_INVALIDOS,
            description="Cantidad de personas inválida")

    return None

def validar_email(email):
    # Expresión regular para validar el formato del email
    patron = r"^[^@]+@[^@]+\.[^@]+$"
    return bool(re.match(patron, email)) # con re.match buscamos coincidencias y con bool convertimos el resultado a True o False

def validar_fecha(fecha):
    try:
        # ACEPTAMOS FECHAS DE TIPO "yyyy-mm-dd"
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        # Si ocurre un error de conversión, la fecha no es válida
        return False
    
def validar_horario(horario):
    try:
        # ACEPTAMOS HORARIOS DE TIPO "HH:MM"
        datetime.strptime(horario, "%H:%M")
        return True
    except ValueError:
        # Si ocurre un error de conversión, el horario no es válido
        return False
    
def validar_telefono(telefono):
    # Expresión regular para validar el formato del teléfono (solo dígitos, con o sin espacios o guiones)
    try:
        patron = r"^\d{8,11}$"
        if re.match(patron, telefono):
            return True
        else:
            return False
    except ValueError:
        return False