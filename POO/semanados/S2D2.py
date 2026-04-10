#Encapusulado
# Le pondres una candado a la informacion
#Sintaxis
# class Cuenta:
#     def __init__(self, SaldoInicial):
#         self.nombre = "Publica" #Atributo publico
#         self.__saldo = "saldo_inicial" #Atributo privado
# mi_cuenta = Cuenta(100)
# print(mi_cuenta.nombre)
# print(mi_cuenta.__saldo) #Error el guardia no nos deja pasar 

#Ventanilla de atencion: Getter y Setter (metodos tradicionales)
#Los getter son obtenedores y retoran el valor del atributo privado
#los setter para modificar los vales, es un metodo que  recibe un parametro
class UsuarioBancario:
    def __init__(self, nombre_ingresado, pin_ingresado):
        self.nombre = nombre_ingresado
        # Atributo privado
        self.__pin = pin_ingresado
#Getter tradicional (Ventanilla para consultar)
    def get__pin(self):
        return self.__pin
    
    def set_pin(self, nuevo_pin):
        #validacion
        
        if len(nuevo_pin) <= 4:
