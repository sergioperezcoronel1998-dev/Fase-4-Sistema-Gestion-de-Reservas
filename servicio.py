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

# Clase gestionar servicio de habitaciones

class ServicioHabitacion(Servicio):
    # Constructor del servicio de habitaciones
    def __init__(self, codigo, nombre, precio, capacidad):

        # Inicializamos los datos de la clase padre
        super().__init__(codigo, nombre, precio)
        # Validamos que la capacidad sea un numero positivo
        if capacidad <= 0:
            raise CalculoInvalidoError("La capacidad debe ser un numero positivo.")
        # Guardamos la capacidad como atributo
        self.capacidad = capacidad

    # Metodo para calcular el costo del servicio de habitaciones por noches
    def calcular_costo(self, cantidad=1, descuento=0):
        try:
            # Validamos que la cantidad de noches sea un numero positivo
            if cantidad <= 0:
                raise CalculoInvalidoError("La cantidad de nochesdebe ser un numero positivo.")
            # Validamos que el descuento sea un numero entre 0 y 100
            if descuento < 0 or descuento > 100:
                raise CalculoInvalidoError("El descuento debe ser un numero entre 0 y 100.")
            # Calculamos el costo total del servicio
            subtotal = self.precio * cantidad
            total= subtotal - (subtotal * descuento / 100)
            return total
        except TypeError as error:
           raise CalculoInvalidoError("Los valores del calculo son invalidos.") from error

    # Mostramos la descripción del servicio de habitaciones
    def mostrar_descripcion(self):
        return(f"Habitacion: {self.nombre}, Capacidad: {self.capacidad} personas, Precio por noche: {self.precio}")

# Clase gestionar alquiler de equipos

class ServicioEquipo(Servicio):
    # Constructor del servicio de alquiler de equipos
    def __init__(self, codigo, nombre, precio, tipo_equipo):
        # Inicializamos los datos de la clase padre
        super().__init__(codigo, nombre, precio)
        # Validamos que el tipo de equipo no este vacio
        if not tipo_equipo:
            raise DatosInvalidosError("El tipo de equipo es obligatorio.")
        # Guardamos el tipo de equipo como atributo
        self.tipo_equipo = tipo_equipo

    # Metodo para calcular el costo del servicio de alquiler de equipos por dias
    def calcular_costo(self, cantidad=1, descuento=0):
        try:
            # Validamos que la cantidad de dias sea un numero positivo
            if cantidad <= 0:
                raise CalculoInvalidoError("La cantidad de dias debe ser un numero positivo.")
            # Validamos que el descuento sea un numero entre 0 y 100
            if descuento < 0 or descuento > 100:
                raise CalculoInvalidoError("El descuento debe ser un numero entre 0 y 100.")
            subtotal = self.precio * cantidad
            total= subtotal - (subtotal * descuento / 100)
            return total
        except TypeError as error:
           raise CalculoInvalidoError("Los valores del calculo son invalidos.") from error

    # Mostramos la descripción del servicio de alquiler de equipos
    def mostrar_descripcion(self):
        return(f"Equipo: {self.nombre}, Tipo: {self.tipo_equipo}, Precio por dia: {self.precio}")

# Clase serivicio de consulta
class ServicioConsulta(Servicio):
    # Constructor del servicio de consulta
    def __init__(self, codigo, nombre, precio, especialidad):
        # Inicializamos los datos de la clase padre
        super().__init__(codigo, nombre, precio)
        # Validamos que la especialidad no este vacia
        if not especialidad:
            raise DatosInvalidosError("La especialidad es obligatoria.")
        # Guardamos la especialidad como atributo
        self.especialidad = especialidad

    # Metodo para calcular el costo del servicio de consulta por horas
    def calcular_costo(self, cantidad=1, descuento=0):
        try:
            # Validamos que la cantidad de horas sea un numero positivo
            if cantidad <= 0:
                raise CalculoInvalidoError("La cantidad de horas debe ser un numero positivo.")
            # Validamos que el descuento sea un numero entre 0 y 100
            if descuento < 0 or descuento > 100:
                raise CalculoInvalidoError("El descuento debe ser un numero entre 0 y 100.")
            subtotal = self.precio * cantidad
            total= subtotal - (subtotal * descuento / 100)
            return total
        except TypeError as error:
           raise CalculoInvalidoError("Los valores del calculo son invalidos.") from error

    # Mostramos la descripción del servicio de consulta
    def mostrar_descripcion(self):
        return(f"Consulta: {self.nombre}, Especialidad: {self.especialidad}, Precio por hora: {self.precio}")