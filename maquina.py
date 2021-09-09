from listaSimpleEnlazada import ListaNoOrdenada
from cola import Cola


class Maquina():
    def __init__(self, nombre):
        self.nombre = nombre
        self.noLineas = 0
        self.lineasProduccion = ListaNoOrdenada()
        self.productos = Cola()
    
    def setLineas(self, numero):
        self.noLineas = numero

    def addLinea(self, linea):
        self.lineasProduccion.agregar(linea)

    def addProducto(self, producto):
        self.productos.agregar(producto)
