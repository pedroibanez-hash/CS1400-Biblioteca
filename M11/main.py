# main.py
from utils import limpiar_y_tokenizar
from markov import construir_modelo, generar_texto

def ejecutar_demo():
    # 1. Datos de entrada
    texto_base = "Un pez nada. Otro pez tambien nada. El pez es azul. El agua es clara."
    
    # 2. Procesamiento (Usando utils.py)
    palabras = limpiar_y_tokenizar(texto_base)
    
    # 3. Construcción (Usando markov_engine.py)
    modelo = construir_modelo(palabras)
    
    # 4. Generación
    print("--- Generador de Texto Markov ---")
    resultado = generar_texto(modelo, "pez", 5)
    
    print(f"Resultado: {resultado}")

# TODO Paso 6.
# Llama a ejecutar_demo() dentro de un bloque if __name__ == "__main__":