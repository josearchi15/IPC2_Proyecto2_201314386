from tkinter import *
from tkinter import filedialog
from main import constuirMaquina

root = Tk()
root.title("Proyecto 2: Brazos de ensamblaje")
root.geometry('600x600')
root.configure(background="#333333")



archivo = StringVar()

def openFile():
    seleccionado = filedialog.askopenfilename(title='Seleccina archivo', filetypes=(('Archivos xml', '*.xml'), ('Todos', '*')))
    archivo.set(seleccionado)
    
abrir = Button(root, text='Seleccionar archivo', command=openFile)
abrir.pack()
ruta = Entry(root, textvariable=archivo).pack()

action2 = Button(root, text='Procesar', command=lambda: constuirMaquina(archivo.get())).pack()

root.mainloop()