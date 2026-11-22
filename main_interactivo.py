from cliente import Cliente
from servicio import ReservaSala
from servicio import AlquilerEquipo
from servicio import Asesoria
from reserva import Reserva
from logger import registrar_log

print("===================================")
print(" SOFTWARE FJ - SISTEMA DE RESERVAS ")
print("===================================")

try:

    nombre = input("Ingrese el nombre del cliente: ")
    correo = input("Ingrese el correo del cliente: ")

    cliente = Cliente(nombre, correo)

print("\nSeleccione su servicio")
print("-----------------------")

while True:

    try:

        print("\nServicios disponibles:")
        print("1. Reserva de sala")
        print("2. Alquiler de equipo")
        print("3. Asesoria especializada")

        opcion = int(
            input("\nDigite el numero del servicio: ")
        )

        if opcion in [1, 2, 3]:
            break

        raise ValueError(
            "Debe seleccionar 1, 2 o 3"
        )

    except ValueError as e:

        registrar_log(e)

        print("\nOpcion invalida.")
        print("Por favor intente nuevamente.")
