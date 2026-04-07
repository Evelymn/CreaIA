#Ejercicio Estudiantes
##1.Funcion simple (sin parametros ni retorno   )
#Bienvenidos al sistema de ventas
#esperamos que tengas un buen dia 

# def bienvenida():
#     print("Bienvenido al sistema de ventas")
#     print("Esperamos que tengas un buen dia")

# bienvenida()


# ## 2. función con parámetros
# Un sistema de gimnasio desea saludar a cada cliente por su nombre.

# Cree una función llamada `saludar_cliente(nombre)` que reciba el
#  nombre del cliente como parámetro e imprima el siguiente mensaje:
# ```
# Hola Diego, bienvenido al gimnasio
# ```


# nombre = input("Ingrese su nombre: ")

# def saludar_cliente(nombre): #Declaracion de la variable nombre como parametro de la funcion
#     print(f"Hola {nombre}, bienvenido al gimnasio")

# saludar_cliente(nombre) ##inovocacion de la funcion con el parametro nombre



# ## 3. función con retorno 
# Un supermercado desea calcular el precio final de una compra.
# Cree una función llamada `calcular_total(precio, cantidad)` que:
# * Reciba el precio de un producto.
# * Reciba la cantidad comprada.
# * Calcule el total a pagar.
# * Devuelva el resultado al programa principal.

# El programa debe mostrar el total final.

# def calcular_total(precio, cantidad):
#     total = precio * cantidad
#     return total

# precio = float(input("Ingrese el precio del producto: "))
# cantidad = int(input("Ingrese la cantidad comprada: "))

# total = calcular_total(precio, cantidad)
# print(f"total a pagar {total}")

#=================================================================================
#==============================================================================
## 4. ejercicio integrador
# Una sala de videojuegos vende fichas para poder jugar en las máquinas.
# Cada ficha cuesta 500 colones.

# El sistema debe permitir que varios clientes compren fichas durante el día.
# El programa debe:

# 1. Mostrar un menú con las siguientes opciones:
# ```
# 1 - Comprar fichas
# 2 - Salir
# ```                 
# * pedir el nombre del cliente
# * pedir cuánto dinero tiene
# * calcular cuántas fichas puede comprar
# * calcular cuánto dinero le sobra

# 3. Reglas del sistema:
# * si el cliente no tiene dinero suficiente para al menos una ficha, el sistema debe indicarlo
# * si tiene suficiente dinero, se debe mostrar:
# ```
# Cantidad de fichas que puede comprar
# Dinero de vuelto
# ```

# 4. El programa debe repetirse usando un ciclo while hasta que el usuario elija salir.
# 5. El cálculo de fichas debe realizarse mediante una función con parámetros y retorno.

# def calcular_fichas(dinero, precio):
#     fichas = dinero // precio
#     vuelto = dinero % precio
#     return fichas, vuelto

# precio_ficha = 500

# while True:

#     print("\n1 - Comprar fichas")
#     print("2 - Salir")

#     opcion = input("Seleccione una opción: ")

#     match opcion:

#         case "1":

#             nombre_cliente = input("Ingrese su nombre: ")
#             dinero_disponible = int(input("Ingrese cuánto dinero tiene: "))

#             if dinero_disponible < precio_ficha:
#                 print("No tiene dinero suficiente para comprar una ficha")

#             else:
#                 fichas, vuelto = calcular_fichas(dinero_disponible, precio_ficha)

#                 print(f"\nCliente: {nombre_cliente}")
#                 print(f"Cantidad de fichas que puede comprar: {fichas}")
#                 print(f"Dinero de vuelto: {vuelto}")

#         case "2":
#             print("Gracias por usar el sistema")
#             break

#         case _: #si el usuario ingresa un valor que no aparece en las opciones por default muestra este case 
#             print("Opción no válida")

#=============================================================================================================
#=============================================================================================================
# ## Retos
# ### Reto 1: El Verificador de Edades
# * **Instrucción:** Crea una función llamada `es_mayor_de_edad` que reciba un parámetro llamado `edad`. 
#     * Dentro de la función, evalúa si la edad es mayor o igual a 18.
#     * Si lo es, la función debe DEVOLVER (`return`) el valor booleano `True`. De lo contrario, devolver `False`.
#     * En el programa principal, pide la edad al usuario, llama a la función, y usa el resultado devuelto en un `if`
# para imprimir "Puedes comprar alcohol" o "Venta denegada".

# def es_mayor_edad(edad):
#     if edad>=18:
#         return True
#     else:
#      return False
# edad =  int(input(" Ingrese su edad: "))
# resultado = es_mayor_edad(edad)
# if resultado:
#    print("Puedes comprar alcohol")
# else:
#       print("Venta Denegada")
   


# ### Reto 2: Calculadora de Descuentos
# * **Instrucción:** Crea una función llamada `aplicar_descuento`
# que reciba dos parámetros: `precio` y `porcentaje_descuento`. La función debe calcular cuánto dinero se 
# descuenta, restarlo al precio original y usar `return` para devolver el nuevo precio. Pruébala con un artículo 
# de 5000 colones y un descuento del 20%
def aplicar_descuento(precio, porcentaje_descuento):
    calcular_descuento = precio * porcentaje_descuento
    nuevo_precio = precio - calcular_descuento
    return nuevo_precio

articulo = 5000
porcentaje_descuento = 0.20

resultado = aplicar_descuento(articulo, porcentaje_descuento)

print(f"El precio con descuento es: {resultado}")


