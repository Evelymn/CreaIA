# Laboratorio listas: El Gestor de Invitados
# Imagina que estás organizando una fiesta VIP. Necesitas un programa que te ayude a controlar quién está en 
# la lista de invitados.
#Instrucciones del Proyecto
# La Lista Principal: Crea una lista vacía llamada lista_invitados.
lista_invitados =[]
# Funciones que debes programar:
# # agregar_invitado(nombre): Debe recibir un nombre y usar el método .append() para guardarlo
def agregar_invitado(nombre):
    lista_invitados.append(nombre)
    print(f"{nombre} \nha sido a gregado a la lista.")

# mostrar_lista(): Debe usar un ciclo for para imprimir todos los nombres que están en la lista actualmente.
def mostrar_lista ():
# buscar_invitado(nombre): Debe verificar si un nombre ya está en la lista.# Si está, devuelve: "El invitado ya está en la lista".
# Si no está, devuelve: "Nombre disponible"
 print("lista de invitados")
 for invitado in lista_invitados:
     print(invitado)
# # eliminar_invitado(nombre): Debe buscar el nombre y usar .remove() para sacarlo de la lista.
# Menú de Usuario:
def buscar_invitado(nombre):
   if nombre in lista_invitados:
      print ("El invitado ya esta en la lista")
   else:
    print("Nombre disponible")
      
# Usa un menú para que el portero del evento pueda:
# 2. Registrar nuevo invitado.
# # 3. Ver lista completa.
# 4. Eliminar a alguien (por si se porta mal).
# 5. Salir.
# Función para eliminar invitado
def eliminar_invitado(nombre):
    if nombre in lista_invitados:
        lista_invitados.remove(nombre)
        print("Invitado eliminado")
    else:
        print("Ese invitado no está en la lista")

# Menú principal
while True:
    print("\n--- MENÚ ---")
    print("1. Agregar invitado")
    print("2. Ver lista")
    print("3. Buscar invitado")
    print("4. Eliminar invitado")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            nombre = input("Ingrese el nombre: ")
            agregar_invitado(nombre)

        case "2":
            mostrar_lista()

        case "3":
            nombre = input("Ingrese el nombre a buscar: ")
            buscar_invitado(nombre)

        case "4":
            nombre = input("Ingrese el nombre a eliminar: ")
            eliminar_invitado(nombre)

        case "5":
            print("Adiós")
            break

        case _:
            print("Opción no válida")