M11 - Modularizacion

Revisa todos los archivos incluidos en M11. Completa los pasos 1 - 6 para tener un programa completo. Tu proyecto final, debe tener al menos 3 archivos.

### Estructura del Proyecto 
El código se divide en tres archivos (módulos):

# utils.py (Utilidades de Procesamiento)
Este archivo se encarga de la fase de preparación.

Función: limpiar_y_tokenizar.

Objetivo: Recibe un texto sucio (con mayúsculas, puntos, comas) y lo convierte en una lista limpia de palabras que el modelo pueda entender.

# markov.py (El "Cerebro")
Aquí reside la lógica matemática y algorítmica.

Función: construir_modelo y generar_texto.

Objetivo: Crea el diccionario de probabilidades (frecuencias de palabras) y contiene el bucle que "elige" la siguiente palabra al azar basándose en la anterior.

# main.py (Punto de Entrada)
Es el archivo que orquesta todo.

Función: ejecutar_demo.

Objetivo: Importa las herramientas de los otros dos archivos, define el texto de ejemplo y muestra el resultado final al usuario. Es el único archivo que "imprime" resultados en la consola.

### Instrucciones
Para completar tu tarea, sigue estos pasos:

1. Completa utils.py: Asegúrate de que el texto se transforme correctamente a minúsculas y se eliminen los signos de puntuación.

2. Completa markov_engine.py:

En construir_modelo, asegúrate de que cada palabra se asocie con una lista de sus posibles seguidoras.

En generar_texto, completa el bucle for siguiendo los comentarios TODO. Recuerda usar random.choice().

3. Ejecuta main.py

4. Puntos Extra: Intercambia el text_base en main.py con un párrafo de tu libro favorito y observa cómo cambia el estilo de las frases generadas. 