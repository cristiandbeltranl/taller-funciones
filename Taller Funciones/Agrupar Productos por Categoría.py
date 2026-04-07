from collections import defaultdict

def group_products_by_category(products_categories):
    """
    Dado un listado de tuplas (producto, categoría), agrupa los productos por categoría
    usando un diccionario donde las claves son las categorías y los valores son listas de productos.
    """
    grouped_products = defaultdict(list)
    for product, category in products_categories:
        grouped_products[category].append(product)
    return dict(grouped_products) # Convertir defaultdict a dict normal para la salida

# Demostración
product_list = [
    ("Leche", "Lácteos"),
    ("Queso", "Lácteos"),
    ("Manzanas", "Frutas"),
    ("Plátanos", "Frutas"),
    ("Pan", "Panadería"),
    ("Yogur", "Lácteos"),
    ("Galletas", "Panadería")
]

grouped = group_products_by_category(product_list)

print(f"Lista de productos y categorías: {product_list}")
print("\nProductos agrupados por categoría:")
for category, products in grouped.items():
    print(f"  {category}: {', '.join(products)}")
