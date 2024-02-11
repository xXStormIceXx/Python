import json

class Camper:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

class Trainer:
    def __init__(self, id, name, specialty):
        self.id = id
        self.name = name
        self.specialty = specialty

class TrainingRoute:
    def __init__(self, id, name, difficulty):
        self.id = id
        self.name = name
        self.difficulty = difficulty

class Evaluation:
    def __init__(self, id, camper_id, route_id, score):
        self.id = id
        self.camper_id = camper_id
        self.route_id = route_id
        self.score = score

class Camp:
    def __init__(self):
        self.campers = []
        self.trainers = []
        self.routes = []
        self.evaluations = []

    def add_camper(self, camper):
        self.campers.append(camper)

    def add_trainer(self, trainer):
        self.trainers.append(trainer)

    def add_route(self, route):
        self.routes.append(route)

    def add_evaluation(self, evaluation):
        self.evaluations.append(evaluation)

    def to_json(self):
        data = {
            "campers": [vars(camper) for camper in self.campers],
            "trainers": [vars(trainer) for trainer in self.trainers],
            "routes": [vars(route) for route in self.routes],
            "evaluations": [vars(evaluation) for evaluation in self.evaluations]
        }
        return data

    def from_json(self, data):
        self.campers = [Camper(**camper) for camper in data["campers"]]
        self.trainers = [Trainer(**trainer) for trainer in data["trainers"]]
        self.routes = [TrainingRoute(**route) for route in data["routes"]]
        self.evaluations = [Evaluation(**evaluation) for evaluation in data["evaluations"]]

# Ejemplo de uso:
# Crear instancias de las clases
camper1 = Camper(1, "Juan", 20)
trainer1 = Trainer(1, "Carlos", "Yoga Instructor")
route1 = TrainingRoute(1, "Mountain Trail", "Intermediate")
evaluation1 = Evaluation(1, 1, 1, 85)

# Crear una instancia del campamento
camp = Camp()

# Agregar instancias al campamento
camp.add_camper(camper1)
camp.add_trainer(trainer1)
camp.add_route(route1)
camp.add_evaluation(evaluation1)

# Convertir el campamento a formato JSON
camp_json = camp.to_json()

# Guardar el JSON en un archivo
with open("camp_data.json", "w") as json_file:
    json.dump(camp_json, json_file)

# Recuperar datos desde el archivo JSON
with open("camp_data.json", "r") as json_file:
    loaded_data = json.load(json_file)

# Crear una nueva instancia de Camp y cargar los datos
new_camp = Camp()
new_camp.from_json(loaded_data)


class Camp:
    # ... (código previo)

    def register_camper(self, name, age):
        camper_id = len(self.campers) + 1
        new_camper = Camper(camper_id, name, age)
        self.add_camper(new_camper)
        print(f"Camper {name} registrado con éxito. ID: {camper_id}")

    def advance_academic_progress(self, camper_id, route_id, score):
        # Verificar si el camper y la ruta existen
        if not any(camper.id == camper_id for camper in self.campers):
            print(f"No se encontró al camper con ID {camper_id}")
            return

        if not any(route.id == route_id for route in self.routes):
            print(f"No se encontró la ruta de entrenamiento con ID {route_id}")
            return

        # Verificar si el camper ya tiene una evaluación para esta ruta
        existing_evaluation = next(
            (evaluation for evaluation in self.evaluations
             if evaluation.camper_id == camper_id and evaluation.route_id == route_id), None)

        if existing_evaluation:
            print(f"El camper ya tiene una evaluación para la ruta de entrenamiento con ID {route_id}.")
            return

        # Crear una nueva evaluación y actualizar el estado del camper
        new_evaluation = Evaluation(len(self.evaluations) + 1, camper_id, route_id, score)
        self.add_evaluation(new_evaluation)

        # Actualizar el estado del camper
        camper = next(camper for camper in self.campers if camper.id == camper_id)
        if score >= 70:
            camper.status = "Aprobado"
        else:
            camper.status = "Reprobado"

        print(f"Se registró la evaluación para el camper {camper.name} en la ruta {route_id}. Estado académico: {camper.status}")

# Ejemplo de uso:
# Crear una instancia del campamento
camp = Camp()

# Registrar nuevos campers
camp.register_camper("Laura", 22)
camp.register_camper("Miguel", 19)

# Realizar evaluaciones y actualizar el estado académico
camp.advance_academic_progress(1, 1, 85)
camp.advance_academic_progress(2, 1, 60)

# Imprimir información sobre los campers
for camper in camp.campers:
    print(f"Camper {camper.name} - Estado: {camper.status}")