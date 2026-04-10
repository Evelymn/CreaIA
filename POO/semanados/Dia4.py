#Manejo de archivos
#nuestro programas solo corren en la momoria ram, y cuando se termina la momoria se pierde
#si hay fallas en la electricidad se pierde el archivo
# asi que nesecitamos tranferir a algun tipo de almacenamiento

#Interactuar con los archivos

#METODOS DE APERTURA
# #puente entre el programa y el SO
# le dice busque este archivo busque  o cree uno nuevo
# para usar esta funcion se nesecitan obligatoriamente dos argumentos

#MODOS DE APERTURA
    #1. MOOD W write (crea un achivo nuevo. ADVERTENCIA si el archivo ya existian lo destruye y lo sobreescribe de nuevo, si el archivo no existe lo crea)
    #2. modo a append/añadir (Abre un archivo existente y coloca el cursos al final)
    #3.moodo r read (permite ver el contenido, no escribe ni modifica, si no existe el archivo el programa se detiene con un error)





# archivo_prueba = open("archivo.txt", "a")

# # para escribir en mi archivos usamos la funcion write
# archivo_prueba.write("Hoy aprendi a escribir en un archivo")

# # siempre que se abre un archivo hay que cerrar

# archivo_prueba.close()

# #administador de contexto "With open" Tener a alguien que abra y cierra la puerta



#=================================================================================================================
#=================================================================================================================
#=================================================================================================================
with open("C:/CreaIA/POO/semanados/registro.txt", "r") as Dia4:
    contador = 0
    for line in Dia4:
        print(line.strip())
        contador += 1

print(f"Total de usuarios registrados: {contador}")