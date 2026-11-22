from cliente import Cliente
from servicio import ReservaSala
from servicio import AlquilerEquipo
from servicio import Asesoria
from reserva import Reserva
from logger import registrar_log
from excepciones import ReservaError


print("=== SISTEMA SOFTWARE FJ ===")


# OPERACION 1
try:
    cliente1 = Cliente("Juan Perez", "juan@gmail.com")
    print(cliente1.mostrar_datos())
except Exception as e:
    registrar_log(e)

# OPERACION 2
try:
    cliente2 = Cliente("Maria Gomez", "maria@gmail.com")
    print(cliente2.mostrar_datos())
except Exception as e:
    registrar_log(e)

# OPERACION 3
try:
    cliente3 = Cliente("Carlos Ruiz", "correo_invalido")
    print(cliente3.mostrar_datos())
except Exception as e:
    registrar_log(e)
    print("Error controlado:", e)


# OPERACION 4
sala = ReservaSala(2)
print(sala.descripcion())
print("Costo:", sala.calcular_costo())

# OPERACION 5
equipo = AlquilerEquipo(3)
print(equipo.descripcion())
print("Costo:", equipo.calcular_costo())

# OPERACION 6
asesoria = Asesoria(1)
print(asesoria.descripcion())
print("Costo:", asesoria.calcular_costo())


# OPERACION 7
try:
    reserva1 = Reserva(cliente1, sala)
    reserva1.confirmar()
    print(reserva1.mostrar_reserva())
except Exception as e:
    registrar_log(e)

# OPERACION 8
try:
    reserva2 = Reserva(cliente2, equipo)
    reserva2.confirmar()
    print(reserva2.mostrar_reserva())
except Exception as e:
    registrar_log(e)

# OPERACION 9
try:
    reserva3 = Reserva(None, asesoria)
except ReservaError as e:
    registrar_log(e)
    print("Error controlado:", e)

# OPERACION 10

try:

    numero = int("123")

except ValueError as e:

    registrar_log(e)

    print("Error:", e)

else:

    print("Conversion realizada correctamente")

finally:

    print("Finalizacion del sistema")
