from tkinter import *
from tkinter import filedialog
from main import constuirMaquina, construirSimulacion, listadoSimulacion, madeProducto, printPasos

root = Tk()
root.title("Proyecto 2: Brazos de ensamblaje")
root.geometry('600x600')
root.configure(background="#333333")



maquina = StringVar()
simulacionRuta = StringVar()

def openFile():
    seleccionado = filedialog.askopenfilename(title='Seleccina archivo', filetypes=(('Archivos xml', '*.xml'), ('Todos', '*')))
    maquina.set(seleccionado)
    constuirMaquina(maquina.get())

def openFile2():
    seleccionado = filedialog.askopenfilename(title='Seleccina archivo', filetypes=(('Archivos xml', '*.xml'), ('Todos', '*')))
    simulacionRuta.set(seleccionado)
    construirSimulacion(simulacionRuta.get())
    
def listado():
    actual = listadoSimulacion.cabeza
    while actual != None:
        print(actual.obtenerDato())
        nombreProducto = actual.obtenerDato()
        # Label(root, text=actual.obtenerDato()).pack()
        producto = Button(root, text=nombreProducto, command=lambda: madeProducto(nombreProducto))
        producto.pack()
        actual = actual.obtenerSiguiente()




# GUI Aplicacion
    
abrir = Button(root, text='Seleccionar archivo', command=openFile)
abrir.pack()
ruta = Entry(root, textvariable=maquina).pack()

simulacion = Button(root, text='Seleccionar simulacion', command=openFile2)
simulacion.pack()
ruta2 = Entry(root, textvariable=simulacionRuta).pack()

printt = Button(root, text='Imprimir pasos', command=printPasos)
printt.pack()

lista = Button(root, text='Imprimir listado', command=listado)
lista.pack()

root.mainloop()