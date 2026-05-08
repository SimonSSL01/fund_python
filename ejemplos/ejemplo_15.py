class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacia")

    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and 0 <= nueva_edad <= 120:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un entero entre 0 y 120")

    def __str__(self):
        return f"{self._nombre} | Edad: {self._edad}"

simon = Persona("Simon Sierra", 29)

print(simon.get_nombre())
print(simon.get_edad())
print(simon)

simon.set_nombre("Simon Mendoza")
simon.set_edad(30)
print(simon)

try:
    simon.set_edad(-5)
except ValueError as e:
    print(f"Error: {e}")

try:
    simon.set_edad(200)
except ValueError as e:
    print(f"Error: {e}")

try:
    simon.set_nombre("")
except ValueError as e:
    print(f"Error: {e}")