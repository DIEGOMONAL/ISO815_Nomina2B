profesores = [
    {"id": 1, "nombre": "Juan Perez",     "cuenta": "101-123456-7", "salario": 45000.00},
    {"id": 2, "nombre": "María Gonzalez", "cuenta": "101-234567-8", "salario": 52000.00},
    {"id": 3, "nombre": "Carlos Ramirez", "cuenta": "101-345678-9", "salario": 48000.00},
    {"id": 4, "nombre": "Ana Martinez",   "cuenta": "101-456789-0", "salario": 51000.00},
    {"id": 5, "nombre": "Luis Hernandez", "cuenta": "101-567890-1", "salario": 47000.00},
]

def generar_archivo():
    with open("nomina_unapec.txt", "w") as archivo:
        archivo.write("ID|NOMBRE|CUENTA|SALARIO\n")
        for profesor in profesores:
            linea = f"{profesor['id']}|{profesor['nombre']}|{profesor['cuenta']}|{profesor['salario']:.2f}\n"
            archivo.write(linea)
    print("Archivo generado exitosamente: nomina_unapec.txt")

generar_archivo()