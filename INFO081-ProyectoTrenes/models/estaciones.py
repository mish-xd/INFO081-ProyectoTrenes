class Estacion:
    def __init__(self, nombre: str, poblacion_total: int, vias: list):
        self.nombre = nombre
        self.poblacion_total = poblacion_total
        self.vias = vias  # por ejemplo: ["Norte", "Sur"]
        self.flujo_personas = 0
        self.personas_en_espera = []
        self.personas_llegadas = []

    # =====================
    # Métodos de gestión
    # =====================

    def agregar_pasajero(self, pasajero):
        """Agrega un pasajero a la estación (entra al área de espera)."""
        self.personas_en_espera.append(pasajero)

    def remover_pasajero(self, pasajero):
        """Elimina un pasajero cuando aborda un tren."""
        if pasajero in self.personas_en_espera:
            self.personas_en_espera.remove(pasajero)

    def registrar_llegada(self, pasajero):
        """Registra cuando un pasajero llega a su destino."""
        self.personas_llegadas.append(pasajero)
        self.flujo_personas += 1

    def resumen(self):
        """Devuelve un texto con la información básica de la estación."""
        return (f"Estación {self.nombre} | "
                f"Población: {self.poblacion_total} | "
                f"Vías: {len(self.vias)} | "
                f"Flujo: {self.flujo_personas}")