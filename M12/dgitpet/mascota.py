# ============================================
# Mascota Virtual - Proyecto de Programación
# ============================================
# Este programa simula una mascota virtual usando
# una clase con atributos y métodos. El usuario
# puede jugar, alimentar y pasear a su mascota.
# ============================================

class MascotaVirtual:
    """Clase que representa una mascota virtual con estados de felicidad, hambre y salud."""

    # Inicializar los atributos de la mascota
    def __init__(self, nombre):
        self.nombre = nombre
        self.felicidad = 100
        self.hambre = 100  # 100 = lleno, 0 = muerto de hambre
        self.salud = 100

    # Método para jugar con la mascota
    def jugar(self):
        self.felicidad = min(self.felicidad + 10, 100)
        self.hambre = max(self.hambre - 5, 0)
        self.salud = max(self.salud - 3, 0)
        print(f"\n🎾 ¡{self.nombre} se divirtió jugando!")

    # Método para alimentar a la mascota
    def alimentar(self):
        self.hambre = min(self.hambre + 15, 100)
        self.felicidad = min(self.felicidad + 3, 100)
        self.salud = min(self.salud + 2, 100)
        print(f"\n🍖 ¡{self.nombre} comió y está satisfecho/a!")

    # Método para pasear a la mascota
    def pasear(self):
        self.salud = min(self.salud + 10, 100)
        self.felicidad = min(self.felicidad + 5, 100)
        self.hambre = max(self.hambre - 8, 0)
        print(f"\n🐾 ¡{self.nombre} disfrutó del paseo!")

    # Método para pasar el tiempo (desgaste natural cada turno)
    def pasar_tiempo(self):
        self.felicidad = max(self.felicidad - 3, 0)
        self.hambre = max(self.hambre - 4, 0)
        self.salud = max(self.salud - 2, 0)

    # Verificar si la mascota sigue viva
    def esta_viva(self):
        return self.felicidad > 0 and self.hambre > 0 and self.salud > 0

    # Mostrar el estado actual de la mascota
    def mostrar_estado(self):
        print(f"\nFelicidad: {self.felicidad}   Nivel de comida: {self.hambre}   Salud: {self.salud}")


# ---- Programa principal ----
def main():
    print("=" * 40)
    print("   🐶 Bienvenido a Mascota Virtual 🐶")
    print("=" * 40)

    nombre = input("\n¿Cómo quieres llamar a tu mascota? ")
    mascota = MascotaVirtual(nombre)

    print(f"\n¡Hola! Soy {nombre} y estoy listo/a para jugar contigo.")

    # Bucle principal del juego
    while mascota.esta_viva():
        mascota.mostrar_estado()
        print("1. Jugar")
        print("2. Alimentar")
        print("3. Pasear")
        print("4. Salir")

        opcion = input("\n¿Qué te gustaría hacer hoy? ")

        if opcion == "1":
            mascota.jugar()
        elif opcion == "2":
            mascota.alimentar()
        elif opcion == "3":
            mascota.pasear()
        elif opcion == "4":
            print(f"\n👋 ¡Adiós! {nombre} te extrañará.")
            break
        else:
            print("\n⚠️ Opción no válida. Intenta de nuevo.")
            continue

        # El tiempo pasa después de cada acción
        mascota.pasar_tiempo()

    # Si la mascota murió
    if not mascota.esta_viva():
        print(f"\n💀 Oh no... {nombre} no sobrevivió. ¡Cuida mejor a tu próxima mascota!")

    print("\nGracias por jugar. ¡Hasta la próxima!")


# Ejecutar el programa
if __name__ == "__main__":
    main()
