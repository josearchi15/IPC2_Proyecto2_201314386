from listaSimpleEnlazada import ListaNoOrdenada
from cola import Cola


class Maquina():
    def __init__(self, nombre):
        self.nombre = nombre
        self.noLineas = 0
        self.lineasProduccion = Cola()
        self.productos = Cola()
    
    def setLineas(self, numero):
        self.noLineas = numero

    def addLinea(self, linea):
        self.lineasProduccion.agregar(linea)

    def addProducto(self, producto):
        self.productos.agregar(producto)

    def showInfo(self):
        print("----------",self.nombre)
        while not self.lineasProduccion.estaVacia():
            linea = self.lineasProduccion.pop()
            linea.getInfo()
        
        while not self.productos.estaVacia():
            prod = self.productos.pop()
            print("Nombre: ",prod.nombre)
            prod.getPasos()
        
    def getLinea(self, lineaId):
        actual = self.lineasProduccion.cabeza    
        encontrado = False      
        while actual != None and not encontrado:  
            if actual.obtenerDato().id == lineaId:      
                encontrado = True                 
            else:
                actual = actual.obtenerSiguiente() 

        return encontrado 

    def getProducto(self, nombreProducto):
        actual = self.productos.cabeza    
        encontrado = False      
        while actual != None and not encontrado:  
            if actual.obtenerDato().nombre == nombreProducto:      
                encontrado = True                 
            else:
                actual = actual.obtenerSiguiente() 

        return actual.obtenerDato()
    
    
    def construirProducto(self, producto):
        pass