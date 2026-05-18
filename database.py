import sqlite3

conexion = sqlite3.connect("nomina.db")

cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS profesores (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    cuenta TEXT NOT NULL,
    salario REAL NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pagos_nomina (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    profesor_id INTEGER,
    monto REAL,
    estado_pago TEXT DEFAULT 'PAGADO',
    fecha_pago TEXT DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (profesor_id)
    REFERENCES profesores(id)
)
""")

conexion.commit()

conexion.close()

print("Base de datos creada correctamente")