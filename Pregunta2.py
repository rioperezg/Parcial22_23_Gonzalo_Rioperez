""""
Recorre el listado del ejemplo y realiza las siguientes operaciones:

[18, 50, 210, 80, 145, 333, 70, 30]

Imprimir el número en caso de que sea múltiplo de 10 y menor que 200
Parar el programa si llega a un número mayor que 300
Organizar la lista mediante el método de ordenamiento merge sort
Dada la lista anterior y un valor 145 devolver el índice de 145 en la lista si 145 está en la lista, y −1 si 145 no está en la lista

"""
class nodoCola(object):
    info, sig = None, None
class Cola(object):
    def __init__(self):
        self.frente, self.final = None, None
        self.tamaño = 0
    def arribo(cola, dato):
        nodo = nodoCola()
        nodo.info = dato
        if cola.frente is None:
            cola.frente = nodo
        else:
            cola.final.sig = nodo
        cola.final = nodo
        cola.tamaño += 1
    def atencion(cola, dato):
        dato = cola.frente.info
        cola.frente = cola.frente.sig
        if cola.frente is None:
            cola.final = None
            cola.tamaño -= 1
            return dato
    def cola_vacia(cola):
        return cola.frente is None
    def en_frente(cola):
        return cola.frente.info
    def tamaño(cola):
        return cola.tamaño
    def mover_al_final(cola):
        dato = Cola.atencion(cola)
        Cola.arribo(cola,dato)
        return dato
    # Primera forma barrido, ineficiente(n^2)
    def barrido(cola):
        caux = Cola()
        while(not Cola.cola_vacia(cola)):
            dato = Cola.atencion(cola)
            print(dato)
            Cola.arribo(caux, dato)
        while(not Cola.cola_vacia(caux)):
            dato = Cola.atencion(caux)
            Cola.arribo(cola,dato)
    # Segunda forma barrido, eficiente(n)
    def barrido2(cola):
        i = 0
        while(i < Cola.tamaño(cola)):
            dato = Cola.mover_al_final(cola)
            print(dato)
            i += 1

def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
    return lista        

def Imprimir(listado):
    # Para hacerlo de forma recursiva pondremos condiciones: hasta que la lista no este vacia....
    auxc = Cola()
    if listado == []:   
        if Cola.cola_vacia(auxc) == True:
            return "El listado esta vacio"
        # La funcion parar la integraremos en esta funcion
    else:
        dato1 = listado[0]
        if dato1 > 300:
            return "El numero es mayor a 300"
        else:  
            listado.pop(0)
            Cola.arribo(auxc, dato1)
            dato = Cola.atencion(auxc, dato1)
            if dato % 10 == 0 and dato < 200:
                print(dato)
            else:
                pass
        return(Imprimir(listado))
def devolver_indice(listilla, valor):
    if valor not in listilla:
        listilla.append(valor)
    else: 
        pass
    list_ord = merge_sort(listilla)
    for indice, elemento in enumerate(list_ord):
        if elemento == valor:
            return indice
 
print(Imprimir([18, 50, 210, 80, 145, 333, 70, 30]))
print(devolver_indice([18, 50, 210, 80, 145, 333, 70, 30], 145))































