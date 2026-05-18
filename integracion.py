import sqlite3

conexion = sqlite3.connect("nomina.db")
cursor = conexion.cursor()

archivo = open("nomina_unapec.txt", "r", encoding="latin-1")

lineas = archivo.readlines()

# Saltar encabezado
for linea in lineas[1:]:

    datos = linea.strip().split("|")

    id_profesor = int(datos[0])
    nombre = datos[1]
    cuenta = datos[2]
    salario = float(datos[3])

    # Insertar profesor si no existe
    cursor.execute(
        "SELECT * FROM profesores WHERE id = ?",
        (id_profesor,)
    )

    profesor = cursor.fetchone()

    if profesor is None:

        cursor.execute(
            """
            INSERT INTO profesores
            (id, nombre, cuenta, salario)
            VALUES (?, ?, ?, ?)
            """,
            (id_profesor, nombre, cuenta, salario)
        )

    # Insertar pago
    cursor.execute(
        """
        INSERT INTO pagos_nomina
        (profesor_id, monto)
        VALUES (?, ?)
        """,
        (id_profesor, salario)
    )

conexion.commit()

print("Integración completada correctamente")

archivo.close()
conexion.close()