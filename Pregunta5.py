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
        self.tamanio = 0

    # Para comparar atributos internos si fuera necesario
    def criterio(dato, campo=None):
        dic = {}
        if hasattr(dato, "__dict__"):
            dic = dato.__dict__
        if (campo is None) or (campo not in dic):
            return dato
        else:
            return dic[campo]

    @staticmethod
    def insertar(lista, dato, campo=None):
        """Inserta 'dato' en la lista 'lista' manteniendo un orden ascendente
           según el 'campo' si se define, o según 'dato' directamente."""
        nodo = nodoLista()
        nodo.info = dato

        # si la lista está vacía o el dato es menor que el primero
        if (lista.inicio is None) or \
           (Lista.criterio(lista.inicio.info, campo) > Lista.criterio(dato, campo)):
            nodo.sig = lista.inicio
            lista.inicio = nodo
        else:
            ant = lista.inicio
            act = lista.inicio.sig
            while (act is not None) and \
                  (Lista.criterio(act.info, campo) < Lista.criterio(dato, campo)):
                ant = act
                act = act.sig
            nodo.sig = act
            ant.sig = nodo

        lista.tamanio += 1

    @staticmethod
    def lista_vacia(lista):
        return (lista.inicio is None)

    @staticmethod
    def eliminar(lista, clave, campo=None):
        """Elimina 'clave' de la lista, si existe, y retorna el dato."""
        dato = None
        if lista.inicio is None:
            return None

        # caso 1: la clave está en el primer nodo
        if Lista.criterio(lista.inicio.info, campo) == Lista.criterio(clave, campo):
            dato = lista.inicio.info
            lista.inicio = lista.inicio.sig
            lista.tamanio -= 1
        else:
            anterior = lista.inicio
            actual = lista.inicio.sig
            while (actual is not None) and \
                  (Lista.criterio(actual.info, campo) != Lista.criterio(clave, campo)):
                anterior = actual
                actual = actual.sig
            if actual is not None:
                dato = actual.info
                anterior.sig = actual.sig
                lista.tamanio -= 1
        return dato

    @staticmethod
    def buscar(lista, buscado, campo=None):
        aux = lista.inicio
        while aux is not None and \
              (Lista.criterio(aux.info, campo) != Lista.criterio(buscado, campo)):
            aux = aux.sig
        return aux  # retorna el nodo o None si no se encontró

    @staticmethod
    def barrido(lista):
        """Muestra todos los elementos sin destruir la lista."""
        aux = lista.inicio
        while aux is not None:
            print(aux.info)
            aux = aux.sig


# -----------------------
# ESTRUCTURA DE PILA CORREGIDA (por si hace falta)
# -----------------------
class nodoPila(object):
    info, sig = None, None

class Pila(object):
    def __init__(self):
        self.cima = None
        self.tamanio = 0

    def apilar(self, dato):
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = self.cima
        self.cima = nodo
        self.tamanio += 1

    def desapilar(self):
        if self.cima is None:
            return None
        x = self.cima.info
        self.cima = self.cima.sig
        self.tamanio -= 1
        return x

    def pila_vacia(self):
        return (self.cima is None)

    def en_cima(self):
        return None if self.cima is None else self.cima.info

    def Tamaño(self):
        return self.tamanio

    def barrido(self):
        """Muestra todos los elementos sin destruir la pila."""
        paux = Pila()
        while not self.pila_vacia():
            dato = self.desapilar()
            print(dato)
            paux.apilar(dato)
        # restaurar elementos a la pila original
        while not paux.pila_vacia():
            self.apilar(paux.desapilar())


# -----------------------
# TABLAS HASH
# -----------------------

def crear_tabla(tamaño):
    """Crea y retorna una tabla hash de tamaño dado (lista de None)."""
    return [None] * tamaño

def cantidad_elementos1(tabla):
    """Retorna la cantidad de elementos en la tabla
       para la versión encadenada (open chaining)."""
    # Ojo: en el original se veía 'len(tabla) - tabla.count(None)' => eso se usaba para la cerrada
    # pero aquí definimos que es la 'open chaining' => sumamos la longitud de cada lista
    cant = 0
    for slot in tabla:
        if slot is not None:
            # slot es una Lista
            cant += slot.tamanio
    return cant

def cantidad_elementos2(tabla):
    """Retorna la cantidad de elementos en la tabla
       para la versión cerrada (simple)."""
    # Si la idea es que 'None' indica vacío, y un slot con un dato indica 1,
    # sumamos 1 por cada slot != None
    return len(tabla) - tabla.count(None)


def funcion_hash(dato, tamaño_tabla):
    """Función hash muy simple basada en la longitud
       del dato (convertido a str) mod tamaño_tabla."""
    return len(str(dato).strip()) % tamaño_tabla


# ========== Hash con Encadenamiento (Open Chaining) ==========
def agregar1(tabla, dato):
    """Inserta 'dato' en la tabla con encadenamiento."""
    pos = funcion_hash(dato, len(tabla))
    if tabla[pos] is None:
        tabla[pos] = Lista()  # se crea la lista enlazada en esa posición
    Lista.insertar(tabla[pos], dato)

def buscar1(tabla, buscado):
    """Busca 'buscado' en la tabla con encadenamiento.
       Retorna el nodo si lo encuentra, o None en caso contrario."""
    pos = funcion_hash(buscado, len(tabla))
    if tabla[pos] is not None:
        nodo = Lista.buscar(tabla[pos], buscado)
        if nodo is not None:
            return nodo.info
    return None

def quitar1(tabla, dato):
    """Elimina 'dato' de la tabla con encadenamiento, si existe."""
    pos = funcion_hash(dato, len(tabla))
    if tabla[pos] is not None:
        x = Lista.eliminar(tabla[pos], dato)
        # si la lista quedó vacía, poner None
        if Lista.lista_vacia(tabla[pos]):
            tabla[pos] = None
        return x
    return None


# ========== Hash Cerrada (Closed Hashing) MUY simple ==========
def agregar2(tabla, dato):
    """Inserta 'dato' en la tabla cerrada. 
       Si la casilla está ocupada => colisión, se notifica, 
       pero no resolvemos la colisión (incompleto)."""
    pos = funcion_hash(dato, len(tabla))
    if tabla[pos] is None:
        tabla[pos] = dato
    else:
        print("Se produjo una colision en pos", pos, "para:", dato)

def buscar2(tabla, buscado):
    """Busca 'buscado' en la tabla cerrada.
       Si no coincide, no se hace sondeo => incompleto."""
    pos = funcion_hash(buscado, len(tabla))
    if tabla[pos] is not None:
        if tabla[pos] == buscado:
            return pos
        else:
            print("aplicar funcion de sondeo => no implementado")
    return None

def quitar2(tabla, dato):
    """Elimina 'dato' en la tabla cerrada si coincide la casilla exacta."""
    pos = funcion_hash(dato, len(tabla))
    if tabla[pos] is not None:
        if tabla[pos] == dato:
            tabla[pos] = None
            return dato
        else:
            print("Aplicar funcion de sondeo => no implementado")
    return None


# ========== Lógica de encriptación y desencriptación ==========

def construir_tablas_encriptacion():
    """Ejemplo de cómo crear dos tablas hash 
       para encriptar y desencriptar caracteres ASCII 32..125.
       - La idea: a cada char se asocia una cadena de 8 caracteres (en la de encriptar).
       - Y en la de desencriptar, a cada cadena de 8 chars se asocia el char original.
       (Implementación a modo de ejemplo, sin colisiones ni mejoras).
    """
    # definimos el rango
    inicio_ascii = 32
    fin_ascii = 125
    num_chars = (fin_ascii - inicio_ascii + 1)

    # Creamos tablas => supongamos encadenamiento open chaining
    tabla_encrip = crear_tabla(num_chars * 2)  # o cualquier tamaño
    tabla_descrip = crear_tabla(num_chars * 2)

    # Asignamos a cada char un string (8 caracteres) => ejemplo tonto: char + "XXXXXXX"
    for code in range(inicio_ascii, fin_ascii+1):
        c = chr(code)
        # 'encriptado' = 8 caracteres => c repetido 8 veces solo como ejemplo
        encript_str = c * 8  
        # Insertar en tabla_encrip: la clave es c, el valor es encript_str
        # Insertar en tabla_descrip: la clave es encript_str, el valor es c
        # NOTA: la 'lista' de open chaining requeriría pares (clave, valor)
        # Cambiemos la 'insertar' en la lista => 
        #   a) definimos un par (c, encript_str)
        #   b) en la de desc => un par (encript_str, c)
        par_encrip = (c, encript_str)
        par_descrip = (encript_str, c)
        agregar1(tabla_encrip, par_encrip)
        agregar1(tabla_descrip, par_descrip)

    return tabla_encrip, tabla_descrip

def encriptar_cadena(cadena, tabla_encrip):
    """Dado que cada caracter se encripta a 8 chars, 
       usamos 'buscar1' asumiendo la clave es (caracter,???). 
       En esta demo, la clave real a buscar es (char, algo?). 
       Realmente, convendría un approach distinto."""
    salida = []
    for ch in cadena:
        # la 'clave' para buscar en la tabla => ch
        # en la tabla guardamos (ch, encript_str). Buscaremos un par con par[0] == ch
        # haremos un pequeño helper:
        par = buscar1(tabla_encrip, (ch, None)) 
        # 'buscar1' retornará la tupla (ch, encript_str) si la encuentra
        if par is not None and par[0] == ch:
            salida.append(par[1])  # encript_str
        else:
            salida.append("[UNK]")  # por si no se halló
    return "".join(salida)

def desencriptar_cadena(cadena_encriptada, tabla_descrip):
    """Dado que cada caracter se encripta a 8 chars,
       partimos la cadena en trozos de 8 y buscamos en la tabla 'descrip'."""
    salida = []
    # cada 8 chars es un token
    for i in range(0, len(cadena_encriptada), 8):
        chunk = cadena_encriptada[i:i+8]
        par = buscar1(tabla_descrip, (chunk, None))
        if par is not None and par[0] == chunk:
            salida.append(par[1])
        else:
            salida.append('?')
    return "".join(salida)


# -------------------
# EJEMPLO DE USO
# -------------------
if __name__ == "__main__":
    # Creamos tablas encriptar/desencriptar (demostración)
    te, td = construir_tablas_encriptacion()

    texto = "Hola!"
    encriptado = encriptar_cadena(texto, te)
    print("Texto original:", texto)
    print("Texto encriptado:", encriptado)
    desencriptado = desencriptar_cadena(encriptado, td)
    print("Texto desencriptado:", desencriptado)

    # Observa que en nuestro 'ejemplo' la encriptación es c * 8 => "HHHHHHHH" para 'H', etc.
    # Lo puedes adaptar a tu método real.




