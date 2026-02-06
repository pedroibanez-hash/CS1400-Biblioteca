"""
Este programa debe darle al usuario la opción de elegir una comida de una lista.
El código asegura que lo ingresado sea legible (en minúsculas) y lo compara con una lista usando lógica if/else.
Al final, muestra un mensaje explicando de dónde es originaria esa comida.
"""

#Todo #1
print("Hola, Bienvenidos a la Biblioteca de Comida")
#TTodo #2

print("1.Hamburguesa \n 2.Pizza \n 3.Ensalada \n 4.Sushi \n 5.Tacos")
comida = input("Por favor, ingrese el nombre de la comida que desea: ")
correcta=comida.lower()
if correcta == "hamburguesa":
    print("Has seleccionado Hamburguesa y es Americana")
elif correcta == "pizza":
    print("Has seleccionado Pizza y es Italiana")
elif correcta == "ensalada":
    print("Has seleccionado Ensalada y es Mediterranea")
elif correcta == "sushi":
    print("Has seleccionado Sushi y es Japonesa")
elif correcta == "tacos":
    print("Has seleccionado Tacos y es Mexicana")   
else:
    print("Lo siento, no tenemos esa comida disponible.")

## Ejemplo de salida esperada:
"""
Bienvenido al programa de comidas de Latinoamérica.
Opciones: tacos, arepas, ceviche, pupusas, empanadas
¿Qué comida quieres conocer? Tacos
Los tacos son típicos de México.
"""
