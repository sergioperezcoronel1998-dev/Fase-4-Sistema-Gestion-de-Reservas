# Gestion de reservas 
# Importamos las excepciones necesarias para esta parte definidas en excepciones.py

from excepciones import DatosInvalidosError, ReservaInvalidaError, OperacionNoPermitidaError

# Clase para representar una reserva del sistema
class Reserva:
    # Constructor de la clase Reserva
    def __init__(self, codigo, cliente, servicio, cantidad):
        # Validamos que los datos no esten vacios y que la cantidad sea un numero positivo
        if not codigo or not cliente or not servicio:
            raise DatosInvalidosError("El codigo, cliente y servicio son obligatorios.")
        if cantidad <= 0:
            raise ReservaInvalidaError("La cantidad debe ser un numero positivo.")
        # Guardamos los datos como atributos
        self.codigo = codigo
        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad
        # Estado de la reserva, por defecto es "pendiente"
        self.estado = "pendiente"

    # Metodo confirmacion de la reserva
    def confirmar_reserva(self):
        # Validamos que la reserva este en estado pendiente antes de confirmarla
        if self.estado != "pendiente":
            raise OperacionNoPermitidaError("La reserva no puede ser confirmada, debe estar en estado pendiente.")
        # Cambiamos el estado de la reserva a confirmada
        self.estado = "confirmada"

    # Metodo cancelacion de la reserva
    def cancelar_reserva(self):
        # Verificamos que la reserva no este ya cancelada antes de cancelarla
        if self.estado == "cancelada":
            raise OperacionNoPermitidaError("La reserva ya esta cancelada.")
        # Cambiamos el estado de la reserva a cancelada
        self.estado = "cancelada"
    
    # Metodo calcular el costo total de la reserva
    def calcular_costo_total(self, descuento=0):
        #verificamos que la reserva no este cancelada antes de calcular el costo total
        if self.estado == "cancelada":
            raise OperacionNoPermitidaError("No se puede calcular el costo de una reserva cancelada.")
        # Calculamos el costo total de la reserva utilizando el metodo calcular_costo del servicio
        return self.servicio.calcular_costo(self.cantidad, descuento)

    # Metodo mostrar la informacion de la reserva
    def mostrar_informacion(self):
        return(f"Codigo: {self.codigo}, Cliente: {self.cliente.nombre}, Servicio: {self.servicio.nombre}, Cantidad: {self.cantidad}, Estado: {self.estado}")