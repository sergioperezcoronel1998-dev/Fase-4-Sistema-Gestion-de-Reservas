# Gestion y registro del sistema

# Importamos las excepciones necesarias para esta parte definidas en excepciones.py

from excepciones import (DatosInvalidosError, ClienteNoEncontradoError, ServicioNoDisponibleError, ReservaNoEncontradaError)

# Clase encargada de administrar la informacion

class Registro:
    # Constructor de la clase Registro
    def __init__(self):
        # Lista para almacenar datos en memoria
        self.clientes = []
        self.servicios = []
        self.reservas = []
        # Nombre del archivo donde se guardara la informacion
        self.archivo = "registro.log"

    # Metodo para guardar eventos en el archivo de registro
    def registrar_evento(self, mensaje):
        with open(self.archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"Evento: {mensaje}\n")

    # Metodo para guardar errores en el archivo de registro
    def registrar_error(self, mensaje):
        with open(self.archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"Error: {mensaje}\n")

    # Metodo para agregar un cliente al sistema
    def agregar_cliente(self, cliente):
        # Verificamos que el cliente no este registraddo previamente antes de agregarlo
        for existente in self.clientes:
            if existente.identificacion == cliente.identificacion:
                raise DatosInvalidosError("El cliente ya esta registrado en el sistema.")
        # Agregamos el cliente a la lista de clientes y registramos el evento
        self.clientes.append(cliente)
        # Registramos el evento de agregar un cliente en el archivo de registro
        self.registrar_evento(f"Cliente agregado: {cliente.nombre}")

    # Metodo buscar cliente por identificacion
    def buscar_cliente(self, identificacion):
        # Recorremos la lista de clientes
        for cliente in self.clientes:
            # Comparamos la identificacion del cliente con la proporcionada
            if cliente.identificacion == identificacion:
                return cliente
        # Si no se encuentra el cliente, generamos una excepcion de ClienteNoEncontradoError
        raise ClienteNoEncontradoError("Cliente no encontrado en el sistema.")
    
    # Metodo para agregar un servicio al sistema
    def agregar_servicio(self, servicio):
        # Verificamos que el servicio no este registrado previamente antes de agregarlo
        for existente in self.servicios:
            if existente._codigo == servicio._codigo:
                raise DatosInvalidosError("El servicio ya esta registrado en el sistema.")
        # Agregamos el servicio a la lista de servicios 
        self.servicios.append(servicio)
        # Guardamos el evento de agregar un servicio en el archivo de registro
        self.registrar_evento(f"Servicio agregado: {servicio.nombre}")

    # Metodo buscar servicio por codigo
    def buscar_servicio(self, codigo):
        # Recorremos la lista de servicios
        for servicio in self.servicios:
            # Comparamos el codigo del servicio con el proporcionado
            if servicio._codigo == codigo:
                return servicio
        # Si no se encuentra el servicio, generamos una excepcion de ServicioNoDisponibleError
        raise ServicioNoDisponibleError("Servicio no disponible en el sistema.")

    # Metodo para agregar una reserva al sistema
    def agregar_reserva(self, reserva):
        # Verificamos que la reserva no este registrada previamente antes de agregarla
        for existente in self.reservas:
            if existente._codigo == reserva._codigo:
                raise DatosInvalidosError("La reserva ya esta registrada en el sistema.")
        # Agregamos la reserva a la lista de reservas
        self.reservas.append(reserva)
        # Guardamos el evento de agregar una reserva en el archivo de registro
        self.registrar_evento(f"Reserva agregada: {reserva._codigo}")

    # Metodo buscar reserva por codigo
    def buscar_reserva(self, codigo):
        # Recorremos la lista de reservas
        for reserva in self.reservas:
            # Comparamos el codigo de la reserva con el proporcionado
            if reserva._codigo == codigo:
                return reserva
        # Si no se encuentra la reserva, generamos una excepcion de ReservaNoEncontradaError
        raise ReservaNoEncontradaError("Reserva no encontrada en el sistema.")

    # Metodo mostrar todas las reservas del sistema
    def mostrar_reservas(self):
        # Verificamos si hay reservas registradas en el sistema
        if not self.reservas:
            return "No hay reservas registradas en el sistema."    
        # Creamos una lista para almacenar la informacion de las reservas
        informacion_reservas = []
        # Recorremos la lista de reservas
        for reserva in self.reservas:
            # Agregamos la informacion de cada reserva a la lista
            informacion_reservas.append(reserva.mostrar_informacion())
        # Retornamos la lista con la informacion de las reservas
        return informacion_reservas
    