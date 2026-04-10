# Reto integrador con atributos privados
# Núcleo lógico de un Banco

class CuentaBancaria:
    # Atributos de clase
    tasa_interes_global = 0.05
    total_cuentas_creadas = 0

    # Constructor
    def __init__(self, nombre_titular):
        self.__saldo = 0.0
        self.titular = nombre_titular  # Usa el setter para validar
        CuentaBancaria.total_cuentas_creadas += 1

    # Propiedad saldo (solo lectura)
    @property
    def saldo(self):
        return self.__saldo

    # Propiedad titular
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, nuevo_titular):
        if not nuevo_titular.strip():
            raise ValueError("El nombre del titular no puede estar en blanco.")
        self.__titular = nuevo_titular

    # Métodos de instancia
    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser positiva.")
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.__saldo:
            raise ValueError("No hay suficiente saldo para retirar esa cantidad.")
        self.__saldo -= cantidad

    def proyectar_interes(self):
        interes = self.__saldo * CuentaBancaria.tasa_interes_global
        print(f"El interés proyectado para este año es: {interes:.2f}")

    # Método de clase
    @classmethod
    def modificar_tasa_interes(cls, nueva_tasa):
        cls.tasa_interes_global = nueva_tasa


# =========================
# Simulación del programa
# =========================
if __name__ == "__main__":
    try:
        # Crear dos cuentas
        cuenta1 = CuentaBancaria("Evelyn Castro")
        cuenta2 = CuentaBancaria("Sofía López")

        # Imprimir total de cuentas
        print(f"Total de cuentas creadas: {CuentaBancaria.total_cuentas_creadas}")

        # Depositar 10,000 a cuenta1
        cuenta1.depositar(10000)
        print(f"Saldo de cuenta1: {cuenta1.saldo}")

        # Proyectar interés con 5%
        cuenta1.proyectar_interes()

        # Cambiar tasa a 10%
        CuentaBancaria.modificar_tasa_interes(0.10)

        # Proyectar nuevamente
        cuenta1.proyectar_interes()

        # Intentar cambiar a nombre vacío (debe fallar)
        cuenta2.titular = ""

    except ValueError as e:
        print(f"Error: {e}")