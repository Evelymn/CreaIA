# Ejercicio Practico 
# el gerente necesita que la computadora entienda tres conceptos 
# nuevos que antes no conocia en la sucursal 
# 1 un cajero
# 2 un inventario
# 3 un VehiculoReparto
# paso uno crear el plano arquitectonico (Clase) de cada uno usando la palabra 
# pass

# class Cajero:
#  pass

# paso 2: fabricar dos objetos reales a partir de la clase Cajero
# imprimelos en la pantalla 
 
# paso 3: Una tienda normalmente tiene un solo registro central. Fabrica un (1) solo objeto de la clase 
# invetario y guardalo en la variable inventario_principal. Imprimelo en pantalla
# Paso 4 Finalmente, fabrica una flota entera de tres vehiculos



# Ejericio 2
# class FacturaEmitida:
#     pass

# class TerminalDePago:
#     pass

# factura_001 = FacturaEmitida()
# factura_002 = FacturaEmitida()

# terminal_principal = TerminalDePago()

# print(type(terminal_principal))

# print(id(factura_001))
# print(id(factura_002))

# print(id(factura_001) == id(factura_002))

# ===========================================
# ===========================================
# Ejercicio 3 Gestios de Flota y Control de Capacidad
class Camion:
    pass    

class CentroLogistico:
    pass

camion1 = Camion()
camion2 = Camion()
camion3 = Camion()
camion4 = Camion()
camion5 = Camion()

garage_principal = [
    camion1,  
    camion2,
    camion3,  
    camion4,  
    camion5 
]

# Total de camiones 
total_camiones = len(garage_principal)

impuesto_total = total_camiones * 500

# Mostrar IDs correctos
for camion in garage_principal:
    print(id(camion))

# Condición
if total_camiones > 4:
    print("Capacidad excedida. Debes mover camiones a otra sucursal")
else:
    print("Capacidad óptima")