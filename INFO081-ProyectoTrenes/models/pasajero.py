class Pasajero:
    def __init__(self, nombre: str, origen: str, destino: str):
        """
        Crea un nuevo pasajero.
        :param nombre: nombre o identificador del pasajero
        :param origen: estación de origen
        :param destino: estación de destino
        """
        self.nombre = nombre
        self.origen = origen
        self.destino = destino
        self.estado = "Esperando"

    # Métodos de gestión

    def iniciar_viaje(self):
        """Cambia el estado del pasajero a 'Viajando'."""
        self.estado = "Viajando"

    def finalizar_viaje(self):
        """Cambia el estado del pasajero a 'Llegó'."""
        self.estado = "Llegó"

    def resumen(self):
        """Devuelve un texto con la información básica del pasajero."""
        return (f"Pasajero {self.nombre} | "
                f"Origen: {self.origen} | "
                f"Destino: {self.destino} | "
                f"Estado: {self.estado}")