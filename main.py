from cola import Cola
from maquina import Maquina
import xml.etree.ElementTree as ET
from lineaProduccion import LineaProduccion
from producto import Producto
    

def cleanText(text):
    cleanTxt = text.replace(" ", "").replace("\n","")
    return cleanTxt


maquina = Maquina("Maquina") 
def constuirMaquina(file):
    tree = ET.parse(file)
    root = tree.getroot()


    for el in root:
        if el.tag == "CantidadLineasProduccion":
            maquina.setLineas(int(el.text))
        elif el.tag == "ListadoLineasProduccion":
            for lp in el:
                noLiena = int(cleanText(lp[0].text))
                componentes = int(cleanText(lp[1].text))
                tiempo = int(cleanText(lp[2].text))
                lineaP = LineaProduccion(noLiena, componentes, tiempo)
                maquina.addLinea(lineaP)
        elif el.tag == "ListadoProductos":
            for pro in el:
                nombre = cleanText(pro[0].text)
                instrucciones = cleanText(pro[1].text)
                product = Producto(nombre, instrucciones)
                maquina.addProducto(product)

    # maquina.showInfo()


listadoSimulacion = Cola()
def construirSimulacion(file):
    tree = ET.parse(file)
    root = tree.getroot()


    for el in root:
        if el.tag == "ListadoProductos":
            for prod in el:
                listadoSimulacion.agregar(str(cleanText(prod.text)))


def printPasos():
    while not listadoSimulacion.estaVacia():
        nombreProducto = listadoSimulacion.pop()
        madeProducto(nombreProducto)




def madeProducto(nombreProducto):
    product = maquina.getProducto(nombreProducto)
    print("Construyendo: --->  ", product.nombre)


    #se recorren los pasos del producto para identificar la cantiad de lineas que recorre y se crea una cola con las lineas que necesita el producto
    pasos = Cola()
    product.getPasos()
    pasos = product.pasos
    lineasProducto2 = Cola()
    while not pasos.estaVacia():
        paso = pasos.pop()  #se obtiene objeto {linea, componente}
        print("Linea: "+paso["linea"]+" componente: "+paso["componente"])
        linea = maquina.getLinea(int(paso["linea"]))
        if not lineasProducto2.buscar(linea):
            lineasProducto2.agregar(linea)
        if lineasProducto2.buscar(linea):
            linea.agregarPaso(paso)
    print(nombreProducto+" usa "+str(lineasProducto2.tamano())+" lineas.")

    # se recorren los pasos para ver cuantos pasos/ensambles hay y el tiempo que estos se llevaran
    pasosEnsambles = Cola()
    product.getPasos()
    pasosEnsambles = product.pasos
    tiempoEnsambles = 0
    ensambles = 0

    pasoActual = pasosEnsambles.pop()
    while not pasosEnsambles.estaVacia():
        pasoSiguiente = pasosEnsambles.pop()
        ensambles += 1
        l2 = maquina.getLinea(int(pasoSiguiente['linea']))
        tiempoEnsambles += l2.tEnsamble
    print(product.nombre+" tardara: "+str(tiempoEnsambles)+" segundos y "+str(ensambles)+" pasos \n")    

    

# fileTxt = "C:/Users/archi/Desktop/USAC 2021/IPC2/Laboratorio/EntradasProyecto2/Entradas/entrada1.xml"
# constuirMaquina(fileTxt)

