from nodo import Nodo

class ListaNoOrdenada:

    def __init__(self):      #en el constructor se asigna la cabeza como null, primer elemento de la lista
        self.cabeza = None

    def estaVacia(self):      #se valida si la lista esta vacia confirmando que el valor de cabeza inicial no ha cambiado. 
        return self.cabeza == None

    def agregar(self,item):      #agregamos un metodo a la lista pasando un dato a ella
        temp = Nodo(item)        #instanciamos una variable temporal tipo Nodo(valor), con su valor 
        temp.asignarSiguiente(self.cabeza)  #asignamos a temp.siguiente la variable cabeza, la cual su valor es null, haciendo que el siguiente de temp sea null
        self.cabeza = temp       #ahora hacemos que la cabeza sea ese nodo como valor de la cabeza de la lista

    def tamano(self):
        actual = self.cabeza       #aqui asignamo a actual la cabeza de la lista(el ultimo elemento ingresado)
        contador = 0               #un contador que nos indicara por cuantos valores hemos pasado hacia llegar al primero ingresado
        while actual != None:      #mientras la cabeza no sea null osea tenga valor
            contador = contador + 1  #contador se le suma 1
            actual = actual.obtenerSiguiente() #actual sera el siguiente valor, si este es null la iteracion termina

        return contador        #devolvemos el valor del contador

    def buscar(self,item):      #ingresamos un valor a buscar
        actual = self.cabeza    #empezamos desde la cabeza nuevamente
        encontrado = False      #asiganmos valor de encontrado falso por default 
        while actual != None and not encontrado:  #mientas el valor actual(cabeza) no sea null y encontrado siga siendo falso
            if actual.obtenerDato() == item:      #revisamos el valor actual y validamos si su valor es igual al que vuscamos
                encontrado = True                 #si son iguales encontrado es true por lo que ya no se cumple la condicion del while
            else:
                actual = actual.obtenerSiguiente() #si no es igual pasamos al siguiente valor 

        return encontrado    #ya sea que ya hayas encontrado el valor o que hayamos recorrido toda la lista, devolvemos el valor

    def remover(self,item):      #ingresamos un valor a encontrar, parecido a remover
        actual = self.cabeza     #asignamos la cabeza al actual
        previo = None            #previo es none al momento
        encontrado = False       #encontrado es falso hasta demostrar lo contrario
        while not encontrado:    #mientras encontrado siga siendo falso
            if actual.obtenerDato() == item:   #si actual.dato es igual a encontrado
                encontrado = True              #encontrado es verdadero ahora
            else:                           #si no
                previo = actual                #el valor actual pasara a ser el previo en la siguiente iteracion
                actual = actual.obtenerSiguiente() #y el actual sera el valor siguienete a este en la sigueinte iteracion

        if previo == None:                    #si ya fue encontrado
            self.cabeza = actual.obtenerSiguiente()  #
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente())