# Sistema integral- Gestion de clientes, servicios y reservas
# Importamos las clases necesarias para el funcionamiento del sistema
from entidades import Cliente
from servicio import ServicioHabitacion, ServicioEquipo, ServicioConsulta
from reserva import Reserva
from registro import Registro

# Importamos las excepciones personalizadas para el manejo de errores
from excepciones import (DatosInvalidosError, CalculoInvalidoError, OperacionNoPermitidaError, ReservaInvalidaError, ServicioNoDisponibleError, ClienteNoEncontradoError)

# Creamos el objeto de registro para manejar la informacion del sistema
sistema = Registro()

# Registramo el primer cliente
try:
    cliente1 = Cliente("12345", "Carlos Perez", "carlos@gmail.com")
    sistema.agregar_cliente(cliente1)
except DatosInvalidosError as error:    
    print (f"Error al registrar el cliente: {error}")
    sistema.registrar_error(str(error))

# Intento de registro de cliente con datos invalidos
try: 
    cliente_invalido = Cliente ("", "Pedro", "pedro@gmail.com")
    sistema.agregar_cliente(cliente_invalido)
except DatosInvalidosError as error:
    print(f"Error al registrar el cliente: {error}")
    sistema.registrar_error(str(error))

# Registramos servicio de Habitaciones 
try:
    servicio1 = ServicioHabitacion("S001", "Habitacion sencilla", 120000, 2)
    sistema.agregar_servicio(servicio1)
except DatosInvalidosError as error:
    print(f"Error al registrar el servicio: {error}")
    sistema.registrar_error(str(error))
else:
    print("Servicio de habitaciones registrado correctamente.")

# Registramos un servicio de alquiler de equipos
try:
    servicio2 = ServicioEquipo("S002", "Alquiler de proyector", 50000, "Proyector")
    sistema.agregar_servicio(servicio2)
except DatosInvalidosError as error:
    print(f"Error al registrar el servicio: {error}")
    sistema.registrar_error(str(error))
else:
    print("Servicio de alquiler de equipos registrado correctamente.")

# Registramos un servicio de consulta especializada
try:
    servicio3 = ServicioConsulta("S003", "Asesoria tecnica", 80000, "Sistemas")
    sistema.agregar_servicio(servicio3)
except DatosInvalidosError as error:
    print(f"Error al registrar el servicio: {error}")
    sistema.registrar_error(str(error))
else:
    print("Servicio de consulta especializada registrado correctamente.")

# Intentamos registrar un servicio con datos invalidos
try:
    servicio_invalido = ServicioHabitacion("S004", " ", 0, 2)
    sistema.agregar_servicio(servicio_invalido)
except DatosInvalidosError as error:
    print(f"Error al registrar el servicio: {error}")
    sistema.registrar_error(str(error))

# Creamos y registramos la primera reserva
try:
    reserva1 = Reserva("R001", cliente1, servicio1, 2)
    sistema.agregar_reserva(reserva1)
except DatosInvalidosError as error:
    print(f"Error al crear la reserva: {error}")
    sistema.registrar_error(str(error))
except Exception as error:
    print(f"Error inesperado al crear la reserva: {error}")
    sistema.registrar_error(str(error))
else:
    print("Reserva creada correctamente.")

# Intentamos crear una reserva con una cantidad invalida
try:
    reserva_invalida = Reserva("R002", cliente1, servicio1, 0)
    sistema.agregar_reserva(reserva_invalida)
except ReservaInvalidaError as error:
    print(f"Error al crear la reserva: {error}")
    sistema.registrar_error(str(error))

# Confirmamos la primera reserva
try:
    reserva1.confirmar_reserva()
    sistema.registrar_evento("Reserva R001 confirmada.")
except OperacionNoPermitidaError as error:
    print(f"Error al confirmar la reserva: {error}")
    sistema.registrar_error(str(error))
else:
    print("Reserva confirmada correctamente.")

# Procesamos la primera reserva y calculamos su costo
try:
    total = reserva1.procesar()
    print(f"El costo total de la reserva es: ${total:,.0f}")
    sistema.registrar_evento("Reserva R001 procesada correctamente.")
except (OperacionNoPermitidaError, CalculoInvalidoError) as error:
    print(f"Error al procesar la reserva: {error}")
    sistema.registrar_error(str(error))
else:
    print("Reserva procesada correctamente.")

# Intentamos cancelar una reserva que ya fue procesada
try:
    reserva1.cancelar_reserva()
except OperacionNoPermitidaError as error:
    print(f"Operacion no permitida: {error}")
    sistema.registrar_error(str(error))

# Mostramos las reservas registradas en el sistema
print("\n--- RESERVAS REGISTRADAS ---")
reservas = sistema.mostrar_reservas()
for informacion in reservas:
    print(informacion)

# Probamos la busqueda de un cliente
try:
    cliente_encontrado = sistema.buscar_cliente("12345")
    print(f"Cliente encontrado: {cliente_encontrado.nombre}")
except Exception as error:
    print(f"Error al buscar el cliente: {error}")
    sistema.registrar_error(str(error))
finally:
    print("Busqueda de cliente finalizada.")

# Intentamos buscar un servicio que no existe
try:
    sistema.buscar_servicio("S006")
except ServicioNoDisponibleError as error:
    print(f"Error al buscar el servicio: {error}")
    sistema.registrar_error(str(error))

# Intentamos buscar un cliente que no existe
try:
    sistema.buscar_cliente("989785")
except ClienteNoEncontradoError as error:
    print(f"Error al buscar el cliente: {error}")
    sistema.registrar_error(str(error))