import datetime

inventario = {
    "Laptop Asus": {"disponible": True, "prestamos": []},
    "Tablet Samsung": {"disponible": True, "prestamos": []}
}

def mostrar_equipos():
    print("\n--- Estado del Inventario ---")
    for nombre, info in inventario.items():
        estado = "Disponible" if info["disponible"] else "Prestado"
        print(f"Equipo: {nombre} | Estado: {estado}")

def registrar_prestamo():
    mostrar_equipos()
    nombre_equipo = input("\nIngrese el nombre exacto del equipo a prestar: ")
    
    if nombre_equipo in inventario:
        if inventario[nombre_equipo]["disponible"]:
            usuario = input("Nombre del usuario: ")
            fecha = datetime.date.today().strftime("%d/%m/%Y")
            
            datos_prestamo = (usuario, fecha)
            inventario[nombre_equipo]["prestamos"].append(datos_prestamo)
            
            inventario[nombre_equipo]["disponible"] = False
            print(f"Préstamo registrado: {nombre_equipo} entregado a {usuario}.")
        else:
            print("El equipo ya se encuentra prestado.")
    else:
        print("El equipo no existe en el sistema.")

def devolver_equipo():
    nombre_equipo = input("\nIngrese el nombre del equipo a devolver: ")
    
    if nombre_equipo in inventario:
        if not inventario[nombre_equipo]["disponible"]:
            inventario[nombre_equipo]["disponible"] = True
            print(f"Devolución exitosa: {nombre_equipo} ya está en bodega.")
        else:
            print("Este equipo ya estaba marcado como disponible.")
    else:
        print("El equipo no existe.")

def ver_historial():
    print("\n=== Historial Completo de Préstamos ===")
    for nombre, info in inventario.items():
        print(f"\nEquipo: {nombre}")
        if info["prestamos"]:
            for usuario, fecha in info["prestamos"]:
                print(f"- Prestado a: {usuario} el día {fecha}")
        else:
            print("- Sin préstamos registrados.")

def agregar_equipo():
    nuevo_nombre = input("\nNombre del nuevo equipo: ")
    if nuevo_nombre not in inventario:
        inventario[nuevo_nombre] = {"disponible": True, "prestamos": []}
        print(f"✅ {nuevo_nombre} agregado al inventario correctamente.")
    else:
        print("El equipo ya existe.")

def menu():
    while True:
        print("\n********** SISTEMA DE PRÉSTAMOS **********")
        print("1. Ver equipos disponibles")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial de préstamos")
        print("5. Agregar nuevo equipo")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_equipos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            devolver_equipo()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
        elif opcion == "6":
            print("Saliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("Opcíon no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()