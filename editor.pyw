# Inicio del proyecto Editor de texto

from tkinter import *
from tkinter import filedialog as FileDialog
# Definicion de funciones

ruta = '' # Almacenara la ruta de un fichero

def nuevo():
    global ruta
    mensaje.set('Nuevo fichero')
    ruta = ''
    texto.delete(1.0, 'end')
    root.title('Nuevo fichero - FaFa texto Editor Inator')

def abrir():
    global ruta
    mensaje.set('Abrir fichero')
    ruta = FileDialog.askopenfilename(initialdir='C:', filetype=(('Ficheros de texto','*.txt'),), title='Abrir un fichero de texto')
    if ruta != '':
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0,'end')
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + ' - FaFa texto Editor Inator')



def guardar():
    global ruta
    mensaje.set('Guardar fichero')

def guardar_como():
    global ruta
    mensaje.set('Guardar fichero como')



# Configuramos la raiz
root = Tk()

root.title('FaFa texto Editor Inator')

# Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Nuevo', command=nuevo)
filemenu.add_command(label='Abrir', command=abrir)
filemenu.add_command(label='Guardar', command=guardar)
filemenu.add_command(label='Guardar como', command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label='Salir', command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

# Caja de texto central
texto = Text(root)
texto.pack(fill='both', expand=1)
texto.config(bd=0, padx=6, font=('Consolas',12))

# Monitor inferior
mensaje = StringVar()
mensaje.set('Bienvenido al mejor editor')
monitor = Label(root,textvar=mensaje, justify='left')
monitor.pack(side='left')

root.config(menu=menubar)
# Bucle de la aplicacion
root.mainloop()