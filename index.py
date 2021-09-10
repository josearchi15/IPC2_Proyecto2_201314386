from tkinter import *
from tkinter import filedialog
from main import constuirMaquina, construirSimulacion

root = Tk()
root.title("Proyecto 2: Brazos de ensamblaje")
root.geometry('600x600')
root.configure(background="#333333")



archivo = StringVar()

def openFile():
    seleccionado = filedialog.askopenfilename(title='Seleccina archivo', filetypes=(('Archivos xml', '*.xml'), ('Todos', '*')))
    archivo.set(seleccionado)
    constuirMaquina(archivo.get())

def openFile2():
    seleccionado = filedialog.askopenfilename(title='Seleccina archivo', filetypes=(('Archivos xml', '*.xml'), ('Todos', '*')))
    archivo.set(seleccionado)
    construirSimulacion(archivo.get())
    
abrir = Button(root, text='Seleccionar archivo', command=openFile)
abrir.pack()
ruta = Entry(root, textvariable=archivo).pack()

simulacion = Button(root, text='Seleccionar simulacion', command=openFile2)
simulacion.pack()
ruta2 = Entry(root, textvariable=archivo).pack()

# action2 = Button(root, text='Procesar', command=lambda: constuirMaquina(archivo.get())).pack()

root.mainloop()