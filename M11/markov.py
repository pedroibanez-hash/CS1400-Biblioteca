import random

def construir_modelo(palabras):
    """
    Crea un diccionario donde cada palabra es una clave y su valor
    es una lista de todas las palabras que la siguen.
    """
    modelo = {}
    for i in range(len(palabras) - 1):
        palabra_actual = palabras[i]
        palabra_siguiente = palabras[i + 1]
        
        if palabra_actual not in modelo:
            modelo[palabra_actual] = []
        
        modelo[palabra_actual].append(palabra_siguiente)
    
    return modelo

def generar_texto(modelo, palabra_inicial, longitud):
    """
    Genera una secuencia de palabras basada en las probabilidades del modelo.
    """
    # Paso 4. Inicializa la frase con la palabra inicial
    frase_generada = [palabra_inicial]
    palabra_actual = palabra_inicial

    # Paso 5. Bucle for con un if/else para generar palabras (IDENTADO)
    for _ in range(longitud - 1):
        # Verificamos si la palabra actual existe en nuestro modelo
        if palabra_actual in modelo:
            # Elegimos una palabra al azar de las opciones disponibles
            palabra_siguiente = random.choice(modelo[palabra_actual])
            frase_generada.append(palabra_siguiente)
            # Actualizamos para la siguiente iteración
            palabra_actual = palabra_siguiente
        else:
            # Si llegamos a una palabra que no tiene "seguidoras", nos detenemos
            break
            
    # Unir y devolver (IDENTADO dentro de la función)
    return " ".join(frase_generada)