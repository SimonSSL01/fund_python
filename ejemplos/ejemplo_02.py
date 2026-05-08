class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def presentarse(self):
        estado = "mayor" if self.es_mayor_de_edad() else "menor"
        return f"Hola, soy {self.nombre_completo()} y soy {estado} de edad."

persona1 = Persona("Simon", "Sierra", 18)
persona2 = Persona("Juan", "Gomez", 15)
persona3 = Persona("Mariana", "Garcia", 28)

print(persona1.nombre_completo())
print(persona1.es_mayor_de_edad())
print(persona1.presentarse())
print()
print(persona2.presentarse())
print()
print(persona3.nombre_completo())
print(persona3.presentarse())