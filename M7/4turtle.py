# ================================
# Proyecto: Dibujar una tarta con Turtle
# ================================
# En este ejercicio vas a:
# 1. Usar trigonometría para calcular la base de un triángulo isósceles.
# 2. Dibujar un triángulo con turtle.
# 3. Repetir el triángulo varias veces para formar una "tarta".
#
# ¡Lee cada paso con atención y completa los TODO!

# Importaciones necesarias
import math
from turtle import make_turtle, forward, left, right, penup, pendown

def triangulo(longitud, angulo):
    """
    TODO Paso 1:
    Escribe aquí qué hace esta función.
    
    Pista:
    - ¿Qué representa 'longitud'?
    - ¿Qué representa 'angulo'?
    - ¿Qué debería dibujar esta función?
    """
    
    # --------------------------------
    # Paso 2: Cálculos matemáticos
    # --------------------------------
    
    # Convierte el ángulo a radianes para poder usar funciones trigonométricas.
    angulo_rad = math.radians(angulo)
    
    # TODO:
    # Calcula la longitud de la base del triángulo isósceles.
    # Pista: estás trabajando con dos lados iguales (longitud)
    # y el ángulo central entre ellos.
    # Puedes usar math.sin().
    base =  # Escribe aquí el cálculo
    
    # TODO:
    # Calcula el ángulo que debe girar la tortuga en las esquinas
    # para que el triángulo se cierre correctamente.
    angulo_giro =  # Escribe aquí el cálculo

    # --------------------------------
    # Paso 3: Dibujo del triángulo
    # --------------------------------
    
    # Dibuja el triángulo usando forward() y left().
    # Recuerda:
    # - Debes dibujar dos lados iguales (longitud).
    # - Debes dibujar la base.
    # - La tortuga debe volver al punto inicial.
    
    # TODO:
    # Escribe aquí los movimientos necesarios.
    
    pass  # ⚠️ Borra esta línea cuando completes el código


def dibujar_tarta(n_porciones, longitud):
    """
    TODO:
    Explica qué hace esta función.
    
    Pista:
    - ¿Qué es n_porciones?
    - ¿Qué representa longitud?
    """
    
    # --------------------------------
    # Paso 4: Calcular el ángulo de cada porción
    # --------------------------------
    
    # TODO:
    # Calcula el ángulo central de cada porción.
    # Pista: un círculo completo tiene 360 grados.
    angulo_porcion =  # Divide 360 entre el número de porciones
    
    # --------------------------------
    # Paso 5: Dibujar todas las porciones
    # --------------------------------
    
    # TODO:
    # Escribe un bucle for que:
    # 1. Llame a la función triangulo(...)
    # 2. Gire la tortuga el ángulo necesario
    #    para dibujar la siguiente porción.
    
    # for ...:
    #     triangulo(...)
    #     left(...)
    
    pass  # ⚠️ Borra esta línea cuando completes el código



# ==================================
# Bloque para probar la función
# ==================================

make_turtle(height=400, width=600)

# ----------------------------------
# Prueba 1
# ----------------------------------

print("Dibujando una tarta de 5 porciones...")
dibujar_tarta(5, 80)

# ----------------------------------
# TODO EXTRA
# ----------------------------------
# 1. Levanta el lápiz (penup()).
# 2. Muévete a otra posición.
# 3. Baja el lápiz (pendown()).
# 4. Dibuja otra tarta con diferentes valores.


# ----------------------------------
# Prueba 2
# ----------------------------------

print("Dibujando una tarta de 8 porciones...")
dibujar_tarta(8, 60)