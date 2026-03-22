<<<<<<< HEAD
def menu():
    print("\n--- Diario Digital ---")
    print("1. Escribir una entrada")
    print("2. Leer entradas anteriores")
    print("3. Salir")
    return input("Selecciona una opción: ")

while True:
    opcion = menu()
    
    if opcion == "1":
        # Entrada de datos
        entrada = input("Escribe tu entrada: ")
        # Abrimos el archivo en modo 'a' (append/añadir)
        with open("diario.txt", "a") as archivo:
            archivo.write(entrada + "\n")
        print("¡Entrada guardada con éxito!")

    elif opcion == "2":
        # Leer el archivo
        try:
            with open("diario.txt", "r") as archivo:
                contenido = archivo.read()
                print("\n--- Entradas anteriores ---")
                print(contenido)
        except FileNotFoundError:
            print("\nAún no hay entradas creadas.")

    elif opcion == "3":
        print("¡Hasta luego!")
        break
        
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
=======
# --- Diaro de      Digital ---

# Aqui tu funcion menu()

while True:
    opcion = menu()

    #Aqui tu if/elif/elif/else statement con las opciones del menu
    
    # Entrada de datos
    # Guardar en archivo
    # Leer el archivo 

    
    # Salir de tu ultimo elif con un break
    # else solo para mostrar al usuario que no funciono lo que intentaron ingresar.
>>>>>>> 4138345bb5449dc622c715ef49c8dae616a71e56
