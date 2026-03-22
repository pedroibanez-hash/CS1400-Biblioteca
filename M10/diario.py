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