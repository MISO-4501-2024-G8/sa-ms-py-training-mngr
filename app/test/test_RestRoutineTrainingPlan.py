import sqlalchemy
import json
from unittest import TestCase
from faker import Faker
from faker.generator import random
from app import app
from datetime import datetime


class TestRestRoutineTrainingPlan(TestCase):
    
    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()
        self.endpoint = "/rest_routine_training_plan"


    def test_post_not_None(self):
        nuevo_training_plan_fake = {
            "rest_routine_name": self.data_factory.name(),
            "rest_routine_description": self.data_factory.name(),
            "id_training_plan": "3872a743" ,
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint +"/123",
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_post_succes(self):
        nuevo_training_plan_fake = {
            "rest_routine_name": self.data_factory.name(),
            "rest_routine_description": self.data_factory.name(),
            "id_training_plan": "3872a743" ,
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint + "/123",
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "Se pudo crear la rutina de descanso de la sesion de entrenamiento exitosamante")

    def test_post_error(self):
        nuevo_training_plan_fake = {
            "rest_routine_name": self.data_factory.name(),
            "rest_routine_description": None,
            "id_training_plan": "3872a743" ,
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint + "/123",
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        print(solicitud_crear_planEntrenamiento)
        self.assertFalse(solicitud_crear_planEntrenamiento["message"] == "No se pudo crear la rutina de descanso de la sesion de entrenamiento exitosamante")
