# # ## El Inventario de la Tienda de Frutas
# # Tienes una lista de listas donde cada sublista representa
# #  un estante. Cada estante tiene cantidades de frutas. Debes calcular
# #  cuántas frutas totales hay, pero solo de aquellas que tengan más de 5 unidades y sean un número par.
# # ```
# # # Lista de estantes con cantidades de productos


# inventario_frutas = [
#     [10, 4, 8],
#     [5, 12, 3],
#     [7, 20, 6]
# ]

# total = 0

# for fila in range(len(inventario_frutas)):
#     for columna in range(len(inventario_frutas[fila])):
        
#         valor = inventario_frutas[fila][columna]
        
#         if valor > 5 and valor % 2 == 0:
#             total += valor

# print("Total de frutas:", total)


# inventario = [
#     [10, 4, 8],
#     [5, 12, 3],
#     [7, 20, 6]
# ]

# # declaramos una variable para guardar la suma total
# total = 0

# # recorremos la matriz (lista de listas)
# for fila in inventario:
#     for cantidad in fila:
        
#         # verificamos si es mayor a 5 y si es par
#         if cantidad > 5 and cantidad % 2 == 0:
            
#             # sumamos al total
#             total += cantidad

# # mostramos el resultado
# print("La cantidad de frutas son:", total)

# ## Ejercicio 2:
# # Eres el encargado de una tienda de abarrotes. Debido a la inflación,
# # todos los productos que cuesten menos de 50 pesos deben subir un 10%. 
# # Los productos que ya cuestan 50 o más se quedan igual. Porteriormente, mostrar los precios finales.
# precios_pasillos = [
#     [10.0, 55.0, 20.0],
#     [45.0, 80.0, 12.0],
#     [100.0, 30.0, 48.0]
# ]

# ### pseudocódigo 
# # * declarar en una variable el 10 porciento de incremento 
# incremteno = 0.10

# # * recorrer la matriz
# for fila in precios_pasillos:
#     for cantidad in fila:
# # * aplicar la condición (if)
# #     si el precio es menor a 50 
#         if cantidad < 50:
    

# #         aplicar el incremento, el cual es multiplicarlo por el 10 porciento 
#            total = cantidad * incremteno
# #         guardar/modificar el valor en la lista(matriz)
#         precios_pasillos = total
# # * mostrar la matriz ya modifica
# print(total)


precios_pasillos = [
    [10.0, 55.0, 20.0],
    [45.0, 80.0, 12.0],
    [100.0, 30.0, 48.0]
]

incremento = 0.10

# recorremos usando índices
for fila in range(len(precios_pasillos)):
    for columna in range(len(precios_pasillos[fila])):
        
        if precios_pasillos[fila][columna] < 50:
            precios_pasillos[fila][columna] *= 1.10  # aumenta 10%

# mostramos la matriz modificada
print(precios_pasillos)