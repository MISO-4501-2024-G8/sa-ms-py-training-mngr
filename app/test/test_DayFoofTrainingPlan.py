import sqlalchemy
import json
from unittest import TestCase
from faker import Faker
from faker.generator import random
from app import app
from datetime import datetime


class TestDayFoofTrainingPlan(TestCase):
    
    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()
        self.endpoint = "/day_food_training_plan"


    def test_post_not_None(self):
        nuevo_training_plan_fake = {
            "day_food_plan": self.data_factory.name(),
            "food" : self.data_factory.word(),
            "calories" : self.data_factory.random_digit(),
            "value": self.data_factory.random_digit(),
            "id_eating_routine": None,

        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint +"/123",
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_post_succes(self):
        nuevo_training_plan_fake = {
            "day_food_plan": self.data_factory.name(),
            "food" : self.data_factory.word(),
            "calories" : self.data_factory.random_digit(),
            "value": self.data_factory.random_digit(),
            "id_eating_routine": None,

        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint + "/123",
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertFalse(solicitud_crear_planEntrenamiento["message"] == "Se pudo crear el plan de alimentacion diario de la rutina de comida de la sesion de entrenamiento exitosamante")


    def test_post_error(self):
        nuevo_training_plan_fake = {
            "day_food_plan": self.data_factory.name(),
            "food" : self.data_factory.word(),
            "calories" : self.data_factory.random_digit(),
            "value": self.data_factory.word(),
            "id_eating_routine": None,

        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint + "/123",
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "No se pudo crear el plan de alimentacion diario de la rutina de comida de la sesion de entrenamiento exitosamante")
