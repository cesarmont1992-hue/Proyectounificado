#---------------------------------------
##PROYECTO UNIFICADO
#CRUD CON TKINTER + SQLITE

from tkinter import * 
from tkinter import messagebox 
from tkinter import ttk 
import sqlite3 
from pathlib import Path 

#----------------------------- 
#RUTA DEL PROYECTO 
#----------------------------- 
base_dir = Path(__file__).resolve().parent 
#BASE DE DATOS EN LA MISMA CARPETA DEL PROGRAMA 
RUTA_BBDD = base_dir / "BaseCRMZ.db" 
RUTA_ICONO = base_dir / "interface_grafica.ico" 

raiz = Tk() 
raiz.title("CRUD OM TKINTER + SQLITE") 
ancho_ventana = 1100 
alto_ventana = 650 

if RUTA_ICONO.exists(): 
    try: 
        raiz.iconbitmap(str(RUTA_ICONO)) 
    except Exception as e: 
        print("No se pudo cargar el icono: ", e) 
else: 
    print("Advertencia: No se encontró el icono") 
print(RUTA_ICONO) 

#variables tkinter 
mild = StringVar() 
miNombre = StringVar() 
miPass = StringVar() 
miApellido = StringVar() 
miDireccion = StringVar() 

#Funciones BDD CONEXIONES 
def conexionBDD(): 
    conexion = sqlite3.connect(str(RUTA_BBDD)) 
    cursor = conexion.cursor() 
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS TBL_USUARIOS( 
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            NOMBRE_USUARIO VARCHAR(50), 
            PASSWORD VARCHAR(50), 
            APELLIDO VARCHAR(50), 
            DIRECCION VARCHAR (100), 
            COMENTARIOS VARCHAR(255) 
        ) 
    """) 
    conexion.commit() 
    conexion.close() 

#VALIDAR DATOS 
def validarCampos(): 
    if miNombre.get().strip() == "": 
        messagebox.showwarning( "Validación", "Ingrese el nombre" ) 
        return False 
    if miPass.get().strip() == "": 
        messagebox.showwarning( "Validación", "Ingrese la contraseña" ) 
        return False 
    if miApellido.get().strip() == "": 
        messagebox.showwarning( "Validación", "Ingrese la apellido" ) 
        return False 
    if miDireccion.get().strip() == "": 
        messagebox.showwarning( "Validación", "Ingrese Dirección" ) 
    return True 

#Validar ID 
def validarID(): 
    if mild.get().strip() == "": 
        messagebox.showwarning( "Validación", "Ingrese un ID" ) 
        return False 
    return True 

#Limpiar campos 
def limpiarCampos(): 
    mild.set("") 
    miNombre.set("") 
    miPass.set("") 
    miApellido.set("") 
    miDireccion.set("") 
    textComentario.delete( "1.0", END ) 

#CARGARR DATOS DE LA TABLA 
def CargarDatos(): 
    for fila in tabla.get_children(): 
        tabla.delete(fila) 
    conexion = sqlite3.connect(str(RUTA_BBDD)) 
    cursor = conexion.cursor() 
    cursor.execute( """ 
        SELECT ID, NOMBRE_USUARIO, PASSWORD, APELLIDO, DIRECCION, COMENTARIOS FROM TBL_USUARIOS ORDER BY ID 
    """ ) 

# CREAR REGISTRO 
def crear(): 
    if not validarCampos(): 
        return 
    conexion = sqlite3.connect(str(RUTA_BBDD)) 
    cursor = conexion.cursor() 
    cursor.execute(""" 
        INSERT INTO TBL_USUARIOS ( NOMBRE_USUARIO, PASSWORD, APELLIDO, DIRECCION, COMENTARIOS ) VALUES (?,?,?,?,?) 
    """, ( 
        miNombre.get().strip(), 
        miPass.get().strip(), 
        miApellido.get().strip(), 
        miDireccion.get().strip(), 
        textComentario.get("1.0", END).strip() 
    )) 
    conexion.commit() 
    conexion.close() 
    messagebox.showinfo( "BBDD", "registro guardo correctamente" ) 
    limpiarCampos() 
    CargarDatos() 

#LEER / CONSULTAR REGISTRO 
def leer(): 
    if not validarID(): 
        return 
    conexion = sqlite3.connect(str(RUTA_BBDD)) 
    cursor = conexion.cursor() 
    cursor.execute( """ 
        SELECT * FROM TBL_USUARIOS WHERE ID = ? 
    """, (mild.get(),) ) 
    usuario = cursor.fetchone() 
    conexion.close() 
    if usuario : 
        miNombre.set(usuario) 
        miPass.set(usuario) 
        miApellido.set(usuario) 
        miDireccion.set(usuario) 
        textComentario.delete( "1.0", END ) 
        textComentario.insert( "1.0", usuario ) 
    else: 
        messagebox.showwarning( "consulta", "no existe un registro con es ID" ) 

# ACTUALIZAR REGISTRO 
def actualizar(): 
    if not validarID(): 
        return 
    if not validarCampos(): 
        return 
    conexion = sqlite3.connect(str(RUTA_BBDD)) 
    cursor = conexion.cursor() 
    cursor.execute(""" 
        UPDATE TBL_USUARIOS SET NOMBRE_USUARIO = ?, PASSWORD = ?, APELLIDO = ?, DIRECCION = ?, COMENTARIOS = ? WHERE ID = ? 
    """, ( 
        miNombre.get().strip(), 
        miPass.get().strip(), 
        miApellido.get().strip(), 
        miDireccion.get().strip(), 
        textComentario.get("1.0", END).strip(), 
        mild.get() 
    )) 
    conexion.commit() 
    registros_actualizados = cursor.rowcount 
    conexion.close() 
    if registros_actualizados > 0: 
        messagebox.showinfo( "Actualizar", "Registro actualizado correctamente" ) 
    else: 
        messagebox.showwarning( "Actualizar", "No existe el ID" ) 
    CargarDatos() 
    limpiarCampos() 

#ELIMINAR REGISTRO 
def eliminar(): 
    if not validarID(): 
        return 
    respuesta = messagebox.askyesno( "Eliminar", "¿Desea elimiar este registro?" ) 
    if not respuesta: 
        return 
    conexion = sqlite3.connect(str(RUTA_BBDD)) 
    cursor = conexion.cursor() 
    cursor.execute( """ 
        DELETE FROM TBL_USUARIOS WHERE ID = ? 
    """, (mild.get(),) ) 
    conexion.commit() 
    registros_eliminados = cursor.rowcount 
    conexion.close() 
    if registros_eliminados > 0: 
        messagebox.showinfo( "Elimiar", "Registro eliminado correctamente" ) 
    else: 
        messagebox.showwarning( "Elimiar", "No existe ID" ) 
    CargarDatos() 
    limpiarCampos()

    #Seleccionar resgistro de tabla

    def selecionarRegistro(event):
        item = tabla.focus()
        if item == "":
            return
        datos = tabla.item(item)["Values"]
        if not datos:
            return
        miId.set(datos[0])
        miNombre.set()
