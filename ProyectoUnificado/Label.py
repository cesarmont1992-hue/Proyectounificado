import os
from tkinter import *

# Carpeta de trabajo
directorio_actual = r"C:\Users\informatica.capacita\Desktop\Tkinter"

# 1. DIAGNÓSTICO: Ver qué archivos hay en la carpeta
print("\n--- REVISANDO CARPETA ---")
if os.path.exists(directorio_actual):
    archivos = os.listdir(directorio_actual)
    print(f"Archivos encontrados en la carpeta Tkinter:")
    for archivo in archivos:
        print(f" -> {archivo}")
else:
    print("La carpeta especificada no existe.")
print("-------------------------\n")

root = Tk()
root.title("Mi primera interfaz gráfica")
root.geometry("500x400")

# Intentar cargar el ícono de forma segura
ruta_icono = os.path.join(directorio_actual, "interface_grafica.gif")
if os.path.exists(ruta_icono):
    icono = PhotoImage(file=ruta_icono)
    root.wm_iconphoto(False, icono)
else:
    print("AVISO: No se encontró 'interface_grafica.gif'. Se abrirá sin ícono personalizado.")

miFrame = Frame(root, width=400, height=500)
miFrame.pack()

# Intentar cargar la imagen de forma segura
ruta_imagen = os.path.join(directorio_actual, "giphy.gif")
if os.path.exists(ruta_imagen):
    mImagen = PhotoImage(file=ruta_imagen)
    milabel = Label(miFrame, image=mImagen)
    milabel.place(x=100, y=100)
else:
    print("AVISO: No se encontró 'giphy.gif'.")
    milabel = Label(miFrame, text="[Falta la imagen giphy.gif]", fg="red")
    milabel.place(x=100, y=100)

root.mainloop()

