class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self.__modelo = modelo 

    def info_vehiculo(self):
        return f"Vehiculo: {self._marca} {self.__modelo}"


class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self._puertas = puertas

    def info_coche(self):
        info = f"Coche: {self._marca} | Puertas: {self._puertas}"

        try:
            info += f" | Modelo: {self.__modelo}"
        except AttributeError:
            info += " | (modelo privado: no accesible desde subclase)"

        return info

vehiculo = Vehiculo("Ford", "F150")
print(vehiculo.info_vehiculo())
print()

coche = Coche("Toyota", "Corolla", 4)

print(coche.info_vehiculo())

print(coche.info_coche())
print()

print(f"Marca (protegida): {coche._marca}")

try:
    print(coche.__modelo)
except AttributeError as e:
    print(f"Error acceso directo a __modelo: {e}")