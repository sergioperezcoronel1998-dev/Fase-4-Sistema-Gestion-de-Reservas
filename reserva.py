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
        if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)):
            raise ReservaInvalidaError("La cantidad debe ser un numero.")
        if cantidad <= 0:
            raise ReservaInvalidaError("La cantidad debe ser un numero positivo.")
        # Guardamos los datos como atributos
        self._codigo = codigo.strip()
        self._cliente = cliente
        self._servicio = servicio
        self._cantidad = cantidad
        # Estado de la reserva, por defecto es "pendiente"
        self._estado = "pendiente"

    # Metodo confirmacion de la reserva
    def confirmar_reserva(self):
        # Validamos que la reserva este en estado pendiente antes de confirmarla
        if self._estado != "pendiente":
            raise OperacionNoPermitidaError("La reserva no puede ser confirmada, debe estar en estado pendiente.")
        # Cambiamos el estado de la reserva a confirmada
        self._estado = "confirmada"

    # Metodo cancelacion de la reserva
    def cancelar_reserva(self):
        # Verificamos que la reserva no este ya cancelada antes de cancelarla
        if self._estado == "cancelada":
            raise OperacionNoPermitidaError("La reserva ya esta cancelada.")
        # Cambiamos el estado de la reserva a cancelada
        self._estado = "cancelada"

    # Metodo para procesar una reserva
    def procesar(self):
        # Verificamos que la reserva este en estado confirmada antes de procesarla
        if self._estado != "confirmada":
            raise OperacionNoPermitidaError("La reserva no puede ser procesada, debe estar en estado confirmada.")
        # Calculamos costo de la reserva
        total = self.calcular_total()
        # Actualizamos el estado de la reserva a procesada y registramos el evento
        self._estado = "procesada"
        # Devolvemos el costo total de la reserva procesada
        return total      
        

    
    # Metodo calcular el costo total de la reserva
    def calcular_total(self, descuento=0):
        #verificamos que la reserva no este cancelada antes de calcular el costo total
        if self._estado == "cancelada":
            raise OperacionNoPermitidaError("No se puede calcular el costo de una reserva cancelada.")
        # Calculamos el costo total de la reserva utilizando el metodo calcular_costo del servicio
        return self._servicio.calcular_costo(self._cantidad, descuento)

    # Metodo mostrar la informacion de la reserva
    def mostrar_informacion(self):
        return(f"Codigo: {self._codigo}, Cliente: {self._cliente.nombre}, Servicio: {self._servicio.nombre}, Cantidad: {self._cantidad}, Estado: {self._estado}")