# Entidades del Sistema
# Importamos ABC y abstractmethod para crear clases abstractas
# Clase abstracta

from abc import ABC, abstractmethod

# Importamos las excepciones necesarias para esta parte definidas en excepciones.py

from excepciones import DatosInvalidosError

# Clase general para representar una entidad del sistema

class Entidad(ABC):
    # Constructor de la clase Entidad
    def __init__(self, identificacion, nombre):
        # Validamos que los datos no esten vacios y que la identificacion y el nombre sean cadenas de texto
        if not isinstance(identificacion, str) or not isinstance(nombre, str):
            raise DatosInvalidosError("Identificacion y nombre deben ser texto.") 
        if not identificacion.strip() or not nombre.strip():
            raise DatosInvalidosError("Identificacion y nombre obligatorios.") 
        # Guardamos los datos como atributos
        self._identificacion = identificacion.strip()
        self._nombre = nombre.strip()
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
        if not correo or not isinstance(correo, str):
            raise DatosInvalidosError("Correo obligatorio.")
        # Validamos que el correo tenga un formato valido
        if "@" not in correo or "." not in correo:
            raise DatosInvalidosError("Correo invalido, formato no aceptado.")
        # Guardamos el correo como atributo
        self.correo = correo
    # Metodo para mostrar la información del cliente
    def mostrar_informacion(self):
        return(f"identificacion: {self._identificacion}, nombre: {self._nombre}, correo: {self._correo}")

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
        return self.__correo

    # Propiedad para establecer el correo del cliente
    @correo.setter
    def correo(self, nuevo_correo):
        if not nuevo_correo or not isinstance(nuevo_correo, str):
            raise DatosInvalidosError("Correo obligatorio.")
        if "@" not in nuevo_correo or "." not in nuevo_correo:
            raise DatosInvalidosError("Correo invalido, formato no aceptado.")
        self.__correo = nuevo_correo.strip()
