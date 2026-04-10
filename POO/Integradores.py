class DronVigilacia:

    def __init__(self, nombre_dron, modelo_dron):
        self.nombre_dron = nombre_dron
        self.modelo_dron = modelo_dron
        self.bateria = 100
        self.estado_vuelo = "En Tierra"
 
    def despegue(self):
        if self.estado_vuelo == "En Tierra":
            self.estado_vuelo = "En vuelo"
            print("¡Despegue exitoso! El dron ahora está en el aire.")
        else:
            print("[ERROR]: El dron ya está en vuelo.")

    def patrullaje(self):
        if self.estado_vuelo == "En Tierra":
            print("[ERROR]: El dron no puede patrullar si aún está en tierra.")
            return

        self.bateria -= 30
        print(f"Patrullaje completado. Consumo: 30%. Batería restante: {self.bateria}%.")

        if self.bateria < 10:
            self.estado_vuelo = "En Tierra"

    def recarga(self):
        self.bateria = 100
        print("Recarga completada. Batería al 100%.")


# PROGRAMA PRINCIPAL 

print("===INICIANDO SISTEMA SKYWATCH ===")

nombre = input("Ingrese nombre del dron: ")
modelo = input("Ingrese modelo del dron: ")

dron1 = DronVigilacia(nombre, modelo)

print(f"\n--- ESTADO ACTUAL: {dron1.nombre_dron} [{dron1.modelo_dron}] ---")
print(f"Batería: {dron1.bateria}% | Estado: {dron1.estado_vuelo}")

opcion = ""

while opcion != "4":

    opcion = input("\n¿Qué acción desea realizar? (1. Despegar / 2. Patrullar / 3. Recargar / 4. Salir): ")

    if opcion == "1":
        dron1.despegue()

    elif opcion == "2":
        dron1.patrullaje()

    elif opcion == "3":
        dron1.recarga()

    elif opcion == "4":
        print("Apagando sistema...")

    else:
        print("Opción inválida")

    if opcion != "4":
        print(f"\n--- ESTADO ACTUAL: {dron1.nombre_dron} [{dron1.modelo_dron}] ---")
        print(f"Batería: {dron1.bateria}% | Estado: {dron1.estado_vuelo}")




#============================================================================================
#============================================================================================


class PlantaEspacial:

    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.hidratacion = 100
        self.salud = 100
        self.estado = "Saludable"

    # Regar planta
    def regar(self):
        if self.estado == "Marchita":
            print("La planta no puede ser regada.")
            return

        self.hidratacion += 15
        if self.hidratacion > 100:
            self.hidratacion = 100

        print(f"Suministrando agua... Hidratación actual: {self.hidratacion}%.")

    # Simular paso del día
    def pasar_dia(self):
        if self.estado == "Marchita":
            print("La planta ya está marchita.")
            return

        self.hidratacion -= 20
        if self.hidratacion < 0:
            self.hidratacion = 0

        print(f"Ha pasado un día en Marte. La hidratación bajó a {self.hidratacion}%.")

        # Regla crítica
        if self.hidratacion < 30:
            self.salud -= 40
            print(f"¡ALERTA! Hidratación crítica. La salud de {self.nombre} ha sufrido daños.")

            if self.salud < 0:
                self.salud = 0

        # Cambio de estado
        if self.salud <= 0:
            self.estado = "Marchita"

    # Mostrar estado
    def mostrar_estado(self):
     print(f"Estado: {self.estado} | Hidratación: {self.hidratacion}% | Salud: {self.salud}")

#PROGRAMA PRINCIPAL 

print(">>> INICIANDO SISTEMA DE BIO-INGENIERÍA ARES-1 <<<")

nombre = input("Nombre de la planta: ")
especie = input("Especie de la planta: ")

planta = PlantaEspacial(nombre, especie)

print(f"\n--- REPORTE DE BIO-MONITOR: {planta.nombre} ---")
planta.mostrar_estado()

opcion = ""

while opcion != "3":

    opcion = input("\n¿Qué acción desea realizar? (1. Regar / 2. Dejar pasar día / 3. Salir): ")

    if opcion == "1":
        planta.regar()

    elif opcion == "2":
        planta.pasar_dia()

    elif opcion == "3":
        print("Saliendo del sistema...")

    else:
        print("Opción inválida")

    if opcion != "3":
        print(f"\n--- REPORTE DE BIO-MONITOR: {planta.nombre} ---")
        planta.mostrar_estado()