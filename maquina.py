from listaSimpleEnlazada import ListaNoOrdenada


class Maquina():
    def __init__(self, nombre):
        self.nombre = nombre
        self.noLineas = 0
        self.lineasProduccion = ListaNoOrdenada()
    
    def setLineas(self, numero):
        self.noLineas = numero

    def addLinea(self, linea):
        self.lineasProduccion.agregar(linea)
