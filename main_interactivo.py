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

    registrar_log(
        f"[EXITO] Cliente registrado: {cliente.nombre}"
    )

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

            registrar_log(
                f"[ERROR] {e}"
            )

            print("\nOpcion invalida.")
            print("Por favor intente nuevamente.")

    if opcion == 1:

        horas = int(input("Cantidad de horas: "))
        servicio = ReservaSala(horas)

    elif opcion == 2:

        dias = int(input("Cantidad de dias: "))
        servicio = AlquilerEquipo(dias)

    else:

        horas = int(input("Cantidad de horas: "))
        servicio = Asesoria(horas)

    registrar_log(
        f"[EXITO] Servicio seleccionado: {servicio.nombre}"
    )

    reserva = Reserva(cliente, servicio)

    reserva.confirmar()

    registrar_log(
        f"[EXITO] Reserva confirmada para {cliente.nombre}"
    )

    print("\n===== RESUMEN DE LA RESERVA =====")
    print(cliente.mostrar_datos())
    print(servicio.descripcion())
    print("Costo:", servicio.calcular_costo())
    print(reserva.mostrar_reserva())

except Exception as e:

    registrar_log(
        f"[ERROR] {e}"
    )

    print("\nError:", e)

finally:

    print("\nGracias por tu reserva")