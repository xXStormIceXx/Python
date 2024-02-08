import json
with open('data.json') as contenido:
    data = json.load(contenido)

print(data)
#1. Devuelve un listado con todos los pedidos que se han realizado. Los pedidos deben estar ordenados por la fecha de realización, mostrando en primer lugar los pedidos más recientes.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 1---------------#")
print("#------------------------------------------------#")


pedidos = data["ventas"]["pedidos"]
pedidos_ordenados = sorted(pedidos, key = lambda x: x["fecha"],reverse=True)
for pedido in pedidos_ordenados:
    print(pedido)

#2. Devuelve todos los datos de los dos pedidos de mayor valor.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 2---------------#")
print("#------------------------------------------------#")

pedidos = data["ventas"]["pedidos"]
pedidos_ordenados = sorted(pedidos, key = lambda x: x["total"],reverse=True)[:2]
print("pedidos de mayor valor")
print(pedidos_ordenados)


#3. Devuelve un listado con los identificadores de los clientes que han realizado algún pedido. Tenga en cuenta que no debe mostrar identificadores que estén repetidos.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 3---------------#")
print("#------------------------------------------------#")

 
#4. Devuelve un listado de todos los pedidos que se realizaron durante el año 2017, cuya cantidad total sea superior a 500€.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 4---------------#")
print("#------------------------------------------------#")
#5. Devuelve un listado con el nombre y los apellidos de los comerciales que tienen una comisión entre 0.05 y 0.11.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 5---------------#")
print("#------------------------------------------------#")
#6. Devuelve el valor de la comisión de mayor valor que existe en la tabla comercial.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 6---------------#")
print("#------------------------------------------------#")
#7. Devuelve el identificador, nombre y primer apellido de aquellos clientes cuyo ciudad sea "Sevilla". El listado deberá estar ordenado alfabéticamente por apellidos y nombre.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 7---------------#")
print("#------------------------------------------------#")
#8. Devuelve un listado de los nombres de los clientes que empiezan por A y terminan por n y también los nombres que empiezan por P. El listado deberá estar ordenado alfabéticamente.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 8---------------#")
print("#------------------------------------------------#")
#9. Devuelve un listado de los nombres de los clientes que  empiezan por A. El listado deberá estar ordenado alfabéticamente.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 9---------------#")
print("#------------------------------------------------#")
#10. Devuelve un listado con los nombres de los comerciales que tienen como apellido "Ruiz". Tenga en cuenta que se deberán eliminar los nombres repetidos.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 10--------------#")
print("#------------------------------------------------#")
#OPCIONAL : CREAR UN CRUD (CREACION,LECTURA,ACTUALIZACIÓN Y ELIMINACIÓN) DE LOS 3 CONJUNTOS DE DATOS ADENTRO DE DATA.JSON, LOS CUALES DEBEN SER PERSISTENTES DONDE APLIQUE.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 11--------------#")
print("#------------------------------------------------#")