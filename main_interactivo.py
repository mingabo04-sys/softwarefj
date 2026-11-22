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

    print("\nServicios disponibles:")
    print("1. Reserva de sala")
    print("2. Alquiler de equipo")
    print("3. Asesoria especializada")

    opcion = int(input("\nSeleccione un servicio: "))

    if opcion == 1:

        horas = int(input("Cantidad de horas: "))
        servicio = ReservaSala(horas)

    elif opcion == 2:

        dias = int(input("Cantidad de dias: "))
        servicio = AlquilerEquipo(dias)

    elif opcion == 3:

        horas = int(input("Cantidad de horas: "))
        servicio = Asesoria(horas)

    else:
        raise ValueError("Opcion no valida")

    reserva = Reserva(cliente, servicio)

    reserva.confirmar()

    print("\n===== RESUMEN DE LA RESERVA =====")
    print(cliente.mostrar_datos())
    print(servicio.descripcion())
    print("Costo:", servicio.calcular_costo())
    print(reserva.mostrar_reserva())

except Exception as e:

    registrar_log(e)

    print("Error:", e)

finally:

    print("\nGracias por usar Software FJ")
