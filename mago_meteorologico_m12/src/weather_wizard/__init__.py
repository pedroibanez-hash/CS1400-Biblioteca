"""
Este archivo expone las funciones principales para que sean fáciles de importar.
"""

from .motor import obtener_clima_ciudad
from .api import fetch_weather_from_provider

# Esto define qué se importa cuando alguien hace "from weather_wizard import *"
__all__ = ["obtener_clima_ciudad", "fetch_weather_from_provider"]

__version__ = "0.1.0"
__author__ = "Tu Nombre o el de tus Estudiantes"