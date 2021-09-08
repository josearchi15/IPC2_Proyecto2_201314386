from maquina import Maquina
from tkinter import *
from tkinter import filedialog
import xml.etree.ElementTree as ET


root = Tk()
root.title("Proyecto 2: Brazos de ensamblaje")
root.geometry('600x600')
root.configure(background="#333333")



archivo = StringVar()

def openFile():
    seleccionado = filedialog.askopenfilename(title='Seleccina archivo', filetypes=(('Archivos xml', '*.xml'), ('Todos', '*')))
    archivo.set(seleccionado)
    # constuirMaquina(archivo.get())
    # print(seleccionado)
    
def constuirMaquina(file):
    tree = ET.parse(file)
    root = tree.getroot()

    maquina = Maquina("Maquina") 

    for el in root:
        if el.tag == "CantidadLineasProduccion":
            maquina.setLineas(int(el.text))
        elif el.tag == "ListadoLineasProduccion":
            for lp in el:
                noLiena = lp[0].text.replace(" ", "").replace("\n","")
                componentes = lp[1].text.replace(" ", "").replace("\n","")
                tiempo = lp[2].text.replace(" ", "").replace("\n","")
                print("Linea: ",noLiena," comp: ",componentes," tiempo: ",tiempo)
        elif el.tag == "ListadoProductos":
            for pro in el:
                print(pro[0].text+"\n")
                print(pro[1].text)

abrir = Button(root, text='Seleccionar archivo', command=openFile)
abrir.pack()
ruta = Entry(root, textvariable=archivo).pack()

# action = Button(root, text='Accion', command=openFile).pack()
action2 = Button(root, text='Procesar', command=lambda: constuirMaquina(archivo.get())).pack()

root.mainloop()