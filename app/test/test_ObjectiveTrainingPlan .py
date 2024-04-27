import sqlalchemy
import json
from unittest import TestCase
from faker import Faker
from faker.generator import random
from app import app
from datetime import datetime


class TestObjetiveTrainingPlan(TestCase):
    
    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()
        self.endpoint = "/objetive_training_plan"


    def test_post_not_None(self):
        nuevo_training_plan_fake = {
            "day": self.data_factory.name(),
            "objective_repeats": self.data_factory.random_digit(),
            "type_objective": self.data_factory.random_digit() ,
            "id_training_plan": None,
            "id_rest_routine": "b76ff61a"
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint +"/123",
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_post_succes(self):
        nuevo_training_plan_fake = {
            "day": self.data_factory.name(),
            "objective_repeats": self.data_factory.random_digit(),
            "type_objective": self.data_factory.random_digit(),
            "id_training_plan": None,
            "id_rest_routine": "b76ff61a"
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint + "/123",
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "Se pudo crear el objetivo sesion de entrenamiento exitosamante")

    def test_post_error(self):
        nuevo_training_plan_fake = {
            "day": self.data_factory.name(),
            "objective_repeats": self.data_factory.name(),
            "type_objective": self.data_factory.name() ,
            "id_training_plan": None,
            "id_rest_routine": "b76ff61a"
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint + "/123",
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "No se pudo crear el objetivo sesion de entrenamiento")
