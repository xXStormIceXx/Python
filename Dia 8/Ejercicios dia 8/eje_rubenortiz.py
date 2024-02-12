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
pedidos_ordenados = json.dumps(pedidos_ordenados, indent=2, separators=(", "))
print("pedidos de mayor valor:")
print(pedidos_ordenados)



#3. Devuelve un listado con los identificadores de los clientes que han realizado algún pedido. Tenga en cuenta que no debe mostrar identificadores que estén repetidos.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 3---------------#")
print("#------------------------------------------------#")
ventas_data= data
clientes_con_pedidos = set([pedido["id_cliente"]for pedido in data ["ventas"]["pedidos"] ])
lista_de_clientes_con_pedidos = list(clientes_con_pedidos)
print(lista_de_clientes_con_pedidos)

#4. Devuelve un listado de todos los pedidos que se realizaron durante el año 2017, cuya cantidad total sea superior a 500€.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 4---------------#")
print("#------------------------------------------------#")

pedidos_2017_mayor_500 = [pedido for pedido in data["ventas"]["pedidos"] if pedido["fecha"].startswith("2017") and pedido["total"] > 500]
pedidos_2017_mayor_500 = json.dumps(pedidos_2017_mayor_500, indent=3, separators=(", "))
print(pedidos_2017_mayor_500)

#5. Devuelve un listado con el nombre y los apellidos de los comerciales que tienen una comisión entre 0.05 y 0.11.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 5---------------#")
print("#------------------------------------------------#")

comerciales_comision_05_11 = [comercial["nombre"] + " " + comercial["apellido1"] + " " + comercial["apellido2"] for comercial in data["ventas"]["comerciales"] if 0.05 <= comercial["comisión"] <= 0.11]
print(comerciales_comision_05_11)

#6. Devuelve el valor de la comisión de mayor valor que existe en la tabla comercial.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 6---------------#")
print("#------------------------------------------------#")

mayor_comision = max([comercial["comisión"] for comercial in data["ventas"]["comerciales"]])
print(mayor_comision)

#7. Devuelve el identificador, nombre y primer apellido de aquellos clientes cuyo ciudad sea "Sevilla". El listado deberá estar ordenado alfabéticamente por apellidos y nombre.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 7---------------#")
print("#------------------------------------------------#")

clientes_sevilla = sorted([{"id": cliente["id"], "nombre": cliente["nombre"], "apellido": cliente["apellido1"]} for cliente in data["ventas"]["clientes"] if cliente["ciudad"] == "Sevilla"], key=lambda x: (x["apellido"], x["nombre"]))
print(clientes_sevilla)

#8. Devuelve un listado de los nombres de los clientes que empiezan por A y terminan por n y también los nombres que empiezan por P. El listado deberá estar ordenado alfabéticamente.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 8---------------#")
print("#------------------------------------------------#")

clientes_A_N_P = sorted([cliente["nombre"] for cliente in data["ventas"]["clientes"] if (cliente["nombre"].startswith("A") and cliente["nombre"].endswith("N")) or cliente["nombre"].startswith("P")])
print(clientes_A_N_P)

#9. Devuelve un listado de los nombres de los clientes que  empiezan por A. El listado deberá estar ordenado alfabéticamente.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 9---------------#")
print("#------------------------------------------------#")

clientes_A = sorted([cliente["nombre"] for cliente in data["ventas"]["clientes"] if cliente["nombre"].startswith("A")])
print(clientes_A)

#10. Devuelve un listado con los nombres de los comerciales que tienen como apellido "Ruiz". Tenga en cuenta que se deberán eliminar los nombres repetidos.
print("#------------------------------------------------#")
print("#---------------EJERCICIO NUMERO 10--------------#")
print("#------------------------------------------------#")

comerciales_ruiz = set([comercial["nombre"] for comercial in data["ventas"]["comerciales"] if comercial["apellido1"] == "Ruiz"])
lista_comerciales_ruiz = list(comerciales_ruiz)
print(lista_comerciales_ruiz)