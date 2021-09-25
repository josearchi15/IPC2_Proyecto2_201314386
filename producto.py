from cola import Cola
from maquina import Maquina

class Producto:
    def __init__(self, nombre, instrucciones):
        self.nombre = nombre
        self.instrucciones = instrucciones
        self.pasos = Cola()
        self.tiempo = 0
        self.ensambles = 0
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

    def getPasosEnsamblaje(self, maquina):
        # se recorren los pasos para ver cuantos pasos/ensambles hay y el tiempo que estos se llevaran
        pasosEnsambles = Cola()
        self.getPasos()
        pasosEnsambles = self.pasos
        tiempoEnsambles = 0
        ensambles = 0

        pasoActual = pasosEnsambles.pop()
        while not pasosEnsambles.estaVacia():
            pasoSiguiente = pasosEnsambles.pop()
            ensambles += 1
            l2 = maquina.getLinea(int(pasoSiguiente['linea']))
            tiempoEnsambles += l2.tEnsamble
        print(self.nombre+" tardara: "+str(tiempoEnsambles)+" segundos y "+str(ensambles)+" pasos \n") 
        self.ensambles = ensambles  


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
        noEnsambles = 0

        
        while noEnsambles < self.ensambles:  #while not self.productoFinalizado:
            self.tiempo += 1
            lineasARevisar = self.lineasProduccion.tamano() #numero de lineas a revisar cada vez



            # avanzar lineas
            for l in range(0,lineasARevisar,1):
                lineaRevisar = self.lineasProduccion.pop()
                if self.tiempo == 1:
                    lineaRevisar.log = {}
                    lineaRevisar.firstStep()
                lineaRevisar.move()
                lineaRevisar.addLog(self.tiempo)
                self.lineasProduccion.agregar(lineaRevisar)

            # revisar si alguna linea ya esta lista para alguno de los pasos
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
                noEnsambles += 1

                tiempoEnsamble = self.getTiempoEnsamblaje(int(paso2['linea']))
                while tiempoEnsamble > 0:
                    self.tiempo += 1


                    if noEnsambles <= 1: #MODIFICACION TENTATIVA
                        for l in range(0,lineasARevisar,1):
                            linea = self.lineasProduccion.pop()
                            if linea.id == int(paso1['linea']) or linea.id == int(paso2['linea']): #analizar este cambio, que se solo si es del paso 2
                                linea.status = "Ensamblando"
                                linea.addLog(self.tiempo)
                            else:
                                linea.move()
                                linea.addLog(self.tiempo)
                            
                            self.lineasProduccion.agregar(linea)

                    else:
                        for l in range(0,lineasARevisar,1):
                            linea = self.lineasProduccion.pop()
                            if linea.id == int(paso2['linea']): 
                                linea.status = "Ensamblando"
                                linea.addLog(self.tiempo)
                            else:
                                linea.move()
                                linea.addLog(self.tiempo)
                            self.lineasProduccion.agregar(linea)

                    tiempoEnsamble -= 1
                

                #actualizar pasos
                paso1 = paso2 
                if colaPasos.estaVacia():
                    self.productoFinalizado = True
                else:               #validar este paso cuando ya no hay mas pasos**********
                    paso2 = colaPasos.pop()
                    paso2["status"] = False

                # cambiar de paso en lineas ensambladas
                for l in range(0,lineasARevisar,1):
                        linea = self.lineasProduccion.pop()
                        if linea.status == "Ensamblando": #aqui esta el otro clavo que como queda en este status pasa al siguiente paso
                            linea.nextStep()
                            # linea.move() podria ser una opcion
                        self.lineasProduccion.agregar(linea)


            
            # if colaPasos.estaVacia():
            #     self.productoFinalizado = True
                        



            # en este bloque solo se imprime el status de cada linea despues de haberse movido
            # for l in range(0,lineasARevisar,1):
            #     lineaRevisar = self.lineasProduccion.pop()
            #     lineaRevisar.getInfo()
            #     self.lineasProduccion.agregar(lineaRevisar)

        
        print('-------------------------------------------------Tiempo total: ',self.tiempo)
        for l in range(0,lineasARevisar,1):
                lineaRevisar = self.lineasProduccion.pop()
                print("\n Log de linea: ",str(lineaRevisar.id))
                lineaRevisar.printLog()
                self.lineasProduccion.agregar(lineaRevisar)
            


















# p1 = Producto("Smartwatch", "L1pC2pL2pC1pL2pC2pL1pC4p")
# p1.getPasos()