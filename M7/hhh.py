def calculadora_segura():
    print("\n--- Bienvenido a la Calculadora Robusta ---")
    
    while True:
        try:
            # Solicitar datos
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número: "))
            op = input("Operación (+, -, *, /): ")

            # Validar operación (Regla de negocio)
            if op not in ['+', '-', '*', '/']:
                # TODO: Lanza (raise) una excepción ValueError con el mensaje "Operador no válido"
                pass

            # Realizar cálculos
            if op == '+':
                resultado = n1 + n2
            elif op == '-':
                resultado = n1 - n2
            elif op == '*':
                resultado = n1 * n2
            elif op == '/':
                # Python lanzará ZeroDivisionError automáticamente si n2 es 0
                resultado = n1 / n2

            print(f"✅ Resultado: {resultado}")
            break # Rompe el bucle si todo salió bien

        # --- MANEJO DE ERRORES ---
        
        # TODO: Crea un except para cuando el usuario ingrese letras en vez de números
        # except ... :
        #    print("Error: Solo se admiten números.")
        except ValueError as e:
            # Captura tanto letras en inputs como el operador no válido
            print(f"❌ Error de entrada: {e}")

        # TODO: Crea un except para la división por cero
        # except ... :
        #    print("Error: No puedes dividir un pastel entre cero personas.")
        except ZeroDivisionError:
            print("❌ Error: No puedes dividir un pastel entre cero personas.")

        # TODO: Crea un except para capturar el ValueError del operador no válido
        # except ValueError as e:
        #    print(f"Error de entrada: {e}")

        except Exception as e:
            print(f"Algo salió muy mal: {e}")
        
        finally:
            # TODO: Imprime un mensaje que diga "Intento de cálculo finalizado" 
            # (Este debe aparecer SIEMPRE, haya error o no)
            pass

calculadora_segura()