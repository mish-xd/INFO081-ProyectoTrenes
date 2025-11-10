# logic/sistema_guardado.py
import json
# Importa la clase desde el mismo directorio 'logic'
from logic.estado_simulacion import EstadoDeSimulacion

class SistemaGuardado:

    def guardar_estado(self, estado: EstadoDeSimulacion, nombre_archivo: str):
        print(f"Guardando estado en {nombre_archivo}...")
        try:
            datos_a_guardar = estado.get_estado_serializable()
            
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                json.dump(datos_a_guardar, f, indent=4, ensure_ascii=False)
            
            print("Guardado exitoso.")
            return True
        except Exception as e:
            print(f"Error al guardar: {e}")
            return False

    def cargar_estado(self, estado: EstadoDeSimulacion, nombre_archivo: str):
        print(f"Cargando estado desde {nombre_archivo}...")
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as f:
                datos_cargados = json.load(f)
            
            estado.restaurar_estado_desde_datos(datos_cargados)
            
            print("Carga exitosa.")
            return True
        except Exception as e:
            print(f"Error al cargar: {e}")
            return False