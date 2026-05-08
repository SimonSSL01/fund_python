class Libro:
    def __init__(self, titulo, autor, paginas):
        """
        Constructor de la clase Libro
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"El libro '{self.titulo}' ha sido prestado con éxito."
        else:
            return f"Lo sentimos, el libro '{self.titulo}' no está disponible por ahora."

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return f"El libro '{self.titulo}' ha sido devuelto correctamente."
        else:
            return f"El libro '{self.titulo}' ya estaba en la biblioteca."

    def informacion(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return (f"Título: {self.titulo}\n"
                f"Autor: {self.autor}\n"
                f"Páginas: {self.paginas}\n"
                f"Estado: {estado}")

def main():
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)
    
    print("=== Información inicial de los libros ===")
    print(libro1.informacion())
    print("-" * 30)
    print(libro2.informacion())
    print("\n")
    
    print("=== Préstamo de libros ===")
    print(libro1.prestar())
    print(libro2.prestar())
    print("\n")
    
    print("=== Intento de préstamo de libros ya prestados ===")
    print(libro1.prestar())
    print("\n")

    print("=== Información después del préstamo ===")
    print(libro1.informacion())
    print("\n")
    
    print("=== Devolución de libros ===")
    print(libro1.devolver())
    print("\n")
    
    print("=== Intento de devolución de libros ya disponibles ===")
    print(libro1.devolver())
    print("\n")
    
    print("=== Información final de los libros ===")
    print(libro1.informacion())
    print("-" * 30)
    print(libro2.informacion())


if __name__ == "__main__":
    main()