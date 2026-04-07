# funcion.py - Funciones externas del supermercado

clientes = {}
productos = {
    "leche":      {"precio": 2500,  "stock": 50},
    "pan":        {"precio": 1800,  "stock": 80},
    "arroz":      {"precio": 3200,  "stock": 60},
    "huevos":     {"precio": 8000,  "stock": 30},
    "aceite":     {"precio": 9500,  "stock": 25},
    "azucar":     {"precio": 2800,  "stock": 45},
    "cafe":       {"precio": 12000, "stock": 20},
    "jabon":      {"precio": 3500,  "stock": 35},
    "papel":      {"precio": 4200,  "stock": 40},
    "shampoo":    {"precio": 11000, "stock": 15},
}


# ------------------------------------------
#  FUNCIONES DE CLIENTES
# ------------------------------------------

def registrar_cliente(cedula, nombre, apellido, telefono, correo):
    """Registra un nuevo cliente en el sistema."""
    if cedula in clientes:
        return f"ERROR: Ya existe un cliente con la cedula {cedula}."
    clientes[cedula] = {
        "nombre":    nombre,
        "apellido":  apellido,
        "telefono":  telefono,
        "correo":    correo,
        "compras":   [],
        "total_gastado": 0,
    }
    return f"OK: Cliente {nombre} {apellido} registrado correctamente."


def buscar_cliente(cedula):
    """Busca un cliente por cedula y muestra su informacion."""
    if cedula not in clientes:
        return f"ERROR: No se encontro ningun cliente con cedula {cedula}."
    c = clientes[cedula]
    info = (
        f"\n{'='*40}\n"
        f"  INFORMACION DEL CLIENTE\n"
        f"{'='*40}\n"
        f"  Cedula    : {cedula}\n"
        f"  Nombre    : {c['nombre']} {c['apellido']}\n"
        f"  Telefono  : {c['telefono']}\n"
        f"  Correo    : {c['correo']}\n"
        f"  Compras   : {len(c['compras'])}\n"
        f"  Total $   : ${c['total_gastado']:,.0f}\n"
        f"{'='*40}"
    )
    return info


def listar_clientes():
    """Lista todos los clientes registrados."""
    if not clientes:
        return "AVISO: No hay clientes registrados aun."
    lineas = [f"\n{'='*50}", "  LISTA DE CLIENTES REGISTRADOS", f"{'='*50}"]
    for cedula, c in clientes.items():
        lineas.append(
            f"  {cedula} | {c['nombre']} {c['apellido']} | "
            f"Tel: {c['telefono']} | Compras: {len(c['compras'])}"
        )
    lineas.append(f"{'='*50}")
    return "\n".join(lineas)


def eliminar_cliente(cedula):
    """Elimina un cliente del sistema."""
    if cedula not in clientes:
        return f"ERROR: No existe cliente con cedula {cedula}."
    nombre = f"{clientes[cedula]['nombre']} {clientes[cedula]['apellido']}"
    del clientes[cedula]
    return f"OK: Cliente {nombre} eliminado correctamente."


# ------------------------------------------
#  FUNCIONES DE PRODUCTOS
# ------------------------------------------

def mostrar_productos():
    """Muestra el catalogo de productos disponibles."""
    lineas = [f"\n{'='*50}", "  CATALOGO DE PRODUCTOS", f"{'='*50}",
              f"  {'Producto':<12} {'Precio':>10}  {'Stock':>6}"]
    lineas.append(f"  {'-'*44}")
    for nombre, datos in productos.items():
        lineas.append(
            f"  {nombre.capitalize():<12} ${datos['precio']:>9,.0f}  "
            f"{datos['stock']:>5} uds"
        )
    lineas.append(f"{'='*50}")
    return "\n".join(lineas)


def agregar_producto(nombre, precio, stock):
    """Agrega un producto nuevo al catalogo."""
    nombre = nombre.lower()
    if nombre in productos:
        return f"ERROR: El producto '{nombre}' ya existe."
    productos[nombre] = {"precio": precio, "stock": stock}
    return f"OK: Producto '{nombre.capitalize()}' agregado al catalogo."


# ------------------------------------------
#  FUNCIONES DE COMPRA
# ------------------------------------------

def realizar_compra(cedula, lista_productos):
    """
    Realiza una compra para un cliente.
    lista_productos: lista de tuplas (nombre_producto, cantidad)
    Retorna el recibo como string.
    """
    if cedula not in clientes:
        return f"ERROR: Cliente con cedula {cedula} no registrado."

    detalle = []
    total   = 0
    errores = []

    for prod, cantidad in lista_productos:
        prod = prod.lower()
        if prod not in productos:
            errores.append(f"  AVISO: Producto '{prod}' no existe.")
            continue
        if productos[prod]["stock"] < cantidad:
            errores.append(
                f"  AVISO: Stock insuficiente de '{prod}' "
                f"(disponible: {productos[prod]['stock']})."
            )
            continue
        subtotal = productos[prod]["precio"] * cantidad
        productos[prod]["stock"] -= cantidad
        detalle.append((prod.capitalize(), cantidad,
                        productos[prod]["precio"], subtotal))
        total += subtotal

    if not detalle:
        return "ERROR: No se proceso ningun producto.\n" + "\n".join(errores)

    c = clientes[cedula]
    c["compras"].append({"detalle": detalle, "total": total})
    c["total_gastado"] += total

    # Generar recibo
    lineas = [
        f"\n{'='*50}",
        f"  RECIBO DE COMPRA - SUPERMERCADO PYTHON",
        f"{'='*50}",
        f"  Cliente : {c['nombre']} {c['apellido']}",
        f"  Cedula  : {cedula}",
        f"  Compra N.: {len(c['compras'])}",
        f"  {'-'*46}",
        f"  {'Producto':<14}{'Cant':>5}{'Precio':>12}{'Subtotal':>12}",
        f"  {'-'*46}",
    ]
    for prod, cant, precio, sub in detalle:
        lineas.append(f"  {prod:<14}{cant:>5}${precio:>11,.0f}${sub:>11,.0f}")
    lineas += [
        f"  {'-'*46}",
        f"  {'TOTAL':>32}  ${total:>11,.0f}",
        f"{'='*50}",
    ]
    if errores:
        lineas.append("  Advertencias:")
        lineas.extend(errores)

    return "\n".join(lineas)


def historial_compras(cedula):
    """Muestra el historial de compras de un cliente."""
    if cedula not in clientes:
        return f"ERROR: Cliente con cedula {cedula} no encontrado."
    c = clientes[cedula]
    if not c["compras"]:
        return f"AVISO: El cliente {c['nombre']} no tiene compras registradas."

    lineas = [
        f"\n{'='*50}",
        f"  HISTORIAL DE COMPRAS - {c['nombre']} {c['apellido']}",
        f"{'='*50}",
    ]
    for i, compra in enumerate(c["compras"], 1):
        lineas.append(f"\n  Compra #{i}  -  Total: ${compra['total']:,.0f}")
        for prod, cant, precio, sub in compra["detalle"]:
            lineas.append(f"    - {prod} x{cant}  ->  ${sub:,.0f}")
    lineas += [
        f"\n  {'-'*46}",
        f"  Total acumulado gastado: ${c['total_gastado']:,.0f}",
        f"{'='*50}",
    ]
    return "\n".join(lineas)


def cliente_mas_fiel():
    """Retorna el cliente que mas ha gastado."""
    if not clientes:
        return "AVISO: No hay clientes registrados."
    top = max(clientes.items(), key=lambda x: x[1]["total_gastado"])
    cedula, c = top
    return (
        f"Cliente mas fiel: {c['nombre']} {c['apellido']} "
        f"(Cedula: {cedula}) - Total gastado: ${c['total_gastado']:,.0f}"
    )
