#  Pilas
# Una pila sigue el principio LIFO: el último elemento en entrar es el primero en salir.

# append() permite apilar elementos al final de la lista.
# pop() elimina y devuelve el último elemento agregado.
# En Estructura de Datos 1, las pilas ayudan a modelar deshacer acciones, llamadas a funciones y validaciones.
# pila = []

# def apilar(x):
#     pila.append(x)

# def desapilar():
#     if pila:
#         return pila.pop()
#     return None

# def mostrar_tope():
#     if pila:
#         return pila[-1]
#     return None

# apilar(10)
# apilar(20)
# apilar(30)
# apilar(40)
# apilar(50)
# apilar(60)
# apilar(70)

# print("Pila inicial:", pila)


# while len(pila) > 1:
#     desapilar()

# print("Pila final:", pila)
# print("Tope actual:", mostrar_tope())

# 2. Arreglos
# En Python, para introducir la idea de arreglo podemos usar listas: 
# una estructura ordenada que permite guardar varios datos y acceder a ellos por posición.

# Cada dato ocupa una posición o índice.
# El primer índice es 0.
# Los arreglos permiten almacenar y recorrer información del mismo tipo o relacionada.
# Código base resuelto
# Reto práctico
# A partir del arreglo anterior, agrega los valores 25, 30 y 35. Luego muestra en pantalla 
# cuántos elementos tiene el arreglo y cuál es el elemento de la posición 4.

# numeros = [5, 8, 12, 20]

# print("Arreglo completo:", numeros)
# print("Primer elemento:", numeros[0])
# print("Último elemento:", numeros[3])

# numeros.append(25)
# numeros.append(30)
# numeros.append(35)


# for numero in numeros:
#     print(numero)

# print("Cantidad de elementos:", len(numeros))


# print("Elemento en posición 4:", numeros[4])


# Matrices
# Una matriz puede representarse en Python como una lista de listas. 
# Cada fila contiene varios elementos y juntas forman una estructura de dos dimensiones.

# Se accede con dos índices: fila y columna.
# Permite modelar tablas, tableros, calificaciones o coordenadas.
# Es una base importante para algoritmos más avanzados.
# Reto práctico
# Cambia el valor 9 por 99 y luego agrega una nueva fila [10, 11, 12]. 
# Finalmente muestra la matriz completa.
 
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matriz[2][2] = 99

# matriz.append([10, 11, 12])

# print("Matriz completa:")

# for fila in matriz:
#     print(fila)

# print("Elemento central:", matriz[1][1])