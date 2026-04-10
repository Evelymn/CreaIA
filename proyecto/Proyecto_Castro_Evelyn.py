# Proyecto - Productos Agroindustriales S.A
# Nombre: Evelyn Castro

print("<<<<<<<<< BIENVENIDO/A A PRODUCTOS AGROINDUSTRIAL S.A >>>>>>>>")

# Estas listas guardan la info de cada producto
# lotes = cuantas veces se ingreso ese producto
# unidades = cuantas unidades lleva acumuladas
lotes = [0, 0, 0]
unidades = [0, 0, 0]
nombres = ["Fertilizante", "Insecticida", "Herbicida"]

# Pedimos el primer dato
#Usamos Strip para eliminar espacio
dato = input("Ingrese el lote: ").strip()

# Se repite hasta que el usuario escriba FIN
while dato != "FIN":
    
    # Validaciones
    
    # Tiene que tener 5 digitos si o si
    if len(dato) != 5:
        print("dato invalido:", dato, "- Debe tener exactamente 5 digitos")

    # El primer numero solo puede ser 1,2 o 3 (tipo de producto)
    elif dato[0] not in ["1","2","3"]:
        print("dato invalido:", dato, "- Codigo de producto invalido (solo 1, 2 o 3)")

    # El ultimo numero solo puede ser 0 o 1
    elif dato[4] not in ["0","1"]:
        print("dato invalido:", dato, "- El ultimo digito debe ser 0 o 1")

    else:
        
        # Convertimos el producto a indice (porque las listas empiezan en 0)
        producto = int(dato[0]) - 1
        
        # Agarramos la cantidad (posiciones 1,2,3)
        cantidad = int(dato[1:4])
        
        # Sumamos 1 lote al producto correspondiente
        lotes[producto] += 1
        
        # Sumamos las unidades que trae ese lote
        unidades[producto] += cantidad
        
        print("Lote agregado correctamente")
    
    # Pedimos otro dato
    dato = input("Ingrese el lote: ").strip()

print("\n")

# Encabezado de la tabla
print(f"{'Producto':<15}{'Lotes':<15}{'Total unidades':<15}{'Promedio':<15}{'Categoria':<15}")

# Recorremos los 3 productos
for indice in range(3):

    # Si tiene lotes calculamos promedio
    if lotes[indice] > 0:
        promedio = unidades[indice] / lotes[indice]
    else:
        promedio = 0  # para evitar error de dividir entre 0

    # Clasificamos segun el promedio
    if promedio <= 99:
        categoria = "Insuficiente"
    elif promedio <= 299:
        categoria = "Regular"
    elif promedio <= 599:
        categoria = "Idoneo"
    else:
        categoria = "Sobreproduccion"

    # Imprimimos todo bonito en forma de tabla
    print(f"{nombres[indice]:<15}{lotes[indice]:<15}{unidades[indice]:<15}{round(promedio,2):<15}{categoria:<15}")

# ================= RESUMEN =================

# Buscamos el producto con mas unidades
max_unidades = max(unidades)
indice_max_unidades = unidades.index(max_unidades)

# Buscamos el producto con mas lotes
max_lotes = max(lotes)
indice_max_lotes = lotes.index(max_lotes)

# Sumamos todo
total_unidades = sum(unidades)
total_lotes = sum(lotes)

# Promedio general (unidades por lote en general)
if total_lotes > 0:
    promedio_general = total_unidades / total_lotes
else:
    promedio_general = 0

# Mostramos el resumen final
print("\n=================Resumen:=================")
print("Producto mayor cantidades:", nombres[indice_max_unidades])
print("Producto con mas lotes:", nombres[indice_max_lotes])
print("Promedio de productos producidos:", round(promedio_general,2))