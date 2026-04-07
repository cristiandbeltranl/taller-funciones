class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price, quantity):
        """
        Agrega o actualiza un producto en el inventario.
        """
        if price <= 0 or quantity < 0:
            print("El precio debe ser positivo y la cantidad no puede ser negativa.")
            return
        self.products[name] = {'price': price, 'quantity': quantity}
        print(f"Producto '{name}' agregado/actualizado. Precio: {price}, Cantidad: {quantity}")

    def calculate_total_inventory_value(self):
        """
        Calcula el valor total del inventario.
        """
        total_value = 0
        for product_name, details in self.products.items():
            total_value += details['price'] * details['quantity']
        return total_value

    def list_products(self):
        """
        Muestra todos los productos en el inventario.
        """
        if not self.products:
            print("El inventario está vacío.")
            return
        print("\n--- Inventario Actual ---")
        for name, details in self.products.items():
            print(f"Producto: {name}, Precio: ${details['price']:.2f}, Cantidad: {details['quantity']}")
        print("-------------------------")

# Demostración
inventory = Inventory()
inventory.add_product("Laptop", 1200.50, 5)
inventory.add_product("Mouse", 25.00, 20)
inventory.add_product("Teclado", 75.99, 10)

inventory.list_products()

total_value = inventory.calculate_total_inventory_value()
print(f"\nValor total del inventario: ${total_value:.2f}")

inventory.add_product("Laptop", 1150.00, 3) # Actualizar cantidad y precio
inventory.list_products()
print(f"Nuevo valor total del inventario: ${inventory.calculate_total_inventory_value():.2f}")
