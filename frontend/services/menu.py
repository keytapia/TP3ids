import requests

API_BACKEND_URL = "http://127.0.0.1:5000"


# =========================
# ADMIN
# =========================

def obtener_menu_admin(categoria=None):
    try:
        url = f"{API_BACKEND_URL}/api/admin/menu"

        params = {}
        if categoria:
            params["categoria"] = categoria

        response = requests.get(url, params=params, timeout=10)

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

    except requests.exceptions.RequestException as e:
        return {
            "ok": False,
            "data": [],
            "error": str(e)
        }


# =========================
# PUBLICO
# =========================

def obtener_menu_publico(categoria=None):
    try:
        url = f"{API_BACKEND_URL}/api/menu"

        params = {}
        if categoria:
            params["categoria"] = categoria

        response = requests.get(url, params=params, timeout=10)

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

    except requests.exceptions.RequestException as e:
        return {
            "ok": False,
            "data": [],
            "error": str(e)
        }


def obtener_plato(id):

    try:

        response = requests.get(
            f"{API_BACKEND_URL}/api/admin/menu/{id}",
            timeout=10
        )

        if response.status_code == 200:
            return {
                "ok": True,
                "data": response.json()
            }

        return {
            "ok": False,
            "data": None,
            "error": response.text
        }

    except requests.exceptions.ConnectionError:
        return {
            "ok": False,
            "data": None,
            "error": "No se pudo conectar con el backend."
        }


def crear_plato(data):

    try:

        response = requests.post(
            f"{API_BACKEND_URL}/api/admin/menu",
            json=data,
            timeout=10
        )

        if response.status_code == 201:
            return {
                "ok": True,
                "data": response.json()
            }

        return {
            "ok": False,
            "data": None,
            "error": response.text
        }

    except requests.exceptions.ConnectionError:
        return {
            "ok": False,
            "data": None,
            "error": "No se pudo conectar con el backend."
        }


def editar_plato(id, data):

    try:

        response = requests.put(
            f"{API_BACKEND_URL}/api/admin/menu/{id}",
            json=data,
            timeout=10
        )

        if response.status_code == 200:
            return {
                "ok": True,
                "data": response.json()
            }

        return {
            "ok": False,
            "data": None,
            "error": response.text
        }

    except requests.exceptions.ConnectionError:
        return {
            "ok": False,
            "data": None,
            "error": "No se pudo conectar con el backend."
        }


def eliminar_plato(id):

    try:

        response = requests.delete(
            f"{API_BACKEND_URL}/api/admin/menu/{id}",
            timeout=10
        )

        if response.status_code == 200:
            return {
                "ok": True
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


def obtener_categorias():

    try:

        response = requests.get(
            f"{API_BACKEND_URL}/api/categorias",
            timeout=10
        )

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