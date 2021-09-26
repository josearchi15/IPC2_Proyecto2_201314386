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


def getPasosEnsamblaje(producto):
    # se recorren los pasos para ver cuantos pasos/ensambles hay y el tiempo que estos se llevaran
    pasosEnsambles = Cola()
    producto.getPasos()
    pasosEnsambles = producto.pasos
    tiempoEnsambles = 0
    ensambles = 0

    pasoActual = pasosEnsambles.pop()
    while not pasosEnsambles.estaVacia():
        pasoSiguiente = pasosEnsambles.pop()
        ensambles += 1
        l2 = maquina.getLinea(int(pasoSiguiente['linea']))
        tiempoEnsambles += l2.tEnsamble
    print(producto.nombre+" tardara: "+str(tiempoEnsambles)+" segundos y "+str(ensambles)+" pasos \n")  
    producto.ensambles = ensambles  

    
def madeProducto(nombreProducto):
    product = maquina.getProducto(nombreProducto)
    print("\n****Construyendo: --->  ", product.nombre)

    product.getLineasProducto(maquina)
    product.getPasosEnsamblaje(maquina)
    print("Ensambles: --->", product.ensambles)
    product.construir()
    product.showTable()

    maquina.resetLineas()

    # print("Status lineas maquina")
    # for l in range(0,maquina.noLineas,1):
    #             lineaRevisar = maquina.lineasProduccion.pop()
    #             lineaRevisar.getInfo()
    #             maquina.lineasProduccion.agregar(lineaRevisar)
