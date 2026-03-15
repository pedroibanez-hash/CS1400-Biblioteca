def agregar_producto(inventario, nombre, precio):
    """
    Intenta convertir el precio a número y añadir el producto al inventario.
    
    Args:
        inventario (dict): Diccionario donde se guardan los productos.
        nombre (str): Nombre del producto.
        precio (any): Valor que se intentará convertir a float.
        
    Returns:
        bool: True si se agregó con éxito, False si el precio no era válido.
    """
    try:
        # Intentamos la conversión; si falla, salta directamente al except
        precio_num = float(precio)
        inventario[nombre] = precio_num
        return True
    except ValueError:
        # Maneja el error si el usuario ingresa texto en lugar de números
        return False

def buscar_precio(inventario, nombre):
    """
    Busca un producto en el diccionario usando su nombre como llave.
    
    Utiliza el método .get() que permite definir un valor por defecto 
    (None) si la llave no se encuentra, evitando errores de KeyError.
    """
    return inventario.get(nombre, None)

def listar_productos(inventario):
    """
    Muestra la lista de productos y precios.
    
    Verifica si el diccionario tiene elementos. Si está vacío, 
    notifica al usuario en lugar de mostrar una lista en blanco.
    """
    if not inventario:
        print("\n[!] El inventario se encuentra actualmente vacío.")
    else:
        print("\n--- Lista de Inventario ---")
        # .items() nos permite iterar sobre llave y valor simultáneamente
        for producto, precio in inventario.items():
            print(f"-> {producto}: ${precio:,.2f}")
        print("---------------------------")