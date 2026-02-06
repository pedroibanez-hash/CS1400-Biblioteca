# Practicando lógica booleana en Python aprendiendo a usar "and", "or" y "not"

# Declaracion de valores o inicialización de Valores para probar diferentes combinaciones
edad = 16
tiene_permiso = True
es_finde = False

# TODO 1: Usa una expresión booleana con "and"
# Por ejemplo: ¿Puede salir hoy solo si tiene 18 años o más Y si tiene permiso?
tu_edad=int(input("Por favor ingresa, Tu Edad: "))
if tu_edad>=18 and tiene_permiso:
    print("Puede salir")
else:
    print("No puedo salir ")
# TODO 2: Usa una expresión booleana con "or" para permitir salir si es fin de semana o tiene permiso

tu_edad=int(input("Por favor ingresa, Tu Edad: "))
if tu_edad>=18 and (tiene_permiso or es_finde):
    print("Puede salir")
else:
    print("No puedo salir ")

# TODO 3: Usa una expresión booleana con "not" para negar una condición
# Por ejemplo: De ninguna manera tiene permiso

tu_edad=int(input("Por favor ingresa, Tu Edad: "))

if not tiene_permiso:
    print("puede salir")
else:
    print("no Puede salir ")

# TODO 5: Escribe tu propia condición con and, or o not e imprimelo a la pantalla.
# Ejemplo: ¿Puede conducir si tiene 18 o más y tiene permiso? u cualquier otra idea. t
print("¿Puede conducir si y solo si tiene 18 o más y ademas tiene permiso?")
tu_edad=int(input("Por favor ingresa, Tu Edad: "))
if tu_edad >= 18 and tiene_permiso:
    print("Resultado: ¡Sí, puedes conducir! Tienes la edad y el permiso.")
else:
    print("Resultado: No puedes conducir. Te falta la edad o el permiso.")