# Crea la clase RegistroAcademico.
class RegistroAcademico:
# En el constructor __init__, recibe nombre_alumno y nota_inicial.
# Define los atributos:
# self.nombre (público)
# self.__nota (privado)
    def __init__(self, nombre_alumno, nota_inicial):
# self.cuenta_activa = True (estado inicial público por defecto)
        self.nombre = nombre_alumno
        self.__nota = nota_inicial
        self.cuenta_activa = True
# Crea el método get_nota(self) que retorne la nota privada.
    def get_nota(self):
     return self.__nota
# Crea un método bloquear_cuenta(self) que cambie el estado self.cuenta_activa a False.
     def bloquear_cuenta(self):
        self.cuenta_activa = False
# Crea el método set_nota(self, nueva_nota). La lógica debe ser:
    def set_nota(self, nueva_nota):
# Si self.cuenta_activa es False, retorna el código numérico -2 (Significa: Cuenta bloqueada).
# Si la nueva nota está entre 0 y 100, actualiza la nota y retorna el código 1 (Significa: Éxito).
# Si no cumple ninguna de las anteriores, retorna el código -1 (Significa: Dato inválido).
        if self.cuenta_activa == False:
             return -2
        elif nueva_nota >= 0 and nueva_nota <= 100:
            self__nota = nueva_nota
            return 1
        else:
            return-1
            
# En el programa principal:
# Instancia a la alumna "Laura" con nota 85.
alumna = RegistroAcademico("Laura", 85)
# Crea un contador de intentos_permitidos = 3.
intentos_permitidos = 3
# Crea un bucle while intentos_permitidos > 0.
while intentos_permitidos >  0:
    
# Dentro del bucle, usa input() para pedirle al profesor la nueva nota.
    nueva_nota= float(input("Ingrese la nueva nota "))
# Llama a set_nota() guardando el resultado en una variable.
# Evalúa el código devuelto usando if/elif:
# Si es 1, felicita y rompe el bucle (break).
# Si es -1, réstale 1 a los intentos y advierte al usuario.
# # Fuera del bucle, si los intentos llegaron a 0, llama al método para bloquear la cuenta e informa al usuario.
    resultado = alumna.set_nota(nueva_nota)

    if resultado == 1:
        print("Nota actualizada correctamente")

    elif resultado == -1:
        intentos_permitidos -= 1
        print(f"Dato inválido. Intentos restantes: {intentos_permitidos}")

    elif resultado == -2:
        print("La cuenta está bloqueada")
    

# Fuera del while
        if intentos_permitidos == 0:
                alumna.bloquear_cuenta()
        print("Cuenta bloqueada por demasiados intentos")