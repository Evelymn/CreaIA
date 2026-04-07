# Acceso a laboratorio de impresión 3D con
# compra de minutos extra
# Un centro tecnológico tiene un laboratorio de impresión 3D al que solo pueden ingresar estudiantes
# autorizados.
# Además, una vez dentro, el estudiante puede comprar minutos extra de uso de impresora mientras
# tenga saldo suficiente.
# El programa debe verificar primero si el estudiante puede ingresar al laboratorio y luego permitirle
# comprar minutos extra de uso.
# El programa debe pedir

# print("Bienvenido al laboratorio de impresión 3D")
# # nombre del estudiante
# nombre = input("Ingrese su nombre: ")
# # edad
# edad = int(input("Ingrese su edad: "))
# # si tiene autorización del profesor (si/no)
# autorizacion = input("¿Tiene autorización del profesor? (si/no): ")
# # saldo disponible
# saldo = float(input("Ingrese su saldo disponible: "))
# # costo de cada paquete de minutos extra
# costo_paquete = float(input("Ingrese el costo de cada paquete de minutos extra: "))
# #Reglas de acceso
# #El estudiante puede entrar al laboratorio únicamente si:
# # tiene 15 años o más
# # y tiene autorización del profesor
# if edad >= 15 and autorizacion.lower() == "si":
#     print(f"Acceso concedido al laboratorio para {nombre}.")
# # Si no cumple estas condiciones, el programa debe indicar que no puede ingresar al laboratorio y
# # finalizar.
# else:
#     print("No puede ingresar al laboratorio. Requisitos no cumplidos.")
#     exit()
# # Compra de minutos extra
# # Si el estudiante puede entrar al laboratorio:
# # El sistema debe permitirle comprar paquetes de minutos extra.

# # Cada paquete cuesta el monto indicado por el programa.
# # Mientras el estudiante tenga saldo suficiente y quiera seguir comprando:
# # se descuenta el costo del paquete
# # se suma un paquete al contador de paquetes comprados
# # Si el saldo ya no alcanza para otro paquete, el sistema debe detener la compra automáticamente.
# paquetes_comprados = 0
# while saldo >= costo_paquete:
#         comprar = input("¿Desea comprar un paquete de minutos extra? (si/no): ")
#         if comprar.lower() == "si":
#             saldo -= costo_paquete
#             paquetes_comprados += 1
#             print(f"Paquete comprado. Saldo restante: {saldo:.2f}")
#         else:
#             break


# # Al final el sistema debe mostrar
# # nombre del estudiante
# # cantidad de paquetes comprados
# # saldo restante

# print(f"Nombre del estudiante: {nombre}")
# print(f"Cantidad de paquetes comprados: {paquetes_comprados}")
# print(f"Saldo restante: {saldo:.2f}")

#==================================================
#=====================================================
    
# Reto 2: Registro de Producto con Tupla

### Enunciado

# La tienda desea representar cada producto como una tupla con tres elementos:

# (nombre, precio, cantidad)

# Realiza lo siguiente:

# 1. Crea una tupla llamada `producto` con los datos:
#    - Nombre: "Arroz"
#    - Precio: 1200
#    - Cantidad: 5
producto = ("Arroz", 1200, 5, "Evelyn")
# 2. Imprime cada elemento usando su índice.

print (producto[0])
print (producto[1])
print (producto[2])
print (producto[3])


# 3. Calcula el valor total del producto (precio × cantidad).
total = producto[1] + producto[2]
print ("Aca se sumo el precio por la cantidad:",total)

# 4. Intenta modificar el precio dentro de la tupla y observa qué ocurre.
# producto [1]=1500
# print (producto[1]) //Dado que las duplas son imutables, 
# no se puede modificar ni un elemento agregdo a la dupla, por lo que se genera un error.
