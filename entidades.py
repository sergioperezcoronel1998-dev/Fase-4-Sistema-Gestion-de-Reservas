# Entidades del Sistema
# Importamos ABC y abstractmethod para crear clases abstractas
# Clase abstracta

from abc import ABC, abstractmethod

# Importamos las excepciones necesarias para esta parte definidas en Excepciones.py

from excepciones import DatosInvalidosError

# Clase general para representar una entidad del sistema

class Entidad(ABC):
    # Constructor de la clase Entidad
    def __init__(self, identificacion, nombre):
        # Validamos que los datos no esten vacios
        if not identificacion or not nombre:
            raise DatosInvalidosError("Identificacion y nombre obligatorios.") 
        # Guardamos los datos como atributos
        self.identificacion = identificacion
        self.nombre = nombre 
    # Método abstracto que deberan implementar las clases que hereden de Entidad
    @abstractmethod
    def mostrar_informacion(self):
        pass    

# Clase cliente

class Cliente(Entidad):
    # Constructor de la clase Cliente
    def __init__(self, identificacion, nombre, correo):
        # Inicializamos los atributos de la clase base Entidad
        super().__init__(identificacion, nombre)
        # Validamos que el correo no este vacio
        if not correo:
            raise DatosInvalidosError("Correo obligatorio.")
        # Guardamos el correo como atributo
        self.correo = correo
    # Metodo para mostrar la información del cliente
    def mostrar_informacion(self):
        return(f"identificacion: {self.identificacion}, nombre: {self.nombre}, correo: {self.correo}")

# Propiedad para consultar información del cliente
    # Propiedad para consultar la identificacion del cliente
    @property
    def identificacion(self):
        return self._identificacion

    # Propiedad para consultar el nombre del cliente
    @property
    def nombre(self):
        return self._nombre

    # Propiedad para consultar el correo del cliente
    @property
    def correo(self):
        return self._correo

   