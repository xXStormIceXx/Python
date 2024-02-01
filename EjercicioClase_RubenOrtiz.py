#----------------Realizar un programa que use un diccionario para gestionar los productos----------------#
#----------------(Y) precios de la tabla, donde se le pregunte al usuario por un producto------------------# 
#----------------(Y) la cantidad. al finalizar mostrar en la consola el precio total.----------------------#
#----------------si el producto no esta debe mostrar un mensaje informando sobre ello.-------------------#


invproduc = {"maxcotas":("perros","gatos","aves","peces","reptiles"),
              "precios":(500,1200,100,50,800)}

for i in range(5):
    print(invproduc["maxcotas"][i],"\t",invproduc["precios"][i])
    
mascotas = str(input("Digite la Mascota que desea: "))
cantidad = int(input(f"digite la cantidad de mascotas que desea llevar: "))
mascotas = mascotas.capitalize()
totalapagar = int

if mascotas in invproduc("maxcotas"):
    pocicionmascota = invproduc["macotas"].index(mascotas)
    totalapagar = invproduc["precios"][pocicionmascota]
    totalapagar = totalapagar * cantidad
    print(f"el total a pagar por las mascotas es: $",totalapagar,)
else:
    print("La mascota ingresada no se encuentra en el inventario")
