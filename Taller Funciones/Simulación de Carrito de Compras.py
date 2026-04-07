class ShoppingCart:
    def __init__(self):
        self.items = {} # {nombre_producto: {'price': precio, 'quantity': cantidad}}
        self.discount_percentage = 0

    def add_product(self, product_name, price, quantity=1):
        """
        Agrega un producto al carrito o actualiza su cantidad si ya existe.
        """
        if price <= 0 or quantity <= 0:
            print("El precio y la cantidad deben ser valores positivos.")
            return

        if product_name in self.items:
            self.items[product_name]['quantity'] += quantity
        else:
            self.items[product_name] = {'price': price, 'quantity': quantity}
        print(f"Se añadió/actualizó '{quantity}' unidades de '{product_name}' al carrito.")

    def remove_product(self, product_name, quantity=None):
        """
        Elimina un producto del carrito o reduce su cantidad.
        Si `quantity` es None, elimina todas las unidades del producto.
        """
        if product_name not in self.items:
            print(f"'{product_name}' no está en el carrito.")
            return

        if quantity is None or quantity >= self.items[product_name]['quantity']:
            del self.items[product_name]
            print(f"Todas las unidades de '{product_name}' eliminadas del carrito.")
        elif quantity > 0:
            self.items[product_name]['quantity'] -= quantity
            print(f"Se eliminaron '{quantity}' unidades de '{product_name}'. Cantidad restante: {self.items[product_name]['quantity']}")
        else:
            print("La cantidad a eliminar debe ser un número positivo.")

    def apply_discount(self, percentage):
        """
        Aplica un porcentaje de descuento al total final del carrito.
        """
        if 0 <= percentage <= 100:
            self.discount_percentage = percentage
            print(f"Descuento del {percentage}% aplicado.")
        else:
            print("El porcentaje de descuento debe estar entre 0 y 100.")

    def calculate_subtotal(self):
        """
        Calcula el total sin descuentos.
        """
        subtotal = 0
        for product_name, details in self.items.items():
            subtotal += details['price'] * details['quantity']
        return subtotal

    def generate_total(self):
        """
        Calcula el total a pagar después de aplicar descuentos.
        """
        subtotal = self.calculate_subtotal()
        discount_amount = subtotal * (self.discount_percentage / 100)
        total_to_pay = subtotal - discount_amount
        return subtotal, discount_amount, total_to_pay

    def display_cart(self):
        """
        Muestra los productos en el carrito y el resumen del pedido.
        """
        if not self.items:
            print("\nEl carrito de compras está vacío.")
            return

        print("\n--- Tu Carrito de Compras ---")
        for product_name, details in self.items.items():
            print(f"  - {product_name}: {details['quantity']} x ${details['price']:.2f} = ${details['quantity'] * details['price']:.2f}")
        print("-----------------------------")
        
        subtotal, discount_amount, total_to_pay = self.generate_total()
        print(f"Subtotal: ${subtotal:.2f}")
        if self.discount_percentage > 0:
            print(f"Descuento ({self.discount_percentage}%): -${discount_amount:.2f}")
        print(f"Total a Pagar: ${total_to_pay:.2f}")
        print("-----------------------------")

# Demostración
my_cart = ShoppingCart()

my_cart.add_product("Camiseta", 25.00, 2)
my_cart.add_product("Pantalón", 50.00, 1)
my_cart.add_product("Zapatillas", 75.00)
my_cart.add_product("Camiseta", 25.00, 1) # Añadir más camisetas

my_cart.display_cart()

my_cart.apply_discount(10)
my_cart.display_cart()

my_cart.remove_product("Pantalón")
my_cart.remove_product("Zapatillas", 0) # Intento de eliminar cantidad inválida
my_cart.remove_product("Zapatillas", 1) # Eliminar 1 zapatilla
my_cart.remove_product("Zapatillas") # Eliminar las restantes

my_cart.display_cart()

my_cart.add_product("Gorra", 15.00, 3)
my_cart.apply_discount(20)
my_cart.display_cart()
