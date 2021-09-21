from cola import Cola
from maquina import Maquina
import xml.etree.ElementTree as ET
from lineaProduccion import LineaProduccion
from producto import Producto
    

def cleanText(text):
    cleanTxt = text.replace(" ", "").replace("\n","")
    return cleanTxt

def tiempoMovimiento(pi, pf):
	p1 = int(pi)
	p2 = int(pf)
	if p1 == p2:
		return 0
	elif p1 > p2:
		return p1 - p2
	elif p2 > p1:
		return p2 - p1

def tiempoEnsamble(linea1, linea2):
    t1 = linea1.tEnsamble
    t2 = linea2.tEnsamble
    if t1 > t2:
        return int(t1)
    elif t2 > t1:
        return int(t2)
    else:
        return int(t1)

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

    # while not listadoSimulacion.estaVacia():
    #     producto = listadoSimulacion.pop() 
    #     print(producto)
    #     pr = maquina.getProducto(producto)
    #     pr.getPasos()


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
    print(nombreProducto+" usa "+str(lineasProducto2.tamano())+" lineas.")

    pasosEnsambles = Cola()
    product.getPasos()
    pasosEnsambles = product.pasos
    tiempoEnsambles = 0
    ensambles = 0
    pasoActual = pasosEnsambles.cabeza
    # print(type(pasoActual.obtenerDato()["linea"]))
    # linea = maquina.getLinea(int(pasoActual.obtenerDato()['linea']))
    # print(linea.id)
    while pasoActual.obtenerSiguiente() != None:
        pasoSiguiente = pasoActual.obtenerSiguiente()
        ensambles += 1
        l1 = maquina.getLinea(int(pasoActual.obtenerDato()['linea']))
        l2 = maquina.getLinea(int(pasoSiguiente.obtenerDato()['linea']))
        tiempoEnsambles += tiempoEnsamble(l1, l2)
        pasoActual = pasoActual.obtenerSiguiente()
    print(product.nombre+" tardara: "+str(tiempoEnsambles)+" segundos y "+str(ensambles)+" pasos \n")

    

# fileTxt = "C:/Users/archi/Desktop/USAC 2021/IPC2/Laboratorio/EntradasProyecto2/Entradas/entrada1.xml"
# constuirMaquina(fileTxt)