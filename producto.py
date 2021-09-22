from cola import Cola
from maquina import Maquina

class Producto:
    def __init__(self, nombre, instrucciones):
        self.nombre = nombre
        self.instrucciones = instrucciones
        self.pasos = Cola()
        self.tiempo = 0
        self.lineasProduccion = Cola()

    def getPasos(self):
        arr = self.instrucciones.split('p')
        puntoLinea = Cola()
        puntoComponente = Cola()
        
        for i in range(len(arr)-1):
            if i%2 == 0:
                # print(arr[i]," es par")
                puntoLinea.agregar(arr[i])
            else:
                # print(arr[i]," es impar")
                puntoComponente.agregar(arr[i])

        while not puntoLinea.estaVacia() and not puntoComponente.estaVacia():
            punto = {
                "linea": puntoLinea.pop().split("L")[1],
                "componente": puntoComponente.pop().split("C")[1]
            }
            self.pasos.agregar(punto)

    def getLineasProducto(self, maquina):
        #se recorren los pasos del producto para identificar la cantiad de lineas que recorre y se crea una cola con las lineas que necesita el producto
        pasos = Cola()
        self.getPasos()
        pasos = self.pasos
        lineasProducto2 = Cola()
        while not pasos.estaVacia():
            paso = pasos.pop()  #se obtiene objeto {linea, componente}
            print("Linea: "+paso["linea"]+" componente: "+paso["componente"])
            linea = maquina.getLinea(int(paso["linea"]))
            if not lineasProducto2.buscar(linea):
                lineasProducto2.agregar(linea)
            if lineasProducto2.buscar(linea):
                linea.agregarPaso(paso)
        self.lineasProduccion = lineasProducto2
        print(self.nombre+" usa "+str(lineasProducto2.tamano())+" lineas. \n")
        # return lineasProducto2



















# p1 = Producto("Smartwatch", "L1pC2pL2pC1pL2pC2pL1pC4p")
# p1.getPasos()