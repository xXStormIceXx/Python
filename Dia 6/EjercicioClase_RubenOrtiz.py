#----------------Realizar un programa que use un diccionario para gestionar los productos----------------#
#----------------(Y) precios de la tabla, donde se le pregunte al usuario por un producto------------------# 
#----------------(Y) la cantidad. al finalizar mostrar en la consola el precio total.----------------------#
#----------------si el producto no esta debe mostrar un mensaje informando sobre ello.-------------------#


stockmascotas = {"tiposdemascotas":("perros","gatos","aves","peces","reptiles"),
              "preciosmascotas":(500,1200,100,50,800)}

for i in range(5):
    print(stockmascotas["tiposdemascotas"][i],"\t",stockmascotas["preciosmascotas"][i])
    
mascotadeseada = str(input("Digite la Mascota que desea: "))
cantidaddemascotas = int(input("digite la cantidad de mascotas que desea llevar: "))
totalapagar = int

if mascotadeseada == stockmascotas["tiposdemascotas"][i]:
    totalapagar = cantidaddemascotas*stockmascotas["tiposdemascotas"][i]
    print("el valor a pagar por las mascotas es: ",totalapagar)
else:
    print("el valor ingresado no es correcto")