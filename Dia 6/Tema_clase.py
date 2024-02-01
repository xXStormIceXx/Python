#Creación de Diccionario - {llave1:valor1,llave2:valor2}
diccionario = {'Nombre':("Danna","Mozo","Andres","Ruben","juanda"),
               "Edad":(18,17,19,25,16),
               "Barrio":("Zapamanga","giron","piedecuesta","provenza","centro")}
print(diccionario)
print(type(diccionario))

#Buscar valor de x llave del diccionario y buscar 
#el segundo dato que contiene la subdiccionario
print(diccionario['Nombre'][1])
diccionario['Nombre']="Danna"
print(diccionario)
print(type(diccionario))
print(diccionario['Nombre'])

#Recorrer un Diccionario por llaves
for i in diccionario:
    print(i)

#Recorrer un Diccionario por valor 
for valor in diccionario:
    print(diccionario[valor])

#Imprimir las llaves y valores de un diccionario
for llave , valor in diccionario.items():
    print(llave,valor)


#guardar las llaves de un diccionario en una lista
listallaves = diccionario.keys()
print(listallaves)

# guardar los valores de un diccionario en una lista
listavalores = diccionario.values()
print(listavalores)

# Eliminar una llaves de un diccionario
diccionario.pop("nombre")
print(diccionario)


#cruzaar un obgeto de un diccionario a otro

diccionario2= {"edad":23, "barrio":"ruitoque"}
diccionario.update(diccionario2)
print(diccionario)

