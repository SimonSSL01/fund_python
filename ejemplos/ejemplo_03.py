class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def esta_disponible(self):
        return self.stock > 0

    def vender(self, cantidad):
        if cantidad > self.stock:
            return f"No hay suficiente stock de {self.nombre}."
        self.stock -= cantidad
        return f"Venta exitosa: {cantidad} unidad(es) de {self.nombre}. Stock restante: {self.stock}"

    def reabastecer(self, cantidad):
        self.stock += cantidad
        return f"Stock de {self.nombre} actualizado: {self.stock} unidades."

    def __str__(self):
        disponible = "Disponible" if self.esta_disponible() else "Agotado"
        return f"{self.nombre} | Precio: ${self.precio} | Stock: {self.stock} | {disponible}"

laptop = Producto("Laptop XPS", 1200)  
teclado = Producto("Teclado mecanico", 80, 15)

print(laptop)
print(teclado)
print()
print(laptop.esta_disponible())
print(teclado.esta_disponible())
print()
print(teclado.vender(3))
print(teclado.vender(20)) 
print(laptop.reabastecer(5))
print(laptop)