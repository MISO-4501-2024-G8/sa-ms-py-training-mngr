import sqlalchemy
import json
from unittest import TestCase
from faker import Faker
from faker.generator import random
from app import app
from datetime import datetime


class TestInstructionsTrainingPlan(TestCase):
    
    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()
        self.endpoint = "/instruction_training_plan"
        self.endpoint_id = "/instruction_training_plan/977e4368"


    def test_post_not_None(self):
        nuevo_training_plan_fake = {
            "instruction_description": self.data_factory.name(),
            "instruction_time": self.data_factory.random_digit(),
            "id_objective": None ,
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_post_succes(self):
        nuevo_training_plan_fake = {
            "instruction_description": self.data_factory.name(),
            "instruction_time": self.data_factory.random_digit(),
            "id_objective": None ,
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "Se pudo crear la instruiccion del objetivo que pertenence a la sesión de entrenamiento exitosamante")

    def test_post_error(self):
        nuevo_training_plan_fake = {
            "instruction_description": self.data_factory.name(),
            "instruction_time": self.data_factory.name(),
            "id_objective": None ,
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "No se pudo crear la instruicción del objetivo que pertenence a la sesión de entrenamiento exitosamante")

    def test_get_not_None(self):
        solicitud_crear_planEntrenamiento = self.client.get(self.endpoint_id,
                                                             data= '',
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_get_succes(self):
        nuevo_training_plan_fake = {
            "instruction_description": self.data_factory.name(),
            "instruction_time": self.data_factory.random_digit(),
            "id_objective": None ,
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        id_instruction = json.loads(solicitud_crear_planEntrenamiento)["instruction"]["id"]
        solicitud_crear_planEntrenamiento = self.client.get(self.endpoint_id.replace("977e4368", id_instruction),
                                                             data= '',
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        print(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "Se Encontro la instruccion buscada")

    def test_get_error(self):
        endpoint = "/training_plan/123"
        solicitud_crear_planEntrenamiento = self.client.get(endpoint,
                                                             data= '',
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertFalse(solicitud_crear_planEntrenamiento["message"] == "No se ha encontrado coninsidencia de la instruccion buscada")
    def test_put_not_None(self):
        nuevo_training_plan_fake = {
            "instruction_description": self.data_factory.name(),
            "instruction_time": self.data_factory.random_digit(),
            "id_objective": None ,
        }
        solicitud_crear_planEntrenamiento = self.client.put(self.endpoint_id,
                                                             data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_put_succes(self):
        nuevo_training_plan_fake = {
            "instruction_description": self.data_factory.name(),
            "instruction_time": self.data_factory.random_digit(),
            "id_objective": None ,
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        id_instruction = json.loads(solicitud_crear_planEntrenamiento)["instruction"]["id"]
        nuevo_training_plan_fake = {
            "instruction_description": self.data_factory.name(),
            "instruction_time": self.data_factory.random_digit(),
            "id_objective": None ,
        }
        solicitud_crear_planEntrenamiento = self.client.put(self.endpoint_id.replace("977e4368", id_instruction),
                                                             data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "Se actualizarón correctamente los campos")

    def test_put_error(self):
        endpoint = "/training_plan/372a7"
        nuevo_training_plan_fake = {
            "instruction_description": self.data_factory.name(),
            "instruction_time": self.data_factory.random_digit(),
            "id_objective": None ,
        }
        solicitud_crear_planEntrenamiento = self.client.put(endpoint,
                                                              data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertFalse(solicitud_crear_planEntrenamiento["message"] == "No se encontro la Instruccion del plan de entrenamiento buscada")

    def test_put_error(self):
        nuevo_training_plan_fake = {
            "instruction_description": self.data_factory.name(),
            "instruction_time": self.data_factory.random_digit(),
            "id_objective": None ,
        }
        solicitud_crear_planEntrenamiento = self.client.put(self.endpoint_id,
                                                              data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertFalse(solicitud_crear_planEntrenamiento["message"] == "No se pudo realizar la Actualización")
    
    def test_put_get_integrity_error(self):
        endpoint = "/instruction_training_plan/integrity_error"
        self.client.put(endpoint,
                        data= {},
                        headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.client.get(endpoint,
                        data= '',
                        headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
