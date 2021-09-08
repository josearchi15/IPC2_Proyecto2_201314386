from maquina import Maquina
import xml.etree.ElementTree as ET

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
                # linea = "Linea: ",noLiena," comp: ",componentes," tiempo: ",tiempo
                print("Linea: ",noLiena," comp: ",componentes," tiempo: ",tiempo)
        elif el.tag == "ListadoProductos":
            for pro in el:
                print(pro[0].text+"\n")
                print(pro[1].text)

# fileTxt = "C:/Users/archi/Desktop/USAC 2021/IPC2/Laboratorio/EntradasProyecto2/Entradas/entrada1.xml"
# constuirMaquina(fileTxt)