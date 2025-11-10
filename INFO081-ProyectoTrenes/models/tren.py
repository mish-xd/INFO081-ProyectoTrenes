class Tren:
    def __init__(self, nombre: str, velocidad: int, vagones: list):
        """
        Crea un nuevo tren con sus datos iniciales.

        Args:
            nombre (str): nombre o identificador del tren.
            velocidad (int): velocidad máxima en km/h.
            vagones (list): lista con la capacidad de cada vagón.
        """
        self.nombre = nombre
        self.velocidad = velocidad
        self.vagones = vagones  # Ejemplo: [100, 80, 120]
        self.flujo_personas = 0
        self.estado = "En espera"  # Otros posibles: "En ruta", "En estación"

    # =====================
    # Métodos de gestión
    # =====================

    def capacidad_total(self) -> int:
        """Devuelve la capacidad total sumando todos los vagones."""
        return sum(self.vagones)

    def embarcar_pasajeros(self, cantidad: int):
        """
        Suma pasajeros al flujo si hay espacio disponible.
        
        Args:
            cantidad (int): número de pasajeros que suben.
        """
        capacidad_restante = self.capacidad_total() - self.flujo_personas
        if cantidad <= capacidad_restante:
            self.flujo_personas += cantidad
        else:
            self.flujo_personas = self.capacidad_total()

    def cambiar_estado(self, nuevo_estado: str):
        """
        Cambia el estado actual del tren.
        
        Args:
            nuevo_estado (str): nuevo estado del tren (por ejemplo, "En ruta").
        """
        self.estado = nuevo_estado

    def resumen(self) -> str:
        """Devuelve un texto con la información principal del tren."""
        return (f"Tren {self.nombre} | Velocidad: {self.velocidad} km/h | "
                f"Vagones: {len(self.vagones)} | Capacidad: {self.capacidad_total()} | "
                f"Flujo: {self.flujo_personas} | Estado: {self.estado}")
