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

def getLineasProducto(producto):
    #se recorren los pasos del producto para identificar la cantiad de lineas que recorre y se crea una cola con las lineas que necesita el producto
    pasos = Cola()
    producto.getPasos()
    pasos = producto.pasos
    lineasProducto2 = Cola()
    while not pasos.estaVacia():
        paso = pasos.pop()  #se obtiene objeto {linea, componente}
        print("Linea: "+paso["linea"]+" componente: "+paso["componente"])
        linea = maquina.getLinea(int(paso["linea"]))
        if not lineasProducto2.buscar(linea):
            lineasProducto2.agregar(linea)
        if lineasProducto2.buscar(linea):
            linea.agregarPaso(paso)
    print(producto.nombre+" usa "+str(lineasProducto2.tamano())+" lineas.")
    return lineasProducto2


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

    
def madeProducto(nombreProducto):
    product = maquina.getProducto(nombreProducto)
    print("Construyendo: --->  ", product.nombre)
    lineasProducto = Cola()
    lineasProducto = getLineasProducto(product)
    getPasosEnsamblaje(product)

    pasosProducto = Cola()
    product.getPasos()
    pasosProducto = product.pasos

    productoFinalizado = False
    segundos = 0
    while not productoFinalizado:
        segundos += 1
        lineaRevision = lineasProducto.cabeza
        
        while lineaRevision != None:
            linea = lineaRevision.obtenerDato()
            if segundos == 1:
                linea.iniciar()
            linea.move()
            lineaRevision = lineaRevision.obtenerSiguiente()