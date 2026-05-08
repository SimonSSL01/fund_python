class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Representacion amigable para el usuario."""
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """Representacion detallada para desarrolladores."""
        return f"Punto({self.x}, {self.y})"

    def __add__(self, otro):
        """Soporte para el operador +"""
        return Punto(self.x + otro.x, self.y + otro.y)

    def __eq__(self, otro):
        """Soporte para el operador =="""
        if not isinstance(otro, Punto):
            return False
        return self.x == otro.x and self.y == otro.y

    def __len__(self):
        """Distancia Manhattan desde el origen."""
        return abs(self.x) + abs(self.y)

p1 = Punto(3, 4)
p2 = Punto(1, 2)
p3 = Punto(3, 4)

print(f"p1 = {p1}")
print(f"repr: {repr(p1)}") 
print()

p4 = p1 + p2
print(f"p1 + p2 = {p4}")
print()

print(f"p1 == p2: {p1 == p2}")
print(f"p1 == p3: {p1 == p3}")
print()

print(f"len(p1) = {len(p1)}") 
print(f"len(p2) = {len(p2)}")