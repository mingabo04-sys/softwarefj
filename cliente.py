from persona import Persona

class Cliente(Persona):

    def __init__(self, nombre, correo):

        super().__init__(nombre)

        if "@" not in correo:
            raise ValueError("Correo invalido")

        self.__correo = correo

    def get_correo(self):
        return self.__correo

    def mostrar_datos(self):
        return f"Cliente: {self.nombre}, Correo: {self.__correo}"
