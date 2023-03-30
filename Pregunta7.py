""""
mplementar sobre el TDA polinomio desarrollado previamente las siguientes actividades:
•  restar;
•  dividir;
•  eliminar un término;
•  determinar si un término existe en un polinomio.
"""
class Nodo(object):
    info, sig = None, None

class datoPolinomio(object):
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino
class Polinomio(object):
    def __init__(self):
        self.termino_mayor = None
        self.grado = -1
    def agregar_termino(polinomio, termino, valor):
        aux = Nodo()
        dato = datoPolinomio(valor,termino)
        aux.info = dato
        if(termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
            return polinomio
        else:
            actual = polinomio.termino_mayor
            while(actual.sig is not None and termino < actual.sig.info.termino):
                actual = actual.sig 
            aux.sig = actual.sig
            actual.sig = aux
            return polinomio
    def modificar_termino(polinomio, termino, valor):
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino != termino):
            aux = aux.sig 
        aux.info.valor = valor
    def Obtener_valor(polinomio, termino):
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino > termino):
            aux = aux.sig
        if(aux is not None and aux.info.termino == termino):
            return aux.info.valor
        else:
            return 0
    def mostrar(polinomio):
        aux = polinomio.termino_mayor
        pol = ''
        if(aux is not None):
            while(aux is not None):
                signo = ' '
                if(aux.info.valor >= 0):
                    signo += '+'
                pol += signo + str(aux.info.valor)+'x^'+str(aux.info.termino)
                aux = aux.sig
        return pol
    def sumar(polinomio1,polinomio2):
        paux = Polinomio()
        pol1 = polinomio1.termino_mayor
        while(pol1 is not None):
            pol2 = polinomio2.termino_mayor
            while(pol2 is not None):
                termino = pol1.info.termino + pol2.info.termino
                valor = pol1.info.valor * pol2.info.valor
                if(Polinomio.Obtener_valor(paux, termino)!= 0):
                    valor += Polinomio.Obtener_valor(paux, termino)
                    Polinomio.modificar_termino(paux, termino, valor)
                else:
                    Polinomio.agregar_termino(paux, termino, valor)
                pol2 = pol2.sig
                pol1 = pol1.sig 
        return paux   
    def eliminar_termino(polinomio, termino, valor): 
        aux = Nodo()
        dato = datoPolinomio(valor,termino)
        aux.info = dato
        if(termino == polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
            aux.info = ''
        else:
            print("No hay polinomio con este grado")