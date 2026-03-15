En este proyecto hay que completar los TODO en el main.py y en el gestion_tienda.py. Luego correr test_tienda.py con el comando python test_tienda.py

Objetivo
Crear un programa que gestione productos mediante un diccionario. El programa debe permitir añadir, buscar y listar productos, manejando posibles errores del usuario.

🛠️ Requisitos Técnicos
Para completar este proyecto, deberás aplicar los siguientes conceptos:
-- Diccionarios: Para almacenar nombre_producto: precio.
-- Funciones: El código debe estar organizado (ej: agregar_producto(), mostrar_menu()).
-- Bucles y Condicionales: Un bucle while para el menú y if/else para validar opciones.
-- Manejo de Errores: Uso de try/except para que el programa no "explote" si el usuario ingresa texto en lugar de un precio.

📋 Lista de Tareas Estructura Base: Define un diccionario vacío llamado inventario.
Menú Principal: Crea un bucle que muestre estas opciones:
1. Ver productos
2. Agregar/Actualizar producto
3. Buscar precio
4. Salir

Lógica de Funciones:
Ver: Recorrer el diccionario con un for y mostrar "Producto: [Nombre] - Precio: $[Valor]".
Agregar: Pedir nombre y precio. Si el producto ya existe, actualizar el precio.
Buscar: Pedir el nombre y mostrar su precio. Si no existe, avisar al usuario.
Validación: Asegúrate de que los precios sean siempre números (usa float()).

Robustez:
Asegúrate de que si el usuario escribe una letra donde se espera un precio, el programa le envíe un mensaje de aviso en lugar de cerrarse.

Cierre y Guardado:
Al salir, el programa debe volcar toda la información del diccionario al archivo o base de datos.

Ejemplo de Ejecución
--- MENÚ DE LA TIENDITA ---
1. Ver inventario
2. Agregar producto
3. Guardar y Salir
Seleccione una opción: 2

Nombre del producto: Manzanas
Precio: 2.50
¡Producto agregado con éxito!

Autoevaluación con VSC
Para verificar que tu lógica es correcta antes de entregar, sigue estos pasos:
Asegúrate de que tus funciones se llamen exactamente agregar_producto y buscar_precio.
Descarga el archivo test_tienda.py en la misma carpeta que tu código.

Si ves todos los ✅, ¡tu lógica está lista!