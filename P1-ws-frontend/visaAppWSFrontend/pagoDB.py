# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# author: rmarabini
import os
import requests

RESTAPIBASEURL = os.environ.get("RESTAPIBASEURL")


def verificar_tarjeta(tarjeta_data):
    """ Check if the tarjeta is registered 
    :param tarjeta_dict: dictionary with the tarjeta data
                       (as provided by TarjetaForm)
    :return True or False if tarjeta_data is not valid
    """
    if not tarjeta_data:
        return False
    url = f"{RESTAPIBASEURL}tarjeta/"
    try:
        response = requests.post(url, json=tarjeta_data)
        return response.status_code == 200
    except Exception as e:
        print("Error verificando tarjeta:", e)
        return False


def registrar_pago(pago_dict):
    """Register a payment using the backend REST API."""
    url = f"{RESTAPIBASEURL}pago/"
    try:
        response = requests.post(url, json=pago_dict)
        if response.status_code == 200:
            return response.json()  # Devuelve el pago registrado como dict
        else:
            print("Error registrando pago:", response.json().get("message", ""))
            return None
    except Exception as e:
        print("Error registrando pago:", e)
        return None


def eliminar_pago(idPago):
    """Delete using the backend REST API."""
    url = f"{RESTAPIBASEURL}pago/{idPago}/"
    try:
        response = requests.delete(url)
        return response.status_code == 200
    except Exception as e:
        print("Error eliminando pago:", e)
        return False


def get_pagos_from_db(idComercio):
    """Get pagos for a comercio using the backend REST API."""
    url = f"{RESTAPIBASEURL}comercio/{idComercio}/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # Lista de pagos
        else:
            return []
    except Exception as e:
        print("Error obteniendo pagos:", e)
        return []
