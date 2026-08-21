from tkinter import*
from tkinter import messagebox
import sqlite3
 #------------------------------
 # FUNCION: CONECTAR Y CREAR BASE
 #------------------------------

def conexionBBDD():
    miConexion = sqlite3.connect("BaseCesarMontoya.db")
    miCursor = miConexion.cursor()

    try:
        miCursor.execute("""
        CREATE TABLE IF NOT EXISTS DATOSUSUARIOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        NOMBRE_USUARIO VARCHAR(50),
        PASSWORD VARCHAR(50),
        APELLIDO VARCHAR(50),
        DIRECCION VARCHAR(50),
        COMENTARIOS VARCHAR(200)
        )
        
        """)

        miConexion.commit()
        messagebox.showinfo("BBDD", "Base de datos conectada o creada con exito.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrio un error: {str(e)}")
    finally:
        miConexion.close()

#---------------
#FUNCION: SALIR
def salirAplicacion():
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")

    if valor == "yes":
        root.destroy()

#FUNCION: LIMPIAR CAMPOS

def limpiarCampos():
    mild.set("")
    miNombre.set("")
    miPass.set("")
    miApellido.set("")
    miDireccion.set("")
    textComentario.delete(1.0, END)

def crear():
    try:
        miConexion = sqlite3.connect("BaseCesarMontoya.db")
        miCursor = miConexion.cursor()

        miCursor.execute("""        
            INSERT INTO DATOSUSUARIOS
            (NOMBRE_USUARIO, PASSWORD, APELLIDO, DIRECCION, COMENTARIOS)
        
            VALUES (?, ?, ?, ?, ?)        
        """, (
            miNombre.get(),
            miPass.get(),
            miApellido.get(),
            miDireccion.get(),
            textComentario.get("1.0", END)
        ))

        miConexion.commit()
        messagebox.showinfo("BBDD", "Registro insertado con exito")
        limpiarCampos()

    except Exception as e:
        messagebox.showerror("Error", f"No se puedo insertar: {str(e)}")

    finally: 
        miConexion.close()

### funcion leer registro 

def leer ():
    if not miId.get().strip():
        messagebox.showwarning("advertencia","debes ingresar un ID")
        return

    try:
        miConexion = sqlite3.connect("baseCesarmontoya.db")
        miCursor = miConexion.cursor()

        miCursor.execute(
            "SELECT * FROM DATOSUSUARIOS WHERE ID = ?",
            (miId.get(),)
        )

        usuario = miCursor.fetchone() 

        if usuario:
            miNombre.set(usuario[1])
            miPass.set(usuario[2])
            miApellido.set(usuario[3])
            miDireccion.set(usuario[4])

            textComentario.delete(1.0,END)
            textComentario.insert(1.0, usuario[5])

        else:
            messagebox.showwarning(
                "sin resultados",
                "no existe un usuario con ese ID"
            )

    except Exception as e:
        messagebox.showerror("error", f"no se pudo leer: {str(e)}")

    finally:
        miConexion.close()

####interfaz grafica

root = Tk()
root.title("CRUD CON TKINTER Y SQLITE")
root.geometry("400x350")

barraMenu = Menu(root)
root.config(menu=barraMenu)

#####menu crud

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)

miFrame = Frame(root)
miFrame.pack(pady=10)

mild = StringVar()
miNombre = StringVar()
miPAss = StringVar()
miApellido = StringVar()
miDireccion = StringVar()


Label(miFrame, text= "ID").grid(row=0, column=0, padx=5, pady=5)
Label(miFrame, text= "Nombre").grid(row=1, column=0, padx=5, pady=5)
Label(miFrame, text= "Password").grid(row=2, column=0, padx=5, pady=5)

Entry(miFrame, textvariable=mild).grid(row=0, column=1)
Entry(miFrame, textvariable=miNombre).grid(row=1, column=1)
Entry(miFrame, textvariable=miPAss, show="$").grid(row=2, column=1)


textComentario = Text(miFrame, width=25, height=5)
textComentario.grid(row=5, column=1)

scrollvert = Scrollbar(miFrame, command=textComentario.yview)
scrollvert.grid(row=5, column=2, sticky="nsew")

textComentario.config(yscrollcommand=scrollvert.set)

root.mainloop()