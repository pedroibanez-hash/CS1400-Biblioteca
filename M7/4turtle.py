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
<<<<<<< HEAD
import turtle
#from turtle import make_turtle, forward, left, right, penup, pendown
ventana = turtle.Screen()
my_tortugita= turtle.Turtle()
=======
#from turtle import make_turtle, forward, left, right, penup, pendown
import turtle

# 1. Iniciar ventana y objeto de tortuga
window = turtle.Screen()
t = turtle.Turtle() 
t.speed(3)


>>>>>>> c439bd28f944149e0e626043b306a763bc6d6cfd

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
    base =  longitud * math.sin(math.pi/2 - angulo_rad) # Escribe aquí el cálculo
    
    # TODO:
    # Calcula el ángulo que debe girar la tortuga en las esquinas
    # para que el triángulo se cierre correctamente.
    angulo_giro =  120 

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
    my_tortugita.forward(longitud)
    my_tortugita.left(angulo_giro)      
    my_tortugita.forward(longitud)
    my_tortugita.left(angulo_giro)      
    my_tortugita.forward(longitud)
    my_tortugita.left(angulo_giro)      

   # pass  # ⚠️ Borra esta línea cuando completes el código


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
    angulo_porcion = 360/ n_porciones  # Divide 360 entre el número de porciones
    
    # --------------------------------
    # Paso 5: Dibujar todas las porciones
    # --------------------------------
    
    
    # TODO:
    # Escribe un bucle for que:
    # 1. Llame a la función triangulo(...)
    # 2. Gire la tortuga el ángulo necesario
    #    para dibujar la siguiente porción.
    
<<<<<<< HEAD
    for i in range(n_porciones):
         triangulo(longitud, 120)
         my_tortugita.left(angulo_porcion)
=======
    ###### for _ in range(n_porciones):
        # triangulo(...)
        # turtle.left(...)
        pass
########

    # for ...:
    #     triangulo(...)
    #     left(...)
>>>>>>> c439bd28f944149e0e626043b306a763bc6d6cfd
    
    pass  # ⚠️ Borra esta línea cuando completes el código



# ==================================
# Bloque para probar la función
# ==================================
####turtle.speed(5) # Ajusta la velocidad (1-10)
#####turtle.shape("turtle")

<<<<<<< HEAD
#mymake_turtle(height=400, width=600)
=======
#make_turtle(height=400, width=600)
>>>>>>> c439bd28f944149e0e626043b306a763bc6d6cfd

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
#### turtle.penup()
#### turtle.goto()

# ----------------------------------
# Prueba 2
# ----------------------------------

print("Dibujando una tarta de 8 porciones...")
dibujar_tarta(8, 60)
####turtle.done()