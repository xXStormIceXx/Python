##-------------------------------##
##----------EJERCICIO 1----------##
##-------------------------------##
##---Desarollado por RUBEN DARIO ORTIZ ORTEGA---##
print("hola mundo")
##Impresion en Consola##
##-----Datos Primitivos-----##
# 1.String
texto = ("Campus")
print (texto)
print (type(texto))
# 2.Int
numeroentero = 1
print (numeroentero) 
# 3.Double
numerodecimal = 3.1
print (numerodecimal)
# 4.Float
numerodecimallargo = 3.1416
print (numerodecimallargo) 
# 5.Boolean
bolean = True
print (bolean)
#-------Entradas Parte del usuario------
entradausuario = input ("ingresa tu nombre: ")
print ("tu nombre es: ", entradausuario)
#----Entradas parte del usuario con definicion de tipo de dato primitivo----
entradausuarionumero = input ("Ingresa tu edad: ")
numerofinal = int (entradausuarionumero)
print ("tu edad es: ", numerofinal)
#-------CICLOS-------+
# a. Ciclo For
for i in range (5,10,2): #For contador en range de (desde, hasta, pasos): 
    print (i)
# b. Ciclo While
booleanito = True    
while booleanito == True:# while Condicion_a_Cumplir:
    print("sigovivo")
booleanito = False
# c. Condicionales
texto1 = "campus"
if texto1 == "campus":
    print("Soy Campus")
else:
    print("No soy Campus")
#-----FUNCIONCES--------
# Funcion sin reetorno y sin parametros

def saludar():
 print("Hola! Mundo")

# Funcion sin retorno y con parametros

def saludar2(nombre):
 print("Hola!", nombre) 
 #llamar luego a la Finsion
 saludar2 ("RUBEN")

# Funcion con retorno y sin parametros

def obtener_numero():
    return 42
resultado = obtener_numero ()
print ("resultado")

# Funciones con retorno y con parametros

def suma(a,b):
    resultado = a + b
    return resultado
# Uso de la Funcion
resultado_suma = suma(3, 5)
print(resultado_suma)
#salida: 8

#------ Listas-------
# En Python un "array" se suele referir a una lista, que es una estructura de datos que pude contener elementos de diferentes tipos
#Ejemplos
array = ["perro", "gato", "pajaro", "peces" ]
mi_array = [1, 2, 3, 4, 5]
