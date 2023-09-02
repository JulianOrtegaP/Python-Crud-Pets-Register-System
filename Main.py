from tkinter import * 
from tkinter import ttk  
from tkinter import messagebox

import mascota as mas
ventana=Tk()
ventana.state("zoomed")
ventana.title("Gestion de Mascotas")

ventana.resizable(0,0)

txt_dni=StringVar()
txt_nombremascota=StringVar()
txt_edad=StringVar()
txt_raza=StringVar()
txt_animal=StringVar()
txt_duenio=StringVar()

Label(ventana,text="DNI dueño:",width=20,justify="left",anchor="w").grid(row=0,column=0)
Label(ventana,text="Nombre:",width=20,justify="left",anchor="w").grid(row=1,column=0)
Label(ventana,text="Edad(meses):",width=20,justify="left",anchor="w").grid(row=2,column=0)
Label(ventana,text="Raza:",width=20,justify="left",anchor="w").grid(row=3,column=0)
Label(ventana,text="Tipo de animal:",width=20,justify="left",anchor="w").grid(row=4,column=0)
Label(ventana,text="Nombre del dueño:",width=20,justify="left",anchor="w").grid(row=5,column=0)


e_dni=ttk.Entry(textvariable=txt_dni,width=30)
e_nombremascota=ttk.Entry(textvariable=txt_nombremascota,width=30)
e_edad=ttk.Entry(textvariable=txt_edad,width=30)
e_raza=ttk.Entry(textvariable=txt_raza,width=30)
e_animal=ttk.Entry(textvariable=txt_animal,width=30)
e_duenio=ttk.Entry(textvariable=txt_duenio,width=30)


e_dni.grid(row=0,column=1,pady=3)
e_nombremascota.grid(row=1,column=1,pady=3)
e_edad.grid(row=2,column=1,pady=3)
e_raza.grid(row=3,column=1,pady=3)
e_animal.grid(row=4,column=1,pady=3)
e_duenio.grid(row=5,column=1,pady=3)

e_dni.focus()





# Funcion guardar

def guardar():
    if txt_edad.get().isnumeric():
        mascota = {"dni":txt_dni.get(),"nombremascota":txt_nombremascota.get(),"nombreduenio":txt_duenio.get(),"raza":txt_raza.get(),"animal":txt_animal.get(),"edad":int(txt_edad.get())}
        res = mas.save(mascota)
        messagebox.showinfo("Mascota registrada",res.get("mensaje"))
    else:
        messagebox.showerror("upps!!","La edad debe ser numerica")


#Funcion Consultar


def consultar():
    if txt_dni.get()=="": #comillas indican que esta vacio el campo
        messagebox.showerror("upps!!","Debe indicar el DNI")
        e_dni.focus()
    else:
        res=mas.find(txt_dni.get())
        if(res.get("respuesta")):
            mascota=dict(res.get("mascota"))
            txt_nombremascota.set(mascota.get("nombremascota"))
            txt_raza.set(mascota.get("raza"))
            txt_animal.set(mascota.get("animal"))
            txt_duenio.set(mascota.get("nombreduenio"))
            txt_edad.set(mascota.get("edad"))
        else:
            messagebox.showwarning("upps!!","No se encontro la mascota con ese DNI")
            e_dni.focus()








################# BOTONES #################################


ttk.Button(ventana,text="Guardar",command=guardar).place(x=145,y=170)
ttk.Button(ventana,text="Consultar",command=consultar).place(x=250,y=170)








ventana.mainloop() 
