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
        print(nombreProducto)
        product1 = maquina.getProducto(nombreProducto)
        product1.getPasos()
        paso = product1.pasos.cabeza
        # print(type(paso.obtenerDato()["linea"]))
        lineasProducto = Cola()

        #se recorren los pasos del producto para identificar la cantiad de lineas que recorre y se crea una cola con las lineas que necesita el producto
        while paso != None:  
            linea = maquina.getLinea(int(paso.obtenerDato()["linea"]))
            if not lineasProducto.buscar(linea):
                lineasProducto.agregar(linea)
            paso = paso.obtenerSiguiente()
        print(nombreProducto+" usa "+str(lineasProducto.tamano())+" lineas.")

        lnActual = lineasProducto.cabeza
        while lnActual != None:

            pasoActual = product1.pasos.cabeza
            while pasoActual != None:
                p1 = lnActual.obtenerDato().posicion
                p2 = pasoActual.obtenerDato()["componente"]
                lnActual.obtenerDato().tiempo = tiempoMovimiento(p1,p2)
                lnActual.obtenerDato().posicion = p2
                pasoActual = pasoActual.obtenerSiguiente()
            
            print("Tiempo linea: ",lnActual.obtenerDato().id," = ", lnActual.obtenerDato().tiempo)
            lnActual = lnActual.obtenerSiguiente()


# fileTxt = "C:/Users/archi/Desktop/USAC 2021/IPC2/Laboratorio/EntradasProyecto2/Entradas/entrada1.xml"
# constuirMaquina(fileTxt)