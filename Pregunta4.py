""""
Creación (0,5 puntos)
Copia el ejercicio anterior y realicemos una modificación:

Junto al método init y calificación, vamos a crear otro método especial de Python, el método str. Al igual que init, debe ir 
encerrado entre dobles guiones bajos, y debe tener el siguiente formato:

def __str__(self): return "Lo que quiero mostrar"

Este método nos sirve para imprimir por pantalla la información de un objeto, si tenemos un objeto alumno1 creado y realizamos 
print(alumno1), Python ejecutará el contenido del método str (el método str lo que tiene que hacer es maquetar la información que 
desea en un string).

Experimentación (0,5 puntos)
Implementa el método str y haz que muestre el nombre y la nota del alumno
Crea algun objeto de la clase Alumno
Realiza print de esos objetos para visualizar por pantalla la información del str
"""
import unittest
class Alumno(object):
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        return("El alumno se ha creado con éxito")
    def calificacion(self):
        if self.nota >= 5:
            return("El alumno ha aprobado")
        else:
            return("El alumno ha suspendido")
    def __str__(self):
        return "{} ha sacado un {}".format(self.nombre, self.nota)



class test_pregunta2(unittest.TestCase):
    def test_calificacion(self):
        alumno1 = Alumno("Juan", 5)
        alumno2 = Alumno("Pedro", 4)
        self.assertEqual(alumno1, "El alumno ha aprobado")
        self.assertEqual(alumno2, "El alumno ha suspendido")
    def test_str(self):
        alumno1 = Alumno("Juan", 5)
        alumno2 = Alumno("Pedro", 4)
        self.assertEqual(alumno1, "Juan ha sacado un 5")
        self.assertEqual(alumno2, "Pedro ha sacado un 4")