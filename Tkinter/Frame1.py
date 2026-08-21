import os  # 1. Importamos la librería para gestionar rutas del sistema
from tkinter import *

raiz = Tk()
raiz.title("VENTANA DE PRUEBA")

# 2. Detectamos automáticamente la carpeta donde está tu archivo Frame1.py
carpeta_actual = os.path.dirname(__file__)

# 3. Unimos la carpeta actual con el nombre de tu imagen PNG
ruta_completa_imagen = os.path.join(carpeta_actual, "interface_grafica.png")

# 4. Cargamos la imagen usando la ruta exacta calculada por Python
icono = PhotoImage(file=ruta_completa_imagen)
raiz.wm_iconphoto(False, icono)

raiz.config(bg="red")

miFrime = Frame(raiz)
miFrime.pack(padx=50, pady=50)

miFrime.config(bg="blue")
miFrime.config(width=650, height=350)
miFrime.config(bd=35)
miFrime.config(relief="groove")
miFrime.config(cursor="hand2")

raiz.mainloop()
