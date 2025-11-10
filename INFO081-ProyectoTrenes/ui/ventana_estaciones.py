# ui/ventana_estaciones.py
import tkinter as tk
from tkinter import ttk, messagebox
from logic.estado_simulacion import EstadoDeSimulacion

# Importar tus configuraciones
from config.colores import (
    COLOR_FONDO, COLOR_TEXTO, COLOR_BOTON, COLOR_TEXTO_BOTON,
    COLOR_BOTON_HOVER, COLOR_PANEL
)

class VentanaEstaciones(tk.Toplevel):
    
    def __init__(self, master, estado: EstadoDeSimulacion):
        super().__init__(master)
        self.title("Gestión de Estaciones")
        self.geometry("600x500")
        self.config(bg=COLOR_FONDO)
        self.resizable(False, False)
        
        self.estado = estado
        
        # Estilos para el Treeview
        style = ttk.Style(self)
        style.theme_use("default")
        
        # Estilo general del Treeview
        style.configure("Treeview",
                        background=COLOR_PANEL,
                        foreground=COLOR_TEXTO,
                        fieldbackground=COLOR_PANEL,
                        bordercolor=COLOR_BOTON,
                        borderwidth=1,
                        rowheight=25)
        style.map('Treeview', background=[('selected', COLOR_BOTON_HOVER)], foreground=[('selected', COLOR_TEXTO_BOTON)])

        # Estilo de la cabecera
        style.configure("Treeview.Heading",
                        background=COLOR_BOTON,
                        foreground=COLOR_TEXTO_BOTON,
                        font=("Segoe UI", 10, "bold"),
                        padding=5)
        style.map("Treeview.Heading",
                  background=[('active', COLOR_BOTON_HOVER)])
        
        # Quitar bordes feos
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        self.crear_widgets()
        self.cargar_estaciones()

    def crear_widgets(self):
        # Frame para la lista de estaciones
        frame_lista = tk.Frame(self, bg=COLOR_FONDO)
        frame_lista.pack(pady=10, padx=10, fill="x")
        
        # Definición del Treeview
        self.tree = ttk.Treeview(frame_lista, columns=("ID", "Nombre", "Poblacion"), show="headings", height=8)
        self.tree.heading("ID", text="ID")
        self.tree.column("ID", width=50, anchor="center")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Poblacion", text="Población")
        self.tree.column("Poblacion", anchor="center")
        self.tree.pack(side="left", fill="x", expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Frame para el formulario
        frame_form = tk.LabelFrame(self, text="Formulario de Estación", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=("Segoe UI", 10))
        frame_form.pack(pady=10, padx=10, fill="x")

        tk.Label(frame_form, text="Nombre:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_nombre = tk.Entry(frame_form, bg=COLOR_PANEL, fg=COLOR_TEXTO, insertbackground=COLOR_TEXTO, font=("Segoe UI", 10))
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        tk.Label(frame_form, text="Población:", bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_poblacion = tk.Entry(frame_form, bg=COLOR_PANEL, fg=COLOR_TEXTO, insertbackground=COLOR_TEXTO, font=("Segoe UI", 10))
        self.entry_poblacion.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        frame_form.columnconfigure(1, weight=1)

        # Frame para botones de acción
        frame_botones_form = tk.Frame(self, bg=COLOR_FONDO)
        frame_botones_form.pack(pady=5, padx=10, fill="x")
        
        boton_style = {
            "bg": COLOR_BOTON, "fg": COLOR_TEXTO_BOTON, "font": ("Segoe UI", 10, "bold"),
            "activebackground": COLOR_BOTON_HOVER, "activeforeground": COLOR_TEXTO_BOTON, "relief": "flat", "width": 20
        }

        self.btn_guardar = tk.Button(frame_botones_form, text="Guardar/Agregar", command=self.guardar_estacion, **boton_style)
        self.btn_guardar.pack(side="left", padx=5)

        self.btn_eliminar = tk.Button(frame_botones_form, text="Eliminar Seleccionada", command=self.eliminar_estacion, **boton_style)
        self.btn_eliminar.pack(side="left", padx=5)
        
        # Botón para cerrar
        btn_volver = tk.Button(self, text="Volver", command=self.destroy, **boton_style)
        btn_volver.pack(pady=10)

    def cargar_estaciones(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for estacion in self.estado.estaciones:
            self.tree.insert("", "end", values=(estacion.id_estacion, estacion.nombre, estacion.poblacion))

    def guardar_estacion(self):
        nombre = self.entry_nombre.get()
        poblacion_str = self.entry_poblacion.get()
        
        if not nombre or not poblacion_str:
            messagebox.showerror("Error", "Debe completar todos los campos.")
            return
            
        try:
            poblacion = int(poblacion_str)
        except ValueError:
            messagebox.showerror("Error", "La población debe ser un número entero.")
            return

        self.estado.agregar_estacion(nombre, poblacion)
        self.cargar_estaciones()
        self.entry_nombre.delete(0, "end")
        self.entry_poblacion.delete(0, "end")

    def eliminar_estacion(self):
        seleccion = self.tree.focus()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Debe seleccionar una estación para eliminar.")
            return

        item_data = self.tree.item(seleccion)
        id_estacion = item_data['values'][0]
        nombre_estacion = item_data['values'][1]
        
        if messagebox.askyesno("Confirmar", f"¿Está seguro que desea eliminar la estación '{nombre_estacion}'?"):
            if self.estado.eliminar_estacion(id_estacion):
                self.cargar_estaciones()
            else:
                messagebox.showerror("Error", "No se pudo eliminar la estación.")