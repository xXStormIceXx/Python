#----------------Realizar un programa que use un diccionario para gestionar los productos----------------#
#----------------(Y) precios de la tabla, donde se le pregunte al usuario por un producto------------------# 
#----------------(Y) la cantidad. al finalizar mostrar en la consola el precio total.----------------------#
#----------------si el producto no esta debe mostrar un mensaje informando sobre ello.-------------------#


invproduc = {"mascotas":("perros","gatos","aves","peces","reptiles"),
                      "cantidad":(500,1200,100,50,800)}
mascotas = invproduc["mascotas"]
for i in range(5):
    print(invproduc["mascotas"][i],"\t",invproduc["cantidad"][i])
    
mascotas = str(input("Digite la Mascota que desea: "))
cantidad = int(input(f"digite la cantidad de mascotas que desea llevar: "))