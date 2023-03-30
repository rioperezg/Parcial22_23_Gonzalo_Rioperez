""""
Realiza el  código para calcular el determinante de una matriz cuadrada de [5 x 5], regla de Sarrus de forma recursiva y de 
forma iterativa
"""
# Primero haremos uan clase matrix que nos permita crear matrices 
class Matrix:
    def __init__(self, numeros):
        self.numeros = numeros
        self.filas = len(numeros)
        self.columnas = len(numeros[0]) if numeros else 0
    def obtener_elementos(self, fila, columna):
        return self.numeros[fila][columna]
    def obtener_fila(self, fila):
        return self.numeros[fila]
    def obtener_columna(self, columna):
        return [self.numeros[fila][columna] for fila in range(self.filas)]
    # Ahora pasamos a calcular determinantes mediante sarrus
    def Dterminante_itera(self):
        if self.filas == 2 and self.columnas == 2:
            return self.numeros[0][0] * self.numeros[1][1] - self.numeros[0][1] * self.numeros[1][0]
        else:
            determinante = 0
            for i in range(self.columnas):
                matriz = Matrix([self.obtener_fila(fila) for fila in range(1, self.filas)])
                determinante += (-1) ** i * self.obtener_elementos(0, i) * matriz.Dterminante_itera()
            return determinante


























def main():



if __name__ == "__main__":
main()