# Servicios del Sistema
# Importamos las herramientas para crear clases abstractas
from abc import ABC, abstractmethod

# Importamos las excepciones necesarias para esta parte definidas en Excepciones.py

from excepciones import DatosInvalidosError, CalculoInvalidoError

# Clase general para representar un servicio del sistema
class Servicio(ABC):

    # Constructor de la clase Servicio
    def __init__(self, codigo, nombre, precio):
        # Validamos que el codigo y el nombre sean cadenas de texto y que no esten vacios
        if not isinstance(codigo, str) or not isinstance(nombre, str):
            raise DatosInvalidosError("El codigo y el nombre deben ser cadenas de texto.")
        if not codigo.strip() or not nombre.strip():
            raise DatosInvalidosError("El codigo y el nombre son obligatorios.")
        # Validamos que el precio sea un numero positivo
        if isinstance(precio, bool) or not isinstance(precio, (int, float)):
            raise DatosInvalidosError("El precio debe ser un numero.")
        if precio <= 0:
            raise DatosInvalidosError("El precio debe ser un numero positivo.")
        # Guardamos los datos como atributos
        self._codigo = codigo.strip()
        self._nombre = nombre.strip()
        self._precio = precio

    # Proiedad para consultar nombre del servicio
    @property   
    def nombre(self):
        return self._nombre
    
    # Método abstracto para calcular el costo del servicio
    @abstractmethod
    def calcular_costo(self, cantidad=1, descuento=0):
        pass

    # Metodo de mostrar descripción del servicio

    @abstractmethod
    def mostrar_descripcion(self):
        pass

# Clase gestionar servicio de habitaciones

class ServicioHabitacion(Servicio):
    # Constructor del servicio de habitaciones
    def __init__(self, codigo, nombre, precio, capacidad):

        # Inicializamos los datos de la clase padre
        super().__init__(codigo, nombre, precio)
        # Validamos que la capacidad sea un numero positivo
        if isinstance(capacidad, bool) or not isinstance(capacidad, int):
            raise DatosInvalidosError("La capacidad debe ser un numero entero.")
        if capacidad <= 0:
            raise DatosInvalidosError("La capacidad debe ser un numero positivo.")
        # Guardamos la capacidad como atributo
        self._capacidad = capacidad

    # Metodo para calcular el costo del servicio de habitaciones por noches
    def calcular_costo(self, cantidad=1, descuento=0):
        try:
            # Validamos que capacidad y descuento sean numeros
            if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)):
                raise CalculoInvalidoError("La cantidad debe ser un numero.")
            if isinstance(descuento, bool) or not isinstance(descuento, (int, float)):
                raise CalculoInvalidoError("El descuento debe ser un numero.")
            # Validamos que la cantidad de noches sea un numero positivo
            if cantidad <= 0:
                raise CalculoInvalidoError("La cantidad de nochesdebe ser un numero positivo.")
            # Validamos que el descuento sea un numero entre 0 y 100
            if descuento < 0 or descuento > 100:
                raise CalculoInvalidoError("El descuento debe ser un numero entre 0 y 100.")
            # Calculamos el costo total del servicio
            subtotal = self._precio * cantidad
            total= subtotal - (subtotal * descuento / 100)
            return total
        except TypeError as error:
           raise CalculoInvalidoError("Los valores del calculo son invalidos.") from error

    # Mostramos la descripción del servicio de habitaciones
    def mostrar_descripcion(self):
        return(f"Habitacion: {self._nombre}, Capacidad: {self._capacidad} personas, Precio por noche: {self._precio}")

# Clase gestionar alquiler de equipos

class ServicioEquipo(Servicio):
    # Constructor del servicio de alquiler de equipos
    def __init__(self, codigo, nombre, precio, tipo_equipo):
        # Inicializamos los datos de la clase padre
        super().__init__(codigo, nombre, precio)
        # Validamos que el tipo de equipo sea una cadena de texto
        if not isinstance(tipo_equipo, str):
            raise DatosInvalidosError("El tipo de equipo debe ser texto.")  
        # Validamos que el tipo de equipo no este vacio
        if not tipo_equipo.strip():
            raise DatosInvalidosError("El tipo de equipo es obligatorio.")
        # Guardamos el tipo de equipo como atributo
        self._tipo_equipo = tipo_equipo.strip()

    # Metodo para calcular el costo del servicio de alquiler de equipos por dias
    def calcular_costo(self, cantidad=1, descuento=0):
        try:
            # Validamos que cantidad y descuento sean numeros
            if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)):
                raise CalculoInvalidoError("La cantidad debe ser un numero.")
            if isinstance(descuento, bool) or not isinstance(descuento, (int, float)):
                raise CalculoInvalidoError("El descuento debe ser un numero.")
            # Validamos que la cantidad de dias sea un numero positivo
            if cantidad <= 0:
                raise CalculoInvalidoError("La cantidad de dias debe ser un numero positivo.")
            # Validamos que el descuento sea un numero entre 0 y 100
            if descuento < 0 or descuento > 100:
                raise CalculoInvalidoError("El descuento debe ser un numero entre 0 y 100.")
            subtotal = self._precio * cantidad
            total= subtotal - (subtotal * descuento / 100)
            return total
        except TypeError as error:
           raise CalculoInvalidoError("Los valores del calculo son invalidos.") from error

    # Mostramos la descripción del servicio de alquiler de equipos
    def mostrar_descripcion(self):
        return(f"Alquiler de equipos: {self._nombre}, Tipo: {self._tipo_equipo}, Precio por dia: {self._precio}")

# Clase serivicio de consulta
class ServicioConsulta(Servicio):
    # Constructor del servicio de consulta
    def __init__(self, codigo, nombre, precio, especialidad):
        # Inicializamos los datos de la clase padre
        super().__init__(codigo, nombre, precio)
        # Validamos que la especialidad sea una cadena de texto
        if not isinstance(especialidad, str):
            raise DatosInvalidosError("La especialidad debe ser texto.")
        # Validamos que la especialidad no este vacia
        if not especialidad.strip():
            raise DatosInvalidosError("La especialidad es obligatoria.")
        # Guardamos la especialidad como atributo
        self._especialidad = especialidad.strip()

    # Metodo para calcular el costo del servicio de consulta por horas
    def calcular_costo(self, cantidad=1, descuento=0):
        try:
            # Validamos que cantidad y descuento sean numeros
            if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)):
                raise CalculoInvalidoError("La cantidad debe ser un numero.")
            if isinstance(descuento, bool) or not isinstance(descuento, (int,float)):
                raise CalculoInvalidoError("El descuento debe ser un numero.")  
            # Validamos que la cantidad de horas sea un numero positivo
            if cantidad <= 0:
                raise CalculoInvalidoError("La cantidad de horas debe ser un numero positivo.")
            # Validamos que el descuento sea un numero entre 0 y 100
            if descuento < 0 or descuento > 100:
                raise CalculoInvalidoError("El descuento debe ser un numero entre 0 y 100.")
            subtotal = self._precio * cantidad
            total= subtotal - (subtotal * descuento / 100)
            return total
        except TypeError as error:
           raise CalculoInvalidoError("Los valores del calculo son invalidos.") from error

    # Mostramos la descripción del servicio de consulta
    def mostrar_descripcion(self):
        return(f"Consulta: {self._nombre}, Especialidad: {self._especialidad}, Precio por hora: {self._precio}")