import sqlite3
import os

def inicializar_bd_banco():
    """Crea la base de datos y la tabla del banco si no existen."""
    conexion = sqlite3.connect("bd_apap.db")
    cursor = conexion.cursor()
    
    # Tabla adaptada a los datos (id, nombre, cuenta, salario)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pagos_nomina (
            id_transaccion INTEGER PRIMARY KEY AUTOINCREMENT,
            id_profesor INTEGER NOT NULL,
            nombre_profesor TEXT NOT NULL,
            cuenta_destino TEXT NOT NULL,
            salario REAL NOT NULL
        )
    ''')
    conexion.commit()
    return conexion

    

def procesar_pull_nomina():
    archivo_txt = "nomina_unapec.txt"
    
    print("--- Iniciando proceso PULL (Banco APAP) ---")
    
    # Verificar que el archivo del PUSH exista
    if not os.path.exists(archivo_txt):
        print(f"X Error: El archivo {archivo_txt} no existe. Ejecuta push.py primero.")
        return

    conexion = inicializar_bd_banco()
    cursor = conexion.cursor()
    
    registros_a_guardar = []
    
    try:
        # 1. Leer el archivo de texto
        with open(archivo_txt, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            
            for linea in lineas[1:]:
                # Limpiar saltos de línea al final y separar por el delimitador "|"
                datos = linea.strip().split("|")
                
                # Validar que tengamos las 4 columnas (ID, NOMBRE, CUENTA, SALARIO)
                if len(datos) == 4:
                    id_profesor = int(datos[0])
                    nombre = datos[1]
                    cuenta = datos[2]
                    salario = float(datos[3])
                    
                    registros_a_guardar.append((id_profesor, nombre, cuenta, salario))

        # 2. Guardar en la Base de Datos
        if registros_a_guardar:
            cursor.executemany('''
                INSERT INTO pagos_nomina (id_profesor, nombre_profesor, cuenta_destino, salario)
                VALUES (?, ?, ?, ?)
            ''', registros_a_guardar)
            
            conexion.commit()
            print(f"¡Éxito! El Banco APAP ha procesado y guardado {cursor.rowcount} pagos en su Base de Datos.")
        else:
            print("El archivo se leyó, pero no contenía datos de profesores.")

    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")
        conexion.rollback()
    finally:
        conexion.close()

# Ejecutar el script
if __name__ == "__main__":
    procesar_pull_nomina()