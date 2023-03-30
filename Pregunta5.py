""""
La alianza rebelde necesita comunicarse de manera segura pero el imperio galáctico interviene todas la comunicaciones, por lo que 
la princesa Leia nos encarga el desarrollo de un algoritmo de encriptación para las comunicaciones rebeldes, que contemple los 
siguientes requerimientos:

 cada carácter deberá ser encriptado a ocho caracteres;
 se deberá generar dos tablas hash para encriptar y desencriptar, para los caracteres desde el “{” hasta el “}” –es decir desde el 
 32 al 125 de la tabla ASCII.
"""
class nodoLista(object):
    info, sig = None, None
class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamaño = 0
    def criterio(dato, campo = None):
        dic = {}
        if(hasattr(dato, "__dict__")):
            dic = dato.__dict__
        if campo is None or campo not in dic:
            return dato
        else:
            return dic[campo]    
    def insertar(lista, dato, campo=None):
        nodo = nodoLista()
        nodo.info = dato
        if (lista.inicio is None) or (Lista.criterio(lista.inicio.info, campo) > Lista.criterio(dato, campo)):
            nodo.sig = lista.inicio
            lista.inicio = nodo
        else:
            ant = lista.inicio
            act = lista.inicio.sig
            while(act is not None and Lista.criterio(act.info, campo) < Lista.criterio(dato, campo)):
                ant = ant.sig
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        lista.tamaño += 1
    def lista_vacia(lista):
        return lista.inicio is None
    def eliminar(lista, clave, campo=None):
        dato = None
        if(Lista.criterio(lista.inicio.info, campo) != Lista.criterio(clave, campo)):
            dato = lista.inicio.info
            lista.inicio = lista.inicio.sig
            lista.tamaño -= 1
        else:
            anterior = lista.inicio
            actual = lista.inicio.sig
            while(actual is not None and Lista.criterio(actual.info, campo) != Lista.criterio(clave, campo)):
                anterior = anterior.sig
                actual = actual.sig
            if (actual is not None):
                dato = actual.info
                anterior.sig = actual.sig
                lista.tamaño -= 1
        return dato
    def tamaño(lista):
        return lista.tamaño
    def buscar(lista, buscado, campo=None):
        aux = lista.inicio
        while(aux is not None and Lista.criterio(aux.info, campo) != Lista.criterio(buscado, campo)):
            aux = aux.sig
        return aux
    def barrido(lista):
        aux = lista.inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig





# TABLAS HASH
# def function"1" - tabla hash cerrada, mientras que def function"2" - tabla hash encadenada
def crear_tabla(tamaño):
    tabla = [None] * tamaño
def cantidad_elementos1(tabla):
    return len(tabla) - tabla.count(None)
def cantidad_elementos2(tabla):
    return sum(Lista.tamaño(lista) for lista in tabla if lista is not None)
def funcion_hash(dato, tamaño_tabla):
    return len(str(dato).strip()) % tamaño_tabla
def agregar1(tabla, dato):
    posicion = funcion_hash(dato, len(tabla))
    if(tabla[posicion] is None):
        tabla[posicion] = Lista()  
    Lista.insertar(tabla[posicion], dato)
def agregar2(tabla, dato):
    posicion = funcion_hash(dato, len(tabla))
    if(tabla[posicion] is None):
        tabla[posicion] = dato
    else:
        print("Se produjo una colision")
# def buscar1(tabla, buscado):
    # pos = None
    # posicion = funcion_hash(buscado, len(tabla))
    # if(tabla[posicion] is not None):
        # pos =....NO SE ENCUENTRA LA FUNCION BUSQUEDA
def buscar2(tabla, buscado):
    pos = None
    posicion = funcion_hash(buscado, len(tabla))
    if(tabla[posicion] is not None):
        if(buscado == tabla[posicion]):
            pos = posicion
        else:
            print("aplicar funcion de sondeo")
    return pos
def quitar1(tabla, dato):
    dato = None
    posicion = funcion_hash(dato, len(tabla))
    if(tabla[posicion] is not None):
        if(dato == tabla[posicion]):
            dato = tabla[posicion]
            tabla[posicion] = None
        else:
            print("Aplicar funcion de sondeo")
    return dato

def quitar2(tabla, dato):
    dato = None
    posicion = funcion_hash(dato, len(tabla))
    if(tabla[posicion] is not None):
        dato = Lista.eliminar(tabla[posicion], dato)
        if(Lista.lista_vacia(tabla[posicion])):
            tabla[posicion] = None
    return dato




