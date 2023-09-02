import conexion as con

def save(mascota):
    try:
        db = con.conexion()
        miCursor=db.cursor()
        columnas=tuple(mascota.keys())
        valores=tuple(mascota.values())
        sql="INSERT INTO mascotas {campos} VALUES(?,?,?,?,?,?)".format(campos = columnas)
        miCursor.execute(sql,(valores))
        creada = miCursor.rowcount>0
        db.commit()
        miCursor.close()
        db.close()
        if creada:
            return{"respuesta":True,"mensaje":"Mascota registrada"}
        else:
            return{"respuesta":False,"mensaje":"No se logro registrar a la Mascota"}
        

    except Exception as ex:
        miCursor.close()
        db.close()
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
        
        miCursor.close()
        db.close()
        return{"respuesta":False,"mensaje":"No hay mascotas"}
    except Exception as ex:
        miCursor.close()
        db.close()
        return{"respuesta":False,"mensaje":str(ex)}


def find(dni):
    try:
        db=con.conexion()
        miCursor=db.cursor()
        miCursor.execute("SELECT* From mascotas WHERE dni="+dni)
        resultado=miCursor.fetchall()

        if resultado:
            info=resultado[0]
            mascota={"id":info[0],"dni":info[1],"nombremascota":[2],"edad":info[3],"raza":[4],"animal":[5],"nombreduenio":[6]}
            miCursor.close()
            db.close()
            return {"respuesta": True,"mascota":mascota, "mensaje":"consultado con exito"}
        else:
            miCursor.close()
            db.close()
            return{"respuesta":False,"mensaje":"No existe la mascota"}
    except Exception as ex:
        miCursor.close()
        db.close()
        return{"respuesta":False,"mensaje":str(ex)}
