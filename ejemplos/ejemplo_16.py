class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Getter: obtiene la temperatura en Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        """Setter: establece Celsius con validacion."""
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        """Getter: calcula y devuelve Fahrenheit."""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        """Setter: permite asignar desde Fahrenheit."""
        celsius = (valor - 32) * 5/9
        if celsius < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = celsius

temp = Temperatura()

temp.celsius = 25
print(f"Temperatura: {temp.celsius}C = {temp.fahrenheit}F")

temp.celsius = 30
print(f"Temperatura: {temp.celsius}C = {temp.fahrenheit}F")

temp.fahrenheit = 68
print(f"68F equivale a {temp.celsius}C")

temp.celsius = 37
print(f"Cuerpo humano: {temp.celsius}C = {temp.fahrenheit}F")

try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")