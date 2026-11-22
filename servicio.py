from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def __init__(self, horas):
        super().__init__("Reserva de Sala")
        self.horas = horas

    def calcular_costo(self):
        return self.horas * 50000

    def descripcion(self):
        return f"Reserva de sala por {self.horas} horas"


class AlquilerEquipo(Servicio):

    def __init__(self, dias):
        super().__init__("Alquiler de Equipo")
        self.dias = dias

    def calcular_costo(self):
        return self.dias * 30000

    def descripcion(self):
        return f"Alquiler de equipo por {self.dias} dias"


class Asesoria(Servicio):

    def __init__(self, horas):
        super().__init__("Asesoria Especializada")
        self.horas = horas

    def calcular_costo(self):
        return self.horas * 80000

    def descripcion(self):
        return f"Asesoria especializada por {self.horas} horas"
