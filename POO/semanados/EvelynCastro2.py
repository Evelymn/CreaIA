class SensorPresion:
#atributos para toda la clase 
    LIMITE_PELIGRO = 200 #psi
#contador global 
    total_lecturas = 0
# la clase debe contar con una función especial 
# encargada de recibirlos datos externos (nombre y presión)    
    def __init__(self, nombre, presion):
        self.nombre = nombre
        self.__presion = 0
        self.presion = presion
# dentro de estemismo bloque es donde debe incrementarse el contador global
# de la plantacada vez que una nueva caldera entra al sistema.
        SensorPresion.total_lecturas += 1


#Además, es fundamental implementar dos funciones gemelas que 
#actúen como la única puerta de acceso al valor de la presión.
    @property
    def presion(self):
     return self.__presion
    @presion.setter
# La segunda función debe actuarcomo un filtro de seguridad; debe recibir
# un nuevo valor, verificar si esválido (que no sea negativo)
    def presion(self, nueva_presion):
       if nueva_presion >= 0:
          self.__presion = nueva_presion
       else:
           print(f"Error:presion inválida para {self.nombre}")
           self.__presion = 0


# Deben desarrollar una sección del código 
# encargadaexclusivamente de la lectura del archivo de texto.
sensores = []
with open("registro.txt", "r") as archivo:    
    while True:
        nombre = archivo.readline().strip()
        
        if nombre == "":
            break
        
        presion = archivo.readline().strip()
        presion = int(presion)
        # Se crea el objeto SensorPresion y se guarda en la lista
        sensor = SensorPresion(nombre, presion)
        sensores.append(sensor)

print("--- SISTEMA DE MONITOREO INDUSTRIAL ---")
print("Leyendo registros de presión...")
with open("alertas.txt", "w") as archivo_alertas:
    archivo_alertas.write("REPORTE DE INCIDENCIAS - CALDERAS CRiTICAS\n")
    archivo_alertas.write("------------------------------------------\n")

    contador = 1

    for sensor in sensores:
        if sensor.presion > SensorPresion.LIMITE_PELIGRO:
            print(f"Analizando: {sensor.nombre} | Estado: Peligro")
            archivo_alertas.write(f"{contador}. {sensor.nombre}\n")
            contador += 1
        else:
            print(f"Analizando: {sensor.nombre} | Estado: Seguro")


print(f"[AUDITORÍA] Se han generado alertas en el archivo 'alertas.txt'")
print(f"[RESUMEN] Total de sensores procesados: {SensorPresion.total_lecturas}")
print("---------------------------------------")