from cola import Cola
from maquina import Maquina

class Producto:
    def __init__(self, nombre, instrucciones):
        self.nombre = nombre
        self.instrucciones = instrucciones
        self.pasos = Cola()
        self.tiempo = 0
        self.lineasProduccion = Cola()
        self.productoFinalizado = False

    def getTiempoEnsamblaje(self, idLinea):
        actual = self.lineasProduccion.cabeza
        while actual != None:
            if actual.obtenerDato().id == idLinea:
                return actual.obtenerDato().tEnsamble
            actual = actual.obtenerSiguiente()


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


    def construir(self):
        
        colaPasos = Cola()
        self.getPasos()
        colaPasos = self.pasos
        paso1 = colaPasos.pop()
        paso1["status"] = False
        paso2 = colaPasos.pop()
        paso2["status"] = False
        # print('Paso1: ', paso1)
        # print('Paso2: ', paso2)

        
        while not self.productoFinalizado:
            self.tiempo += 1
            lineasARevisar = self.lineasProduccion.tamano() #numero de lineas a revisar cada vez



            # avanzar lineas
            for l in range(0,lineasARevisar,1):
                lineaRevisar = self.lineasProduccion.pop()
                if self.tiempo == 1:
                    lineaRevisar.firstStep()
                lineaRevisar.move()
                self.lineasProduccion.agregar(lineaRevisar)

            # revisar status pasos
            for l in range(0,lineasARevisar,1):
                lineaRevisar = self.lineasProduccion.pop()
                if lineaRevisar.id == int(paso1['linea']):
                    if lineaRevisar.posicion == int(paso1['componente']) and lineaRevisar.status == "Lista":
                        print('Paso1 listo para ensamblar')
                        paso1['status'] = True
                if lineaRevisar.id == int(paso2['linea']):
                    if lineaRevisar.posicion == int(paso2['componente']) and lineaRevisar.status == "Lista":
                        print('Paso2 listo para ensamblar')
                        paso2['status'] = True

                self.lineasProduccion.agregar(lineaRevisar)
            
            # si estan los pasos listos ensamblar
            if paso1['status'] and paso2['status']:
                print('\n Ensamblandooo!!\n')
                tiempoEnsamble = self.getTiempoEnsamblaje(int(paso2['linea']))

                while tiempoEnsamble > 0:
                    self.tiempo += 1
                    # print('Ensamblandooo----')

                    # esto lo tengo que encerrar en un while
                    for l in range(0,lineasARevisar,1):
                        linea = self.lineasProduccion.pop()
                        if linea.id == int(paso1['linea']) or linea.id == int(paso2['linea']):
                            linea.status = "Ensamblando"
                        else:
                            linea.move()
                        self.lineasProduccion.agregar(linea)

                    tiempoEnsamble -= 1


                self.productoFinalizado = True
                        



            # en este bloque solo se imprime el status de cada linea despues de haberse movido
            for l in range(0,lineasARevisar,1):
                lineaRevisar = self.lineasProduccion.pop()
                lineaRevisar.getInfo()
                self.lineasProduccion.agregar(lineaRevisar)

        
        print('-------------------------------------------------Tiempo total: ',self.tiempo)
            


















# p1 = Producto("Smartwatch", "L1pC2pL2pC1pL2pC2pL1pC4p")
# p1.getPasos()