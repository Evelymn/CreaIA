# class Empleado:
#     pass

# empleado_1 = Empleado()
# empleado_2 = Empleado()
# empleado_3 = Empleado()

# empleado_1.nombre = "Eliceo"
# empleado_1.cargo = "Gerente"
# empleado_1.salario = 2300

# empleado_2.nombre = "Lomary"
# empleado_2.cargo = "Secretaria"
# empleado_2.salario = 1500

# empleado_3.nombre = "Yeraldy"
# empleado_3.cargo = "Supervisora"
# empleado_3.salario = 4000

        
# print(f"{empleado_1.nombre}")
#======================================================================================
#======================================================================================
# class Empleado():
#     def saludar_cliente(self):

#         print(f"Hola me llamo {self.nombre}, bienvenido")

# cajero = Empleado()
# cajero.nombre = "Juan"
# cajero.saludar_cliente()

# caja registradora
# 1. crear una clase caja registradora
# 2. dentro de nuestra clase, vamos a crear 2 metodos: 
#    - mostrar_dinero_actual: imprimir el dinero actual
#    - procesar_venta(): todas nuestras ventas son de 500. añadir a nuestro dinero actual los 500 de ganancia
#======================================================================================
#======================================================================================
# 3. fabricar una caja registradora
# 4. le asignamos dinero inicial
# 5. ponemos a trabajar nuestra caja registradora
#    - muestre el dinero 
#    - procese una venta
#    - muestre el dinero

# class CajaRegistradora:
#     def mostrar_dinero_actual(self):
#         print(f"Dinero actual: {self.dineroinicial}")
    
#     def procesar_ventas(self):
#             self.dineroinicial = self.dineroinicial + 500
#             print("Venta Procesada")

# caja_registradora = CajaRegistradora()
# caja_registradora.dineroinicial = 1300


# caja_registradora.mostrar_dinero_actual()
# caja_registradora.procesar_ventas()
# caja_registradora.mostrar_dinero_actual()
#======================================================================================
#======================================================================================
#======================================================================================
# En nuestra tienda, los cliente VIP tienen una tarjeta de puntos.
# 1. crea una clase llamada TarjetaVIP
# 2. dentro de la clase, crea un metodo llamado mostrar_puntos()
#  que imprima: "sus puntos acumulados son: {puntos del objeto}"
# 3. crea un segundo metodo llamado sumar_puntos(), que le sume 50 puntos al atributo del objeto e imprima "se han sumado 50 puntos por su compra"
# 4. fuera de la clase (en el programa principal), instancia un objeto llamado tarjeta_carlos.
# 5. asignele un atributo puntos con el valor inicial de 100
# 6. llama al metodo para mostrar los puntos, luego llama al metodo para sumar,
#  y finalmente vuelve a mostrar los puntos para comprobar que la matematica funcionó

# class TarjetaVIP():
#     def mostrar_puntos(self):
#         print(f"Sus puntos acumulados son:{self.puntos} ")
       

#     def sumar_puntos(self):
#         self.puntos = self.puntos + 50
#         print(f"Se han sumado 50 puntos por su compra")
# tarjeta_carlos = TarjetaVIP()
# tarjeta_carlos.puntos = 100

# tarjeta_carlos.mostrar_puntos()
# tarjeta_carlos.sumar_puntos()
# tarjeta_carlos.mostrar_puntos()

#==========================================================================

# class CajaRegistradora():

#     def cobrar_producto(self):
#         precio_producto = float(input("Ingrese el precio del producto: "))
#         self.dinero_acumulado = self.dinero_acumulado + precio_producto
#         print(f"Cobro exitoso. llevamos acumulado {self.dinero_acumulado}")

#     def imprimir_cierre_turno(self):
#         print(f"Cajero {self.cajero_asignado}")
#         print(f"Total recaudado: {self.dinero_acumulado}")

    

# caja_express = CajaRegistradora()
# caja_express.cajero_asignado = "Evelyn"
# caja_express.dinero_acumulado = 0

# caja_express.cobrar_producto()
# caja_express.cobrar_producto()
# caja_express.imprimir_cierre_turno()
# Reto integrador: El Simulador de Mascota Virtual

# Vas a crear un programa que simule una mascota digital (como un Tamagotchi). 
# La mascota tendrá un nombre y un nivel de energía inicial. El usuario podrá interactuar con 
# ella para alimentarla (sube energía) o hacerla jugar (baja energía). El programa debe detenerse 
# si la mascota se queda sin energía o si el usuario decide salir.



# 1. Crea una plantilla llamada Mascota.
# 2. Al nacer, la mascota debe recibir un nombre y fijar su energía en 100 puntos.
# 3. Acción de alimentar: Crea una función interna que sume 20 puntos de energía cada vez que se use,
# pero que no permita exceder el máximo de 100.
# 4. Acción de jugar: Crea una función que reste 30 puntos de energía. Importante: Usa una condición 
# para verificar si tiene suficiente energía antes de jugar; si tiene menos de 30, debe avisar que está muy cansada.
# 5. Implementa un bucle que se repita mientras la energía sea mayor a 0.
# 6. Dentro del bucle, pregunta al usuario qué acción desea realizar (1. Alimentar, 2. Jugar, 3. Salir).
# 7. Según lo que el usuario escriba, llama al método correspondiente de tu mascota.
