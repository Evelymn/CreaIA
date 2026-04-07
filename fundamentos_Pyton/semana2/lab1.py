# ==========================================
# Ejercicio 1: Control de entrada a un torneo
# ==========================================
# aquí va la solución del ejercicio 1
# ==========================================

#El torneo Juvenil tiene una regla: solo pueden entrar 
# participantes con inscripcion confirmada.

# En este ejercicio considero que no es nesesario declarar variables para guardar el nombre y la edad, 
# ya que no se utilizan para nada en el programa, pero si se desea se pueden declarar y utilizar para mostrar un mensaje de bienvenida personalizado.
# nombre = input("Ingrese su nombre:")
# edad = int(input("Ingrese su edad:"))
# inscripcion = input("Tiene inscripcion confirmada? (si/no): ")
# if inscripcion == "si":
#     print("Bienvenido al torneo Juvenil!", nombre)
# else:
#       print("Lo siento, no puedes entrar al torneo Juvenil.")




# ==========================================
# Ejercicio 2 Complete el codigo para que muestre si el celular nesecita cargarse o no. 
# Si la bateria es menor o igual 20, debe indicar que nesecita cargarse 
#En caso contrario, debe indicar que tiene suficiente bateria.
# ==========================================
# aquí va la solución del ejercicio 2

# bateria = int(input("Ingrese el porcentaje de batería: "))
# if bateria <= 20:
#     print("Nesecita cargarse")
# else:
#     print("La batería es suficiente")



#Ejercicio 3. Clasificación de envío
#Enunciado
#Una empresa clasifica paquetes según el peso:
#si pesa menos de 1 kg → Paquete liviano
#si pesa entre 1 y 5 kg inclusive → Paquete estándar
#si pesa más de 5 kg → Paquete pesado
#El programa debe pedir el peso del paquete y mostrar la clasificación.

# print("Bienvenido/a al clasificador de paquetes")
# peso = float(input("Ingrese el peso del paquete en kg: "))
# if peso  <= 1:
#     print("Paquete liviano")
# elif peso > 1 and peso <= 5:
#     print("Paquete estándar")
# else:
#     print("Paquete pesado")



# Ejercicio 4. Corregir código: semáforo
#Enunciado
#El siguiente programa debe actuar como un semaforo simple:
# -si el color es verde, avanzar 
#- Si es amarillo, precaución
# - Si es rojo, detenerse

# color = input("Ingrese el color del semáforo: ")
# if color == "verde":
#   print("Avanzar")
# elif color == "amarillo":
#   print("Precaución")
# else:
#   print("Detenerse")

#Ejercicio 5. Acceso VIP a concierto con compra de bebida
# Un sistema de conciertos desea validar si una
# persona puede entrar al área VIP
# y además comprar una bebida especial.
# El programa debe pedir:
# nombre del cliente
# edad
# tipo de entrada ( general o vip )
# dinero disponible
# precio de la bebida especial

print("=== Sistema de Acceso VIP ===")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
precio_bebida = 15

if edad < 18:
     print("No puede ingresar al área VIP.")

else:
     tipo_entrada = input("Ingrese el tipo de entrada (general/vip): ").strip().lower()

     if tipo_entrada != "vip":
         print("No puede ingresar al área VIP.")

     else:
         print("Acceso VIP aprobado para", nombre)

         desea_bebida = input("¿Desea comprar bebida especial? (si/no): ").strip().lower()

         if desea_bebida == "si":

             dinero_disponible = float(input("Ingrese su dinero disponible: "))

             if dinero_disponible >= precio_bebida:
                 cambio = dinero_disponible - precio_bebida
                 print("Compra de bebida aprobada")
                 print("Cambio:", cambio)
             else:
                 print("No tiene dinero suficiente para comprar la bebida.")

         else:
             print("Disfrute su acceso VIP.")


# Ejercicio 6. Sistema de becas estudiantiles por promedio y condición económica
# Enunciado
# Una institución quiere asignar becas según el rendimiento y la situación económica del estudiante.
# El programa debe pedir:
# nombre del estudiante
# promedio final
# ingreso familiar mensual
# cantidad de materias aprobadas

# print("=== Sistema de Becas Estudiantiles ===")
# nombre = input("Ingrese el nombre completo del estudiante: ")
# promedio_final = float(input("Ingrese el promedio final: "))
# ingreso_familiar = float(input("Ingrese el ingreso familiar mensual: "))
# materias_aprobadas = int(input("Ingrese la cantidad de materias aprobadas: "))
# if promedio_final >= 70 and ingreso_familiar <= 2000 and materias_aprobadas >= 5:
#     print("Beca completa asignada a", nombre)
# else:
#     print("El estudiante no cumple con los requisitos para la beca.")


#Ejercicio 7. Tarifa de hotel con recargo y descuento
# Enunciado
# Un hotel desea calcular el total a pagar según la temporada y la cantidad de noches.
# El programa debe pedir:
# nombre del cliente
# temporada ( alta , media , baja )
# cantidad de noches
# precio base por noche
# si tiene membresía ( si/no )

# print("=== Sistema de Tarifa Hotel ===")

# nombre = input("Nombre: ")
# temporada = input("Temporada (alta/media/baja): ")
# noches = int(input("Cantidad de noches: "))
# precio_base = float(input("Precio base por noche: "))
# membresia = input("¿Tiene membresía? (si/no): ")

# subtotal = precio_base * noches

# if temporada == "alta":
#     subtotal *= 1.20
# elif temporada == "media":
#     subtotal *= 1.10
# elif temporada == "baja":
#     subtotal *= 1.00

# descuento = 0

# if membresia == "si" and noches >= 3:
#     descuento = subtotal * 0.15
# elif membresia == "si" or noches == 2:
#     descuento = subtotal * 0.05

# total_final = subtotal - descuento

# print("Cliente:", nombre)
# print("Subtotal con recargo: {:.2f}".format(subtotal))
# print("Descuento aplicado: {:.2f}".format(descuento))
# print("Total final: {:.2f}".format(total_final))

#Ejercicio 8. Menú de academia con permisos
# Tipo: ejercicio completo con match
# Enunciado
# Una academia virtual tiene este menú:
# 1 o matricular
# 2 o notas
# 3 o certificado
# 4 o salir
# El programa debe pedir:
# opción
# tipo de usuario ( admin , profesor , estudiante )
# promedio del estudiante

# print("=== Sistema Academia Virtual ===")

# opcion = input("Opción: ")
# tipo_usuario = input("Tipo de usuario (admin/profesor/estudiante): ")
# promedio = float(input("Promedio: "))

# match opcion:
#     case "1" | "matricular":
#         if tipo_usuario == "admin" or tipo_usuario == "profesor":
#             print("Matrícula realizada correctamente")
#         else:
#             print("No tiene permisos para matricular")

#     case "2" | "notas":
#         if tipo_usuario == "profesor" or tipo_usuario == "estudiante":
#             print("Acceso a notas permitido")
#         else:
#             print("No tiene permisos para ver notas")

#     case "3" | "certificado":
#         if tipo_usuario == "estudiante" and promedio >= 70:
#             print("Certificado generado correctamente")
#         else:
#             print("No cumple los requisitos para generar certificado")

#     case "4" | "salir":
#         print("Programa finalizado")

#     case _:
#         print("Opción inválida")

# Ejercicio 9. Sistema de tienda gamer con promociones y validación de stock
# Tipo: ejercicio clásico completo
# Enunciado
# Una tienda gamer vende accesorios y desea aplicar promociones según el monto de compra y la membresía del cliente.
# El programa debe pedir:
# nombre del cliente
# nombre del producto
# precio unitario
# cantidad deseada
# cantidad en stock
# si tiene membresía gamer ( si/no )

# print("=== Sistema Tienda Gamer ===")

# nombre = input("Nombre: ")
# producto = input("Producto: ")
# precio_unitario = float(input("Precio unitario: "))
# cantidad_deseada = int(input("Cantidad deseada: "))
# cantidad_stock = int(input("Cantidad en stock: "))
# membresia = input("¿Tiene membresía gamer? (si/no): ").strip().lower()

# if cantidad_deseada > cantidad_stock:
#     print("No se puede realizar la venta, stock insuficiente")
# else:
#     subtotal = precio_unitario * cantidad_deseada
#     descuento = 0

#     if subtotal > 50000 and membresia == "si":
#         descuento = subtotal * 0.20
#     elif subtotal > 30000 or membresia == "si":
#         descuento = subtotal * 0.10

#     total_final = subtotal - descuento

#     print("Venta aprobada")
#     print(f"Subtotal: {subtotal:.2f}")
#     print(f"Descuento: {descuento:.2f}")
#     print(f"Total final: {total_final:.2f}")


# Ejercicio 10. Panel de misiones y cálculo de recompensa
# Tipo: ejercicio completo avanzado
# Enunciado
# Un videojuego tiene un panel de misiones. El jugador puede elegir entre distintos tipos de misión.
# El programa debe pedir:
# nombre del jugador
# clase del jugador ( guerrero , mago , arquero )
# opción de misión
# nivel del jugador
# cantidad de enemigos derrotados

# print("=== Panel de Misiones ===")

# nombre = input("Nombre del jugador: ")
# clase = input("Clase (guerrero/mago/arquero): ")
# opcion = input("Opción de misión (1/bosque, 2/castillo, 3/dragón, 4/salir): ")
# nivel = int(input("Nivel del jugador: "))
# enemigos = int(input("Cantidad de enemigos derrotados: "))

# match opcion:
#     case "1" | "bosque":
#         if nivel >= 1:
#             recompensa_base = enemigos * 10
#             print("Misión bosque completada")
#             print(f"Recompensa base: {recompensa_base}")
#             print(f"Recompensa total: {recompensa_base}")
#         else:
#             print("No cumple el requisito de nivel mínimo (nivel 1 requerido)")

#     case "2" | "castillo":
#         if nivel >= 5:
#             recompensa_base = enemigos * 20
#             bono = 0
#             if clase == "guerrero" or clase == "mago":
#                 bono = 50
#             total = recompensa_base + bono
#             print("Misión castillo completada")
#             print(f"Recompensa base: {recompensa_base}")
#             if bono > 0:
#                 print(f"Bono adicional: {bono}")
#             print(f"Recompensa total: {total}")
#         else:
#             print("No cumple el requisito de nivel mínimo (nivel 5 requerido)")

#     case "3" | "dragón":
#         if nivel >= 10 and (clase == "guerrero" or clase == "arquero"):
#             recompensa_base = enemigos * 50
#             bono = 0
#             if enemigos > 3:
#                 bono = 100
#             total = recompensa_base + bono
#             print("Misión dragón completada")
#             print(f"Recompensa base: {recompensa_base}")
#             if bono > 0:
#                 print(f"Bono adicional: {bono}")
#             print(f"Recompensa total: {total}")
#         else:
#             if nivel < 10:
#                 print("No cumple el requisito de nivel mínimo (nivel 10 requerido)")
#             elif clase != "guerrero" and clase != "arquero":
#                 print("Su clase no puede realizar la misión dragón")

#     case "4" | "salir":
#         print("Programa finalizado")

#     case _:
#         print("Opción inválida")