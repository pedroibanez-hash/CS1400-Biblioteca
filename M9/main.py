# main.py
# Este es el programa principal para gestionar la tienda.
from gestion_tienda import agregar_producto, buscar_precio, listar_productos

def mostrar_menu():
    """
    Muestra las opciones disponibles en la consola.
    """
    # TODO #1 Completa el menú de opciones imprimiendo un mensaje y las opciones.
    print("\n--- 🛒 MENÚ DE GESTIÓN DE TIENDA ---")
    print("1. Ver inventario completo")
    print("2. Agregar o actualizar producto")
    print("3. Buscar precio de un producto")
    print("4. Salir")
    print("------------------------------------")

def ejecutar_programa():
    # TODO #2 iniciar un diccionario vacio
    mi_inventario = {} 
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            # Llama a la función del módulo gestion_tienda
            listar_productos(mi_inventario)

        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            precio = input("Precio: ")
            # La función agregar_producto maneja el ValueError internamente
            exito = agregar_producto(mi_inventario, nombre, precio)
            if exito:
                print(f"✅ '{nombre}' guardado correctamente.")
            else:
                print("❌ Error: El precio debe ser un número (ej: 10.50).")

        elif opcion == "3":
            nombre = input("¿Qué producto buscas?: ")
            precio = buscar_precio(mi_inventario, nombre)
            # Verificamos 'is not None' para permitir precios de $0.00
            if precio is not None:
                print(f"🔍 El precio de '{nombre}' es ${precio:.2f}")
            else:
                print(f"⚠️ El producto '{nombre}' no existe.")

        elif opcion == "4":
            print("Saliendo del sistema... ¡Buen día!")
            break
        
        else:
            print("🚫 Opción no válida, intenta de nuevo.")

# El programa se ejecutará desde aquí
if __name__ == "__main__":
    ejecutar_programa()