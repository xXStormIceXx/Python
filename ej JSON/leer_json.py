import json, os
script = os.path.dirname(__file__)

with open(script+"/data.json") as file:
    data = json.load(file)
    for client in data["clientes"]:
        print("Nombre", client["nombre"])
        print("Apellido", client["apellido"])
        print("")