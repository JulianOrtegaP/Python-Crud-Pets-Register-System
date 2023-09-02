import sqlite3

def conexion():
    miconexion=sqlite3.connect("mascotas.db")
    miCursor=miconexion.cursor()
    try:
        miCursor.execute("""
        CREATE TABLE IF NOT EXISTS mascotas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni TEXT NOT NULL UNIQUE,
        nombremascota VARCHAR (50),
        edad INTEGER NOT NULL,
        raza VARCHAR (50),
        animal VARCHAR (20),
        nombreduenio VARCHAR (50) UNIQUE
        )
        """)
        
        print ("BBDD creada con exito")
        miCursor.close()
        return miconexion
    except Exception as ex:
        print("Error de Conexion:",ex)
        miCursor.close()
    return miconexion