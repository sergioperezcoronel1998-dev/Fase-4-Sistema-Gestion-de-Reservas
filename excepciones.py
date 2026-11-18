# Excepciones del sistema
# Clase principal para manejar excepciones y errores del sistema
# Hereda de la clase Exception de Python

class ErrorSistema(Exception):
    pass

# Error datos ingresados no validos
class DatosInvalidosError(ErrorSistema):
    pass

# Error cliente no encontrado
class ClienteNoEncontradoError(ErrorSistema):
    pass    

# Error servicio no disponible  
class ServicioNoDisponibleError(ErrorSistema):
    pass

# Error reserva datos incorrectos   
class  ReservaInvalidaError(ErrorSistema):
    pass

# Error reserva no encontrada
class ReservaNoEncontradaError(ErrorSistema):
    pass

# Error intento de operación no permitida
class OperacionNoPermitidaError(ErrorSistema):
    pass

# Error problema en un calculo
class CalculoInvalidoError(ErrorSistema):
    pass    
