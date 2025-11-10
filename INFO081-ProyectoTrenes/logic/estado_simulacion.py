# logic/estado_simulacion.py
from datetime import datetime

# --- Clases Modelo (Necesarias para el estado y guardado) ---
class Estacion:
    def __init__(self, id_estacion, nombre, poblacion):
        self.id_estacion = id_estacion
        self.nombre = nombre
        self.poblacion = poblacion
        # Faltan atributos: Vías, flujo acumulado

    def to_dict(self):
        return {
            "id_estacion": self.id_estacion,
            "nombre": self.nombre,
            "poblacion": self.poblacion
        }

    @staticmethod
    def from_dict(data):
        return Estacion(
            data["id_estacion"],
            data["nombre"],
            data["poblacion"]
        )

class Tren:
    def __init__(self, id_tren, nombre, velocidad):
        self.id_tren = id_tren
        self.nombre = nombre
        self.velocidad = velocidad
    def to_dict(self): return {"id_tren": self.id_tren, "nombre": self.nombre, "velocidad": self.velocidad}
    @staticmethod
    def from_dict(data): return Tren(data["id_tren"], data["nombre"], data["velocidad"])
    
class Ruta: pass
class Persona: pass

# --- Clase Principal del Estado ---

class EstadoDeSimulacion:
    
    def __init__(self):
        self.tiempo_actual = None
        self.estaciones = []
        self.trenes = []
        self.rutas = []
        self.personas_activas = []
        self.personas_historial = []
        
        self.update_callback = None

    def set_update_callback(self, callback_func):
        self.update_callback = callback_func

    def inicializar_estado_base(self):
        print("Inicializando estado base...")
        self.tiempo_actual = datetime(2015, 3, 1, 7, 0, 0)
        
        self.estaciones = [
            Estacion(id_estacion="E01", nombre="Central", poblacion=100000),
            Estacion(id_estacion="E02", nombre="Norte", poblacion=50000),
            Estacion(id_estacion="E03", nombre="Sur", poblacion=75000)
        ]
        self.trenes = [
            Tren(id_tren="T01", nombre="Tren A", velocidad=80)
        ]
        
        print(f"Estado base cargado. Tiempo: {self.tiempo_actual}")
        if self.update_callback:
            self.update_callback()

    def avanzar_al_siguiente_evento(self):
        print("Avanzando al siguiente evento...")
        
        # --- Lógica de simulación  ---
        # Por ahora, solo avanzamos el tiempo 1 hora
        if self.tiempo_actual:
            from datetime import timedelta
            self.tiempo_actual += timedelta(hours=1)
        
        print(f"Evento procesado. Nuevo tiempo: {self.tiempo_actual}")
        
        if self.update_callback:
            self.update_callback()

    def procesar_evento(self, evento):
        pass

    #Métodos de gestion de estaciones
    def agregar_estacion(self, nombre, poblacion):
        nuevo_id = f"E{len(self.estaciones) + 1:02d}"
        nueva_estacion = Estacion(nuevo_id, nombre, poblacion)
        self.estaciones.append(nueva_estacion)
        print(f"Estación agregada: {nombre}")
        return nueva_estacion

    def eliminar_estacion(self, id_estacion):
        estacion = next((e for e in self.estaciones if e.id_estacion == id_estacion), None)
        if estacion:
            self.estaciones.remove(estacion)
            print(f"Estación eliminada: {estacion.nombre}")
            return True
        return False
        
    def get_estado_serializable(self):
        return {
            "tiempo_actual": self.tiempo_actual.isoformat() if self.tiempo_actual else None,
            "estaciones": [e.to_dict() for e in self.estaciones],
            "trenes": [t.to_dict() for t in self.trenes],
        }

    def restaurar_estado_desde_datos(self, data):
        self.tiempo_actual = datetime.fromisoformat(data["tiempo_actual"]) if data["tiempo_actual"] else None
        self.estaciones = [Estacion.from_dict(e_data) for e_data in data["estaciones"]]
        self.trenes = [Tren.from_dict(t_data) for t_data in data["trenes"]]
        print("Estado restaurado desde datos.")
        if self.update_callback:
            self.update_callback()