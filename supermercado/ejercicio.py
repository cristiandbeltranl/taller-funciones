# ejercicio.py - Programa principal del Supermercado Python
# Importa todas las funciones desde funcion.py

from funcion import (
    registrar_cliente,
    buscar_cliente,
    listar_clientes,
    eliminar_cliente,
    mostrar_productos,
    agregar_producto,
    realizar_compra,
    historial_compras,
    cliente_mas_fiel,
)


# ------------------------------------------
#  MENU PRINCIPAL
# ------------------------------------------

def menu_principal():
    opciones = """
+==========================================+
|     SUPERMERCADO                         |
+==========================================+
|  1. Registrar cliente                    |
|  2. Buscar cliente                       |
|  3. Listar todos los clientes            |
|  4. Eliminar cliente                     |
|------------------------------------------|
|  5. Ver catalogo de productos            |
|  6. Agregar producto                     |
|------------------------------------------|
|  7. Realizar compra                      |
|  8. Ver historial de compras             |
|  9. Cliente mas fiel                     |
|------------------------------------------|
|  0. Salir                                |
+==========================================+
"""
    print(opciones)
    return input("  Seleccione una opcion: ").strip()


# ------------------------------------------
#  FLUJOS POR OPCION
# ------------------------------------------

def flujo_registrar():
    print("\n-- REGISTRAR CLIENTE --")
    cedula    = input("  Cedula    : ").strip()
    nombre    = input("  Nombre    : ").strip().capitalize()
    apellido  = input("  Apellido  : ").strip().capitalize()
    telefono  = input("  Telefono  : ").strip()
    correo    = input("  Correo    : ").strip()
    print(registrar_cliente(cedula, nombre, apellido, telefono, correo))


def flujo_buscar():
    print("\n-- BUSCAR CLIENTE --")
    cedula = input("  Cedula del cliente: ").strip()
    print(buscar_cliente(cedula))


def flujo_eliminar():
    print("\n-- ELIMINAR CLIENTE --")
    cedula = input("  Cedula del cliente a eliminar: ").strip()
    confirmar = input(f"  Seguro que desea eliminar al cliente {cedula}? (s/n): ").strip().lower()
    if confirmar == "s":
        print(eliminar_cliente(cedula))
    else:
        print("  Operacion cancelada.")


def flujo_agregar_producto():
    print("\n-- AGREGAR PRODUCTO --")
    nombre = input("  Nombre del producto: ").strip()
    try:
        precio = float(input("  Precio ($): ").strip())
        stock  = int(input("  Stock inicial (uds): ").strip())
        print(agregar_producto(nombre, precio, stock))
    except ValueError:
        print("  ERROR: Precio o stock invalido.")


def flujo_compra():
    print("\n-- REALIZAR COMPRA --")
    cedula = input("  Cedula del cliente: ").strip()
    print(mostrar_productos())

    carrito = []
    print("  Ingrese los productos (escriba 'listo' para terminar):")
    while True:
        prod = input("    Producto: ").strip().lower()
        if prod == "listo":
            break
        try:
            cant = int(input("    Cantidad: ").strip())
            carrito.append((prod, cant))
        except ValueError:
            print("    AVISO: Cantidad invalida, intente de nuevo.")

    if carrito:
        print(realizar_compra(cedula, carrito))
    else:
        print("  AVISO: Carrito vacio, compra cancelada.")


def flujo_historial():
    print("\n-- HISTORIAL DE COMPRAS --")
    cedula = input("  Cedula del cliente: ").strip()
    print(historial_compras(cedula))


# ------------------------------------------
#  CARGA DE DATOS DE EJEMPLO
# ------------------------------------------

def cargar_datos_ejemplo():
    """Carga clientes y compras de ejemplo para demostracion."""
    registrar_cliente("1020304050", "Carlos",    "Ramirez",  "3101234567", "carlos.ramirez@mail.com")
    registrar_cliente("987654321",  "Maria",     "Gonzalez", "3209876543", "maria.gonzalez@mail.com")
    registrar_cliente("112233445",  "Andres",    "Perez",    "3154567890", "andres.perez@mail.com")
    registrar_cliente("556677889",  "Valentina", "Torres",   "3006543210", "vale.torres@mail.com")
    registrar_cliente("998877665",  "Luis",      "Morales",  "3187654321", "luis.morales@mail.com")

    realizar_compra("1020304050", [("leche", 3), ("pan", 2), ("cafe", 1)])
    realizar_compra("987654321",  [("arroz", 5), ("aceite", 2), ("azucar", 3)])
    realizar_compra("112233445",  [("huevos", 2), ("jabon", 4)])
    realizar_compra("1020304050", [("shampoo", 1), ("papel", 2), ("leche", 2)])
    realizar_compra("556677889",  [("cafe", 2), ("pan", 5), ("aceite", 1)])

    print("  Datos de ejemplo cargados correctamente.\n")


# ------------------------------------------
#  PROGRAMA PRINCIPAL
# ------------------------------------------

def main():
    print("\n  Cargando datos de ejemplo...")
    cargar_datos_ejemplo()

    while True:
        opcion = menu_principal()

        if   opcion == "1": flujo_registrar()
        elif opcion == "2": flujo_buscar()
        elif opcion == "3": print(listar_clientes())
        elif opcion == "4": flujo_eliminar()
        elif opcion == "5": print(mostrar_productos())
        elif opcion == "6": flujo_agregar_producto()
        elif opcion == "7": flujo_compra()
        elif opcion == "8": flujo_historial()
        elif opcion == "9": print("\n" + cliente_mas_fiel())
        elif opcion == "0":
            print("\n  Hasta pronto. Gracias por usar Supermercado Python.\n")
            break
        else:
            print("  AVISO: Opcion invalida. Intente de nuevo.")

        input("\n  Presione Enter para continuar...")


if __name__ == "__main__":
    main()
