class Estudiante:
    universidad = "SENA"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.activo = True

    def presentarse(self):
        estado = "activo" if self.activo else "inactivo"
        return f"{self.nombre} ({self.edad} anos) - {self.universidad} - {estado}"

    def desactivar(self):
        self.activo = False
        return f"{self.nombre} ha sido desactivado."
 
est1 = Estudiante("Simon Sierra", 18)
est2 = Estudiante("Carlos Navia", 22)
est3 = Estudiante("Andres Jaramillo", 20)

print(est1.universidad)
print(est2.universidad)
print(Estudiante.universidad)   
print()

print(est1.presentarse())
print(est2.presentarse())
print(est3.presentarse())
print()

Estudiante.universidad = "SENA Regional Medellin"
print(est1.universidad)
print(est2.universidad)
print()

print(est3.desactivar())
print(est3.presentarse())
print(est1.presentarse())