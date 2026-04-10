class AgenteSeguridad:

    def evaluar_entrada(self):
        nivel_puerta = int(input("Ingrese el nivel de seguridad de la puerta (1-5): "))

        if self.nivel_acceso >= nivel_puerta:
            print(f"Acceso concedido para {self.nombre}")
        else:
            print("Acceso denegado")


# Programa principal
guardia_turno = AgenteSeguridad()
guardia_turno.nombre = "Yeraldy"
guardia_turno.nivel_acceso = 4

guardia_turno.evaluar_entrada()