import conexion as con

# Funcion para guardar una mascota

def save(mascota):
    mascota=dict(mascota)

    try:
        db=con.conexion()
        miCursor=db.cursor()
        columnas=tuple(mascota.keys())
        valores=tuple(mascota.values())
        sql="""
        INSERT INTO mascotas{columnas} VALUES (?,?,?,?,?,?)
        """.format(columnas = columnas)
        miCursor.execute(sql,(valores))
        creada = miCursor.rowcount>0
        db.commit()
        
        if creada:
            miCursor.close()
            db.close()
            return{"respuesta":True,"mensaje":"Mascota registrada =)"}
        
        else:
            miCursor.close()
            db.close()
            return{"respuesta":False,"mensaje":"No se logro registrar a la Mascota"}
        
    except Exception as ex:

        return{"respuesta":False,"mensaje":str(ex)}
    
  


# Bloque para listar mascotas 

def findAll():
    try:
        db = con.conexion()
        miCursor=db.cursor()
        miCursor=db.execute("SELECT * FROM mascotas")
        mascotas=miCursor.fetchall()

        if mascotas:
            miCursor.close()
            db.close()
            return{"respuesta":True,"mascotas":mascotas,"mensaje":"lista de mascotas con exito"}
        
        else:
            miCursor.close()
            db.close()
            return{"respuesta":False,"mensaje":"No hay mascotas registradas aun"}
        
    except Exception as ex:
        miCursor.close()
        db.close()
        return{"respuesta":False,"mensaje":str(ex)}
  
        
# Bloque para actualizar a un persona por su DNI


def find(dniMascota):
    try:
        db=con.conexion()
        miCursor=db.cursor()
        miCursor.execute("SELECT * FROM mascotas WHERE dni={dni}".format(dni=dniMascota))
        resultado = miCursor.fetchall()

        if resultado:

            info=resultado[0]
            mascota={"id":info[0],"dni":info[1],"nombremascota":info[2],"edad":info[3],"raza":info[4],"animal":info[5],"nombreduenio":info[6]}
            miCursor.close()
            db.close()
            return {"respuesta": True,"mascota":mascota, "mensaje":"mascota encontrada"}
        
        else:

            miCursor.close()
            db.close()
            return{"respuesta":False,"mensaje":"No existe la mascota"}
        
    except Exception as ex:
        miCursor.close()
        db.close()
        return{"respuesta":False,"mensaje":str(ex)}
