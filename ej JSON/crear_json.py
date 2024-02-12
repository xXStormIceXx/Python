import json

data = {}
data["clientes"] = []
data["clientes"].append({
    "nombre":"ruben",
    "apellido":"ortiz",
    "edad":25,
    "importe":2.55
})
data["clientes"].append({
    "nombre":"nelcy",
    "apellido":"ortega",
    "edad":49,
    "importe":4.55
})
data["clientes"].append({
    "nombre":"daniel",
    "apellido":"ortega",
    "edad":20,
    "importe":6.55
})

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)