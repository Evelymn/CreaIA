#Diccionario 
#le ponemos una etiqueta con nombre (clave)
# a la caja  y dentro guardamos (clave)


producto = {
     "Nombre": "Arroz",
     "Precio": 1200,
     "Cantidad": 5
 }

print(producto["Nombre"])
print(producto["Precio"])


total = producto ["Cantidad"]* producto ["Precio"]
print(f"Total de los produtos son:{total}")


print(producto)
 # modifcar valores en un diccionario
producto["Precio"] = 1500

# #actualizar precio despues de una venta

producto["Cantidad"] = producto["Cantidad"]-1
print(producto)

##Ejercicio crear diccionario llamado cliente con datos 
# nombre
# edad
# ciudad

#imprimir cada valor utilizando la variable correcta
#  porsteriormente modificar el diccionario
#cambiar la ciudad.
# aumentar la edad en 1

# cliente = {
#     "nombre" : "Juan",
#     "edad": 23,
#     "ciudad" : "Canada"
# }
# print(cliente["nombre"])
# print(cliente["edad"])
# print(cliente["ciudad"])

# cliente["ciudad"] = "Brasil"
# cliente["edad"] = cliente["edad"]+1
# print(cliente)

#agregr un elemento a mi diccionario
# producto["categoria"]="Granos"
# print(producto)

# for clave in producto:
#     print{f"clave{clave}:valor:{producto[clave]}"}

