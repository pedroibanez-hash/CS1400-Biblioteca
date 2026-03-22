"""
========================================
  Widget Flotante Pomodoro
  Técnica Pomodoro - Gestor de Tiempo
========================================
Descripción:
    Widget flotante que implementa la técnica Pomodoro.
    Permite iniciar sesiones de trabajo de 25 minutos
    seguidas de descansos cortos de 5 minutos.

Estructura del proyecto:
    - Fase 1: Repositorio Git configurado
    - Fase 2: Pseudocódigo y diagrama de flujo
    - Fase 3: MVP funcional (este archivo)

Autor: Equipo Pomodoro
Versión: 1.0 MVP
"""

# ── Importaciones ─────────────────────────────────────────────────────────────
import tkinter as tk          # Interfaz gráfica estándar de Python
import tkinter.messagebox     # Ventanas emergentes de notificación
import time                   # Manejo del tiempo
import threading              # Hilo secundario para el temporizador
import sys                    # Información del sistema operativo


# ── Constantes de configuración ───────────────────────────────────────────────
TIEMPO_TRABAJO    = 25 * 60   # 25 minutos en segundos
TIEMPO_DESCANSO   = 5  * 60   # 5 minutos en segundos
POMODOROS_META    = 4         # Cantidad de pomodoros antes del descanso largo
TIEMPO_DESC_LARGO = 15 * 60   # 15 minutos de descanso largo

# Colores del widget
COLOR_TRABAJO     = "#E8593C"  # Rojo-naranja para modo trabajo
COLOR_DESCANSO    = "#1D9E75"  # Verde para modo descanso
COLOR_DESC_LARGO  = "#185FA5"  # Azul para descanso largo
COLOR_TEXTO       = "#FFFFFF"  # Texto blanco
COLOR_FONDO       = "#2C2C2A"  # Fondo oscuro
COLOR_BOTON       = "#3d3d3a"  # Botones neutros
COLOR_BTN_HOVER   = "#5F5E5A"  # Hover de botones


# ── Pseudocódigo (referencia académica, Fase 2) ───────────────────────────────
"""
PSEUDOCÓDIGO - Widget Pomodoro
==============================
1.  INICIO
2.  INICIALIZAR variables:
        tiempo_restante  ← TIEMPO_TRABAJO
        pomodoros_completados ← 0
        modo_actual ← "trabajo"
        temporizador_activo ← FALSO
3.  CREAR ventana flotante always-on-top
4.  MOSTRAR tiempo_restante en pantalla

5.  MIENTRAS el_programa_está_corriendo:
6.      SI el_usuario_presiona_INICIO:
7.          temporizador_activo ← VERDADERO
8.          INICIAR hilo_temporizador()

9.  FUNCIÓN hilo_temporizador():
10.     MIENTRAS temporizador_activo Y tiempo_restante > 0:
11.         ESPERAR 1 segundo
12.         tiempo_restante ← tiempo_restante - 1
13.         ACTUALIZAR display con tiempo_restante
14.
15.     SI tiempo_restante == 0:
16.         NOTIFICAR al usuario (sonido + alerta visual)
17.         pomodoros_completados ← pomodoros_completados + 1
18.
19.         SI modo_actual == "trabajo":
20.             SI pomodoros_completados % 4 == 0:
21.                 modo_actual ← "descanso_largo"
22.                 tiempo_restante ← TIEMPO_DESC_LARGO
23.             SINO:
24.                 modo_actual ← "descanso"
25.                 tiempo_restante ← TIEMPO_DESCANSO
26.         SINO:
27.             modo_actual ← "trabajo"
28.             tiempo_restante ← TIEMPO_TRABAJO
29.
30.         ACTUALIZAR color_widget según modo_actual
31.         CONTINUAR temporizador automáticamente
32.
33.  SI el_usuario_presiona_PAUSA:
34.      temporizador_activo ← FALSO
35.
36.  SI el_usuario_presiona_RESET:
37.      temporizador_activo ← FALSO
38.      tiempo_restante ← TIEMPO_TRABAJO
39.      modo_actual ← "trabajo"
40.      ACTUALIZAR display
41.
42. FIN
"""


# ── Clase principal del Widget ────────────────────────────────────────────────
class PomodoroWidget:
    """
    Widget flotante que implementa la técnica Pomodoro.

    Atributos:
        ventana              : Ventana principal de tkinter
        tiempo_restante (int): Segundos restantes en el ciclo actual
        activo         (bool): Estado del temporizador (corriendo/pausado)
        modo           (str) : Modo actual ('trabajo', 'descanso', 'largo')
        pomodoros      (int) : Pomodoros completados en la sesión
        hilo           (Thread): Hilo del temporizador en segundo plano
    """

    def __init__(self):
        """Inicializa el widget, configura la ventana y los elementos UI."""

        # ── Estado interno del temporizador ───────────────────────────────────
        self.tiempo_restante = TIEMPO_TRABAJO   # Segundos restantes
        self.activo          = False            # ¿Está corriendo?
        self.modo            = "trabajo"        # Modo actual
        self.pomodoros       = 0                # Contador de pomodoros
        self.hilo            = None             # Hilo del contador
        self._arrastrar_x    = 0                # Coordenada X para arrastrar
        self._arrastrar_y    = 0                # Coordenada Y para arrastrar

        # ── Configuración de la ventana ───────────────────────────────────────
        self.ventana = tk.Tk()
        self.ventana.title("Pomodoro")
        self.ventana.overrideredirect(True)      # Sin borde de sistema operativo
        self.ventana.attributes("-topmost", True) # Siempre encima
        self.ventana.configure(bg=COLOR_FONDO)

        # Opacidad (transparencia leve para que no sea invasivo)
        try:
            self.ventana.attributes("-alpha", 0.95)
        except Exception:
            pass  # Algunos sistemas no soportan transparencia

        # ── Posición inicial: esquina superior derecha ─────────────────────────
        ancho_pantalla = self.ventana.winfo_screenwidth()
        self.ventana.geometry(f"220x280+{ancho_pantalla - 240}+40")

        # ── Construcción de la interfaz ────────────────────────────────────────
        self._construir_ui()

        # ── Eventos para arrastrar el widget ──────────────────────────────────
        self.ventana.bind("<ButtonPress-1>",   self._iniciar_arrastre)
        self.ventana.bind("<B1-Motion>",       self._arrastrar)

        # Iniciar el loop principal
        self.ventana.mainloop()

    # ── Construcción de la interfaz de usuario ────────────────────────────────
    def _construir_ui(self):
        """Crea y posiciona todos los elementos visuales del widget."""

        # Marco contenedor principal
        self.marco = tk.Frame(
            self.ventana,
            bg=COLOR_FONDO,
            highlightthickness=0
        )
        self.marco.pack(fill="both", expand=True, padx=0, pady=0)

        # ── Barra superior: título y botón cerrar ─────────────────────────────
        barra = tk.Frame(self.marco, bg=COLOR_FONDO)
        barra.pack(fill="x", padx=10, pady=(10, 0))

        self.lbl_titulo = tk.Label(
            barra,
            text="🍅 POMODORO",
            font=("Helvetica", 10, "bold"),
            bg=COLOR_FONDO,
            fg="#B4B2A9"
        )
        self.lbl_titulo.pack(side="left")

        btn_cerrar = tk.Label(
            barra,
            text="✕",
            font=("Helvetica", 11),
            bg=COLOR_FONDO,
            fg="#888780",
            cursor="hand2"
        )
        btn_cerrar.pack(side="right")
        btn_cerrar.bind("<Button-1>", lambda e: self.ventana.destroy())

        # ── Indicador de modo (trabajo / descanso) ────────────────────────────
        self.lbl_modo = tk.Label(
            self.marco,
            text="TIEMPO DE TRABAJO",
            font=("Helvetica", 9),
            bg=COLOR_FONDO,
            fg=COLOR_TRABAJO
        )
        self.lbl_modo.pack(pady=(12, 0))

        # ── Display principal del temporizador ────────────────────────────────
        self.lbl_tiempo = tk.Label(
            self.marco,
            text=self._formatear_tiempo(self.tiempo_restante),
            font=("Helvetica", 48, "bold"),
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO
        )
        self.lbl_tiempo.pack(pady=(4, 0))

        # ── Barra de progreso circular (canvas) ───────────────────────────────
        self.canvas_prog = tk.Canvas(
            self.marco,
            width=180, height=8,
            bg=COLOR_FONDO,
            highlightthickness=0
        )
        self.canvas_prog.pack(pady=(6, 0))
        self._dibujar_progreso(1.0)  # Progreso inicial completo

        # ── Contador de pomodoros completados ─────────────────────────────────
        self.lbl_contador = tk.Label(
            self.marco,
            text=self._texto_pomodoros(),
            font=("Helvetica", 9),
            bg=COLOR_FONDO,
            fg="#888780"
        )
        self.lbl_contador.pack(pady=(8, 0))

        # ── Botones de control ────────────────────────────────────────────────
        marco_botones = tk.Frame(self.marco, bg=COLOR_FONDO)
        marco_botones.pack(pady=(14, 10))

        # Botón Iniciar / Pausar
        self.btn_play = tk.Button(
            marco_botones,
            text="▶  Iniciar",
            font=("Helvetica", 11, "bold"),
            bg=COLOR_TRABAJO,
            fg=COLOR_TEXTO,
            relief="flat",
            bd=0,
            padx=18, pady=7,
            cursor="hand2",
            command=self._toggle_temporizador
        )
        self.btn_play.grid(row=0, column=0, padx=5)

        # Botón Reiniciar
        btn_reset = tk.Button(
            marco_botones,
            text="↺",
            font=("Helvetica", 13),
            bg=COLOR_BOTON,
            fg="#B4B2A9",
            relief="flat",
            bd=0,
            padx=10, pady=6,
            cursor="hand2",
            command=self._reiniciar
        )
        btn_reset.grid(row=0, column=1, padx=5)
        btn_reset.bind("<Enter>", lambda e: btn_reset.config(bg=COLOR_BTN_HOVER))
        btn_reset.bind("<Leave>", lambda e: btn_reset.config(bg=COLOR_BOTON))

        # Botón Saltar al siguiente ciclo
        btn_saltar = tk.Button(
            marco_botones,
            text="⏭",
            font=("Helvetica", 13),
            bg=COLOR_BOTON,
            fg="#B4B2A9",
            relief="flat",
            bd=0,
            padx=10, pady=6,
            cursor="hand2",
            command=self._saltar_ciclo
        )
        btn_saltar.grid(row=0, column=2, padx=5)
        btn_saltar.bind("<Enter>", lambda e: btn_saltar.config(bg=COLOR_BTN_HOVER))
        btn_saltar.bind("<Leave>", lambda e: btn_saltar.config(bg=COLOR_BOTON))

    # ── Lógica del temporizador ───────────────────────────────────────────────
    def _toggle_temporizador(self):
        """Alterna entre iniciar y pausar el temporizador."""

        if self.activo:
            # Pausar: detener el hilo
            self.activo = False
            self.btn_play.config(text="▶  Continuar")
        else:
            # Iniciar: crear hilo del temporizador
            self.activo = True
            self.btn_play.config(text="⏸  Pausar")
            # Hilo daemon: se cierra automáticamente con la ventana
            self.hilo = threading.Thread(target=self._correr_temporizador, daemon=True)
            self.hilo.start()

    def _correr_temporizador(self):
        """
        Bucle principal del temporizador (corre en hilo separado).

        Estructura de control:
            - BUCLE WHILE: descuenta tiempo mientras está activo
            - CONDICIONAL: detecta fin del ciclo
            - CONDICIONAL anidado: decide el siguiente modo
        """

        # BUCLE: corre mientras el temporizador esté activo y haya tiempo
        while self.activo and self.tiempo_restante > 0:
            time.sleep(1)                        # Esperar 1 segundo real
            self.tiempo_restante -= 1            # Descontar un segundo

            # Actualizar la interfaz (desde el hilo principal con after)
            self.ventana.after(0, self._actualizar_display)

        # CONDICIONAL: verificar si el tiempo llegó a cero (fin de ciclo)
        if self.tiempo_restante == 0 and self.activo:
            self.activo = False
            self.ventana.after(0, self._ciclo_completado)

    def _ciclo_completado(self):
        """
        Maneja la transición entre ciclos al llegar a cero.
        Notifica al usuario y determina el siguiente modo.
        """

        # CONDICIONAL: determinar qué ciclo terminó y cuál sigue
        if self.modo == "trabajo":
            self.pomodoros += 1  # Incrementar contador de pomodoros

            # CONDICIONAL: verificar si corresponde descanso largo
            if self.pomodoros % POMODOROS_META == 0:
                self.modo            = "largo"
                self.tiempo_restante = TIEMPO_DESC_LARGO
                mensaje = f"¡Completaste {self.pomodoros} pomodoros!\nTómate un descanso largo de 15 minutos 🎉"
            else:
                self.modo            = "descanso"
                self.tiempo_restante = TIEMPO_DESCANSO
                mensaje = "¡Buen trabajo! Tómate 5 minutos de descanso ☕"

        else:
            # Fin del descanso → volver a trabajar
            self.modo            = "trabajo"
            self.tiempo_restante = TIEMPO_TRABAJO
            mensaje = "¡Descanso terminado! Hora de concentrarse 🍅"

        # Actualizar colores y texto del widget según el nuevo modo
        self._actualizar_colores()
        self._actualizar_display()

        # Notificación emergente al usuario
        tkinter.messagebox.showinfo("Pomodoro", mensaje)

        # Auto-iniciar el siguiente ciclo
        self.activo = True
        self.btn_play.config(text="⏸  Pausar")
        self.hilo = threading.Thread(target=self._correr_temporizador, daemon=True)
        self.hilo.start()

    def _reiniciar(self):
        """Reinicia el temporizador al estado inicial de trabajo."""
        self.activo          = False    # Detener cualquier hilo activo
        self.modo            = "trabajo"
        self.tiempo_restante = TIEMPO_TRABAJO
        self.btn_play.config(text="▶  Iniciar")
        self._actualizar_colores()
        self._actualizar_display()

    def _saltar_ciclo(self):
        """Salta al siguiente ciclo sin esperar que termine el actual."""
        self.activo          = False
        self.tiempo_restante = 0
        # Simular fin de ciclo desde el hilo principal
        self.ventana.after(100, self._ciclo_completado)

    # ── Actualización visual ──────────────────────────────────────────────────
    def _actualizar_display(self):
        """Actualiza el label del tiempo y la barra de progreso."""

        # Actualizar texto del temporizador
        self.lbl_tiempo.config(
            text=self._formatear_tiempo(self.tiempo_restante)
        )

        # Calcular progreso (fracción de tiempo restante)
        if self.modo == "trabajo":
            total = TIEMPO_TRABAJO
        elif self.modo == "descanso":
            total = TIEMPO_DESCANSO
        else:
            total = TIEMPO_DESC_LARGO

        fraccion = self.tiempo_restante / total
        self._dibujar_progreso(fraccion)

        # Actualizar contador de pomodoros
        self.lbl_contador.config(text=self._texto_pomodoros())

    def _actualizar_colores(self):
        """Cambia los colores del widget según el modo actual."""

        # CONDICIONAL: asignar color según el modo
        if self.modo == "trabajo":
            color     = COLOR_TRABAJO
            texto_modo = "TIEMPO DE TRABAJO"
        elif self.modo == "descanso":
            color     = COLOR_DESCANSO
            texto_modo = "DESCANSO CORTO"
        else:
            color     = COLOR_DESC_LARGO
            texto_modo = "DESCANSO LARGO"

        # Aplicar color al botón y etiqueta de modo
        self.btn_play.config(bg=color)
        self.lbl_modo.config(text=texto_modo, fg=color)

    def _dibujar_progreso(self, fraccion):
        """
        Dibuja una barra de progreso horizontal.

        Args:
            fraccion (float): Valor entre 0.0 y 1.0 que indica el progreso.
        """
        self.canvas_prog.delete("all")           # Limpiar canvas
        ancho_total = 180
        alto        = 8

        # Fondo de la barra (gris)
        self.canvas_prog.create_rectangle(
            0, 0, ancho_total, alto,
            fill="#444441", outline=""
        )

        # Determinar color según modo
        if self.modo == "trabajo":
            color_barra = COLOR_TRABAJO
        elif self.modo == "descanso":
            color_barra = COLOR_DESCANSO
        else:
            color_barra = COLOR_DESC_LARGO

        # Barra de progreso activa
        ancho_activo = max(8, int(ancho_total * fraccion))
        self.canvas_prog.create_rectangle(
            0, 0, ancho_activo, alto,
            fill=color_barra, outline=""
        )

    # ── Arrastre del widget ───────────────────────────────────────────────────
    def _iniciar_arrastre(self, evento):
        """Registra la posición inicial del clic para arrastrar la ventana."""
        self._arrastrar_x = evento.x
        self._arrastrar_y = evento.y

    def _arrastrar(self, evento):
        """Mueve la ventana según el movimiento del mouse."""
        delta_x = evento.x - self._arrastrar_x
        delta_y = evento.y - self._arrastrar_y
        nueva_x = self.ventana.winfo_x() + delta_x
        nueva_y = self.ventana.winfo_y() + delta_y
        self.ventana.geometry(f"+{nueva_x}+{nueva_y}")

    # ── Utilidades ────────────────────────────────────────────────────────────
    def _formatear_tiempo(self, segundos):
        """
        Convierte segundos a formato MM:SS.

        Args:
            segundos (int): Total de segundos a formatear.

        Returns:
            str: Tiempo en formato "MM:SS".
        """
        minutos = segundos // 60
        segs    = segundos % 60
        return f"{minutos:02d}:{segs:02d}"

    def _texto_pomodoros(self):
        """Genera el texto del contador de pomodoros con círculos visuales."""
        # Mostrar hasta 4 círculos; rellenos según pomodoros completados en el ciclo
        completados_ciclo = self.pomodoros % POMODOROS_META
        circulos = "●" * completados_ciclo + "○" * (POMODOROS_META - completados_ciclo)
        return f"{circulos}  {self.pomodoros} completados"


# ── Punto de entrada ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    """
    Inicia el widget Pomodoro.

    Requisitos:
        - Python 3.7+
        - tkinter (incluido en Python estándar)
        - No requiere instalación de dependencias externas
    """
    print("=" * 45)
    print("  Widget Flotante Pomodoro  🍅")
    print("=" * 45)
    print("  Iniciando interfaz gráfica...")
    print("  Arrastra el widget a donde prefieras.")
    print("  Ciérralo con el botón ✕ del widget.")
    print("=" * 45)

    # Crear e iniciar el widget (blocking hasta que se cierre la ventana)
    app = PomodoroWidget()