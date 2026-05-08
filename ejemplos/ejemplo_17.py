import math

class Circulo:
    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError("El radio debe ser positivo")
        self._radio = valor

    @property
    def area(self):
        """Propiedad de solo lectura: calculada a partir del radio."""
        return round(math.pi * self._radio ** 2, 2)

    @property
    def perimetro(self):
        """Propiedad de solo lectura: calculada a partir del radio."""
        return round(2 * math.pi * self._radio, 2)

    def __str__(self):
        return f"Circulo r={self._radio} | Area={self.area} | Perimetro={self.perimetro}"

c = Circulo(5)
print(c)
print(f"Radio: {c.radio}")
print(f"Area: {c.area}")
print(f"Perimetro: {c.perimetro}")
print()

c.radio = 10
print(f"Nuevo radio: {c.radio}")
print(c)
print()

try:
    c.area = 100
except AttributeError as e:
    print(f"Error: no se puede modificar area directamente.")

try:
    c.radio = -3
except ValueError as e:
    print(f"Error: {e}")