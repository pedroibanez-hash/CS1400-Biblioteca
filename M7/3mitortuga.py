# ==========================================
# TAREA 1 - Introducción a Turtle 🐢
# ==========================================
# En esta actividad aprenderás a:
# 1. Mover la tortuga hacia adelante.
# 2. Girarla usando grados.
# 3. Dibujar un cuadrado.
# 4. Usar un bucle para repetir instrucciones.
#
# IMPORTANTE:
# - Un giro completo es de 360 grados.
# - Un cuadrado tiene 4 lados iguales.
# - Cada esquina de un cuadrado mide 90 grados.
#
# Completa todos los TODO.

# ------------------------------------------
# Importaciones necesarias
# ------------------------------------------
#from turtle import make_turtle, forward, left
import turtle

<<<<<<< HEAD
<<<<<<< HEAD
#from turtle import make_turtle, forward, left
import turtle
=======
=======
>>>>>>> 4138345bb5449dc622c715ef49c8dae616a71e56
# 1. Iniciar ventana y objeto de tortuga
ventana = turtle.Screen()
t = turtle.Turtle() 
t.speed(3)
<<<<<<< HEAD
>>>>>>> 4138345bb5449dc622c715ef49c8dae616a71e56
=======
>>>>>>> 4138345bb5449dc622c715ef49c8dae616a71e56

# ------------------------------------------
# Paso 1: Crear la ventana y la tortuga
# ------------------------------------------
ventana = turtle.Screen()
my_tortugita= turtle.Turtle()

# TODO:
# Crea la tortuga usando make_turtle().
# La ventana debe tener 400 de alto y 400 de ancho.

# Escribe aquí tu código


# ------------------------------------------
# Paso 2: Dibujar una línea
# ------------------------------------------

# TODO:
# Mueve la tortuga hacia adelante 100 pasos.
# Observa qué sucede.
my_tortugita.forward(100)
# Escribe aquí tu código


# ------------------------------------------
# Paso 3: Girar la tortuga
# ------------------------------------------

# TODO:
# Gira la tortuga 90 grados hacia la izquierda.
# Luego avanza otros 100 pasos.
my_tortugita.left(90)
my_tortugita.forward(100)
# Escribe aquí tu código


# ------------------------------------------
# Paso 4: Dibujar un cuadrado (sin bucle)
# ------------------------------------------
# Un cuadrado tiene:
# - 4 lados
# - 4 giros de 90 grados

print("Dibujando un cuadrado sin bucle...")

# TODO:
# Completa los movimientos necesarios
# para dibujar un cuadrado de lado 100.
# Debes usar forward() y left() varias veces.
# La tortuga debe terminar donde empezó.

# Escribe aquí tu código

my_tortugita.forward(100)
my_tortugita.left(90)
my_tortugita.forward(100)
my_tortugita.left(90)
my_tortugita.forward(100)
my_tortugita.left(90)
my_tortugita.forward(100)
my_tortugita.left(90)
# ------------------------------------------
# Paso 5: Dibujar un cuadrado usando un bucle
# ------------------------------------------
# Ahora haremos lo mismo pero usando menos código.

print("Dibujando un cuadrado con bucle...")

# TODO:
# Usa un bucle for que repita 4 veces:
#   - avanzar 100
#   - girar 90 grados

for i in range(4):
   my_tortugita.forward(100)
   my_tortugita.left(90)


# ------------------------------------------
# Paso EXTRA (opcional)
# ------------------------------------------
# ¿Puedes dibujar un triángulo?
#
# Pista:
# - Un triángulo tiene 3 lados.
# - Un giro completo es 360 grados.
# - ¿Cuánto debe girar en cada esquina?
<<<<<<< HEAD
<<<<<<< HEAD

for i in range(3):
   my_tortugita.forward(100)
   my_tortugita.left(120)


turtle.done()
=======
ventana.exitonclick()
>>>>>>> 4138345bb5449dc622c715ef49c8dae616a71e56
=======
ventana.exitonclick()
>>>>>>> 4138345bb5449dc622c715ef49c8dae616a71e56
