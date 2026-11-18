# Servicios del Sistema
# Importamos las herramientas para crear clases abstractas
from abc import ABC, abstractmethod

# Importamos las excepciones necesarias para esta parte definidas en Excepciones.py

from excepciones import DatosInvalidosError, CalculoInvalidoError

# Clase general para representar un servicio del sistema
class Servicio(ABC):
    # Constructor de la clase Servicio
    def __init__(self, codigo, nombre, precio):
        # Validamos que los datos no esten vacios y que el precio sea un numero positivo
        if not codigo or not nombre:
            raise DatosInvalidosError("El codigo y el nombre son obligatorios.")
        # Validamos que el precio sea un numero positivo
        if precio <= 0:
            raise CalculoInvalidoError("El precio debe ser un numero positivo.")
        # Guardamos los datos como atributos
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    # Método abstracto para calcular el costo del servicio
    @abstractmethod
    def calcular_costo(self, cantidad=1, descuento=0):
        pass

    # Metodo de mostrar descripción del servicio

    def mostrar_descripcion(self):
        pass

    