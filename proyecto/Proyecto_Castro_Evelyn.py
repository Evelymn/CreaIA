print("BIENVENIDO/A A PRODUCTOS AGROINDUSTRIAL S.A")
lotes = [0, 0, 0] #Aca el codigo del producto, las veces que inserten 1, 2, 3 
unidades = [0, 0, 0] #La cantidad de unidade de los productos insertados 
nombres = ["Fertilizante", "Insecticida","Herbicida"] #lista de nombres

#Se le pide al usuarion ingresar el lote, y empizan las validaciones
dato = input("Ingrese el lote").strip() 
#mintras dato sea diferente de Fin el ciclo no termina
while dato != "FIN":
    #validaciones si la longitud del dato es diferente de 5 o el indice 0 del dato no es 1, 2, 3, o el indice 4 del dato no es 1 ni 0
    #Imprimir dato invalido
    if len(dato) != 5 or dato[0] not in ["1","2","3"]or dato[4] not in ["0","1"]:#son lo digitos que acepta 
     #Preguntar si es necesario validar el indice 4
     print("datos invalido", dato) 
#Si se cumple la condion del if entonces declaramos producto que ahora va converti el dato ingresado por el usuario en un int 
#y en indice 0 se -1 
    else:
        producto = int(dato[0]) - 1
        #Aca se declara cantidad y se le pasa el valor del dato convertido en un int desde el indice 1 y 4
        cantidad = int(dato[1:4])
      #conforme el usuario vaya ingresando datos se va ir 1 en productos 
        lotes[producto] += 1
        #aca es lo mismo mientras el usuario ingrese datos, en lotees de le pasa a productos para determinar el total
        unidades[producto] += cantidad
#se termina el while y se repite el mismo procedimiento
    dato = input("Ingrese lote: ").strip()

print("\n")
print(f"{producto:<15}{'Lotes':<15}{'Total unidades':<15}{'Promedio':<15}{'Categoria':<15}")

for indice in range(3):

    if lotes[indice] > 0:
        promedio = unidades[indice] / lotes[indice]
    else:
        promedio = 0

    if promedio <= 99:
        categoria = "Insuficiente"
    elif promedio <= 299:
        categoria = "Regular"
    elif promedio <= 599:
        categoria = "Idoneo"
    else:
        categoria = "Sobreproduccion"

    print(f"{nombres[indice]:<15}{lotes[indice]:<15}{unidades[indice]:<15}{round(promedio,2):<15}{categoria:<15}")
    
print(f"{nombres[indice]:<15}{lotes[indice]:<15}{unidades[indice]:<15}{round(promedio,2):<15}{categoria:<15}")
max_unidades = max(unidades)
indice_max_unidades = unidades.index(max_unidades)

max_lotes = max(lotes)
indice_max_lotes = lotes.index(max_lotes)

total_unidades = sum(unidades)
total_lotes = sum(lotes)

if total_lotes > 0:
    promedio_general = total_unidades / total_lotes
else:
    promedio_general = 0

print("\nResumen:")
print("Producto mayor cantidades:", nombres[indice_max_unidades])
print("Producto con mas lotes:", nombres[indice_max_lotes])
print("Promedio de productos producidos:", round(promedio_general,2))
