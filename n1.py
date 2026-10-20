productos = [
("Mouse", 25000, 10),
("Teclado", 60000, 3),
("Monitor", 450000, 5),
("Audifonos", 80000, 2),
("Cable HDMI", 15000, 20),
]

ventas = [("Mouse", 3), ("Monitor", 6), ("Teclado", 1), ("Parlante", 2),
("Mouse", 4)]

def crear_inventario(productos):
    inventario = {}
    for nombre, precio, stock in productos:
        inventario[nombre] = {"precio": precio, "stock": stock}
    return inventario

inventario = crear_inventario(productos)
print(inventario)