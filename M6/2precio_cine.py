"""
Tarea en casa #2: Calculadora de precio de entrada al cine
En este programa, el usuario ingresará su edad y si es fin de semana o no.
El programa calculará el precio de la entrada al cine basado en la edad del usuario
 y si es fin de semana o no, usando una estructura de control if/else anidada.
"""

    #TODO 1: Pedir al usuario su edad y usar un variable para ver si es fin de semana
    #  Intenta usar la funcion .lower() por si el usuario escribe "Sí" o "sí" o "SI" o algo similar. 
edad=int(input("Hola, Ingresa tu edad: "))
weekend=input("¿Es fin de semana? (sí/no):")
week=weekend.lower()
    #TODO 2: Usar if/else anidados para calcular el precio de la entrada
    #  al cine basado en las siguientes reglas:
    # menores de 12 años pagan $5 los fines de semana y $3 entre semana,
    # mayores de 65 años pagan $6 los fines de semana y $4 entre semana,
    # y todos los demás pagan $10 los fines de semana y $7 entre semana.
if edad > 65 and week == "si":
    precio=6.00
elif edad > 65 and week == "no":
    precio=4.00
elif edad < 12 and week == "si":
    precio=5.00
elif edad < 12 and week == "no":
    precio=3.00
else:
    if week == "si":
        precio=10.00
    else:
        precio=7.00
    #TODO 3: Imprimir el precio de la entrada al cine con un mensaje claro.
    # Por ejemplo, "El precio de tu entrada es: $5.00" intenta usar un f string para formatear.
print(f"El precio de tu entrada es: ${precio:.2f}")