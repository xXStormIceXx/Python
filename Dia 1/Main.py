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