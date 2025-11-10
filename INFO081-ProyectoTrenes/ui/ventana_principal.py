# ui/ventana_principal.py
import tkinter as tk
from tkinter import filedialog, messagebox

# Importar configuraciones
from config.colores import (
    COLOR_FONDO, COLOR_TEXTO, COLOR_BOTON, COLOR_TEXTO_BOTON,
    COLOR_BOTON_HOVER, COLOR_PANEL
)
from config.tamaño_ventana import ANCHO_VENTANA, ALTO_VENTANA

# Importar la lógica y otras ventanas
from logic.estado_simulacion import EstadoDeSimulacion
from logic.sistema_guardado import SistemaGuardado
from ui.ventana_estaciones import VentanaEstaciones

# Definir estilos comunes de los widgets
estilo_boton = {
    "bg": COLOR_BOTON,
    "fg": COLOR_TEXTO_BOTON,
    "font": ("Segoe UI", 12, "bold"),
    "width": 25,
    "height": 2,
    "relief": "flat",
    "activebackground": COLOR_BOTON_HOVER,
    "activeforeground": COLOR_TEXTO_BOTON
}

estilo_label = {
    "bg": COLOR_FONDO,
    "fg": COLOR_TEXTO,
    "font": ("Segoe UI", 10)
}

class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        
        #Configuración de la Ventana
        self.title("Simulador de Tráfico Ferroviario (EFE)")
        self.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}")
        self.config(bg=COLOR_FONDO)
        self.resizable(False, False)

        #Componentes Centrales
        self.estado = EstadoDeSimulacion()
        self.guardador = SistemaGuardado()
        
        #Asignar el callback para que el estado actualice la UI
        self.estado.set_update_callback(self.actualizar_vista_simulacion)

        #Frames de la Aplicación
        self.frame_menu = None
        self.frame_simulacion = None
        
        # Iniciar mostrando el menú principal
        self.crear_menu_principal()

    def _limpiar_frames(self):
        """Oculta todos los frames principales."""
        if self.frame_menu:
            self.frame_menu.pack_forget()
        if self.frame_simulacion:
            self.frame_simulacion.pack_forget()

    def crear_menu_principal(self):
        """Crea la pantalla del Menú Principal (basado en tu main.py)"""
        self._limpiar_frames()
        
        self.frame_menu = tk.Frame(self, bg=COLOR_FONDO)
        self.frame_menu.pack(fill="both", expand=True)
        
        titulo = tk.Label(
            self.frame_menu, 
            text="Sistema de Simulación Ferroviaria", 
            bg=COLOR_FONDO, 
            fg=COLOR_TEXTO, 
            font=("Segoe UI", 20, "bold")
        )
        titulo.pack(pady=40)

        # Botones del menú principal
        btn_iniciar = tk.Button(
            self.frame_menu, 
            text="INICIAR NUEVA SIMULACIÓN", 
            command=self.iniciar_nueva_simulacion, 
            **estilo_boton
        )
        btn_iniciar.pack(pady=10)

        btn_cargar = tk.Button(
            self.frame_menu, 
            text="CARGAR SIMULACIÓN", 
            command=self.cargar_simulacion, 
            **estilo_boton
        )
        btn_cargar.pack(pady=10)

        btn_estaciones = tk.Button(
            self.frame_menu, 
            text="GESTIONAR ESTACIONES", 
            command=self.abrir_gestion_estaciones, 
            **estilo_boton
        )
        btn_estaciones.pack(pady=10)
        
        #Espacio para agregar botones para Trenes y Rutas aquí

        btn_salir = tk.Button(
            self.frame_menu, 
            text="SALIR", 
            command=self.quit, 
            **estilo_boton
        )
        btn_salir.pack(pady=10)

    def crear_vista_simulacion(self):
        """Crea la pantalla de "SIMULACION EN EJECUCION"""
        self._limpiar_frames()
            
        self.frame_simulacion = tk.Frame(self, bg=COLOR_FONDO)
        self.frame_simulacion.pack(fill="both", expand=True, padx=10, pady=10)
        
        #Frame Superior (Controles)
        frame_controles = tk.Frame(self.frame_simulacion, bg=COLOR_FONDO)
        frame_controles.pack(fill="x", pady=5)
        
        # 1. Botón Avanzar
        estilo_avanzar = estilo_boton.copy()
        estilo_avanzar['width'] = 15
        estilo_avanzar['height'] = 1
        
        self.btn_avanzar = tk.Button(
            frame_controles, 
            text="Avanzar Evento", 
            command=self.estado.avanzar_al_siguiente_evento, 
            **estilo_avanzar
        )
        self.btn_avanzar.pack(side="left", padx=10)
        
        # 2. Botón Guardar
        estilo_guardar = estilo_boton.copy()
        estilo_guardar['width'] = 10
        estilo_guardar['height'] = 1
        
        self.btn_guardar = tk.Button(
            frame_controles, 
            text="Guardar", 
            command=self.guardar_simulacion, 
            **estilo_guardar
        )
        self.btn_guardar.pack(side="left", padx=10)
        
        # 3. Botón Volver
        estilo_volver = estilo_boton.copy()
        estilo_volver['width'] = 15
        estilo_volver['height'] = 1
        
        self.btn_volver_menu = tk.Button(
            frame_controles, 
            text="Volver al Menú", 
            command=self.crear_menu_principal, 
            **estilo_volver
        )
        self.btn_volver_menu.pack(side="right", padx=10)

        #Frame Central (Visualización e Indicadores)
        frame_display = tk.Frame(self.frame_simulacion, bg=COLOR_FONDO)
        frame_display.pack(fill="both", expand=True, pady=10)

        #Estilo para los TÍTULOS
        estilo_titulo_panel = estilo_label.copy()
        estilo_titulo_panel['bg'] = COLOR_PANEL # Usamos el fondo del panel

        #Estilo para los VALORES 
        estilo_valor_panel = estilo_label.copy()
        estilo_valor_panel['bg'] = COLOR_PANEL     # Usamos el fondo del panel
        estilo_valor_panel['font'] = ("Courier", 14) # Cambiamos la fuente

        # Panel de Estado
        frame_estado = tk.Frame(frame_display, bg=COLOR_PANEL, relief="sunken", borderwidth=1)
        frame_estado.pack(side="left", fill="y", padx=10, pady=5)
        
        #estilo_titulo_panel (Tiempo Transcurrido)
        tk.Label(frame_estado, text="Tiempo Transcurrido:", **estilo_titulo_panel).pack(pady=5, padx=10)
        
        #estilo_valor_panel (Tiempo)
        self.lbl_tiempo_valor = tk.Label(frame_estado, text="N/A", **estilo_valor_panel)
        self.lbl_tiempo_valor.pack(pady=5, padx=10)
        
        #estilo_titulo_panel (Trenes Activos)
        tk.Label(frame_estado, text="Trenes Activos:", **estilo_titulo_panel).pack(pady=5, padx=10)
        
        #estilo_valor_panel (Trenes)
        self.lbl_trenes_valor = tk.Label(frame_estado, text="N/A", **estilo_valor_panel)
        self.lbl_trenes_valor.pack(pady=5, padx=10)

        # Panel del Mapa
        self.canvas_mapa = tk.Canvas(frame_display, bg=COLOR_PANEL, width=500, height=400, relief="sunken", borderwidth=1)
        self.canvas_mapa.pack(side="right", fill="both", expand=True, padx=10, pady=5)

    # --- Funciones de Botones ---

    def iniciar_nueva_simulacion(self):
        # 1. Crear la vista PRIMERO
        self.crear_vista_simulacion()
        # 2. Inicializar el estado DESPUÉS
        self.estado.inicializar_estado_base() # RF04

    def abrir_gestion_estaciones(self):
        ventana = VentanaEstaciones(self, self.estado)
        ventana.transient(self)
        ventana.grab_set()
        self.wait_window(ventana)

    def guardar_simulacion(self):
        archivo_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("Archivos de Simulación JSON", "*.json")],
            title="Guardar estado de simulación"
        )
        if not archivo_path:
            return
        
        if self.guardador.guardar_estado(self.estado, archivo_path):
            messagebox.showinfo("Guardado", "Simulación guardada exitosamente.")
        else:
            messagebox.showerror("Error", "No se pudo guardar la simulación.")

    def cargar_simulacion(self):
        archivo_path = filedialog.askopenfilename(
            filetypes=[("Archivos de Simulación JSON", "*.json")],
            title="Cargar estado de simulación"
        )
        if not archivo_path:
            return

        # 1. Crear la vista PRIMERO
        self.crear_vista_simulacion()
        
        # 2. Cargar el estado DESPUÉS
        if self.guardador.cargar_estado(self.estado, archivo_path):
            messagebox.showinfo("Carga Exitosa", "Simulación cargada correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo cargar la simulación.")
            # Si la carga falla, vuelve al menú
            self.crear_menu_principal()

    # --- Función de Actualización de GUI ---

    def actualizar_vista_simulacion(self):
        # Comprobación de seguridad: No hacer nada si la vista de simulación no está activa
        if not self.frame_simulacion or not hasattr(self, 'lbl_tiempo_valor'):
            print("Callback de actualización llamado, pero la vista de simulación no está lista. Omitiendo.")
            return
            
        if self.estado.tiempo_actual:
            self.lbl_tiempo_valor.config(text=self.estado.tiempo_actual.strftime("%Y-%m-%d %H:%M"))
        self.lbl_trenes_valor.config(text=f"{len(self.estado.trenes)}")
        
        # Actualizar el Mapa
        self.canvas_mapa.delete("all")
        self.canvas_mapa.create_text(250, 200, text="[Simulación de Mapa]", font=("Arial", 12), fill=COLOR_TEXTO)