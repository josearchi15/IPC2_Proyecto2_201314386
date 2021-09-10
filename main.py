from cola import Cola
from maquina import Maquina
import xml.etree.ElementTree as ET
from lineaProduccion import LineaProduccion
from producto import Producto
    
maquina = Maquina("Maquina") 
listadoSimulacion = Cola()

def cleanText(text):
    cleanTxt = text.replace(" ", "").replace("\n","")
    return cleanTxt

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
                # print("Linea: ",noLiena," comp: ",componentes," tiempo: ",tiempo)
        elif el.tag == "ListadoProductos":
            for pro in el:
                nombre = cleanText(pro[0].text)
                instrucciones = cleanText(pro[1].text)
                product = Producto(nombre, instrucciones)
                maquina.addProducto(product)

    # print('Tamano: ' + str(maquina.lineasProduccion.tamano()))
    # maquina.showInfo()


def construirSimulacion(file):
    tree = ET.parse(file)
    root = tree.getroot()


    for el in root:
        if el.tag == "ListadoProductos":
            for prod in el:
                listadoSimulacion.agregar(str(cleanText(prod.text)))

    while not listadoSimulacion.estaVacia():
        producto = listadoSimulacion.pop() 
        print(producto)
        pr = maquina.getProducto(producto)
        pr.getPasos()

# fileTxt = "C:/Users/archi/Desktop/USAC 2021/IPC2/Laboratorio/EntradasProyecto2/Entradas/entrada1.xml"
# constuirMaquina(fileTxt)