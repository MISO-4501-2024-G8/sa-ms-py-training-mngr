import sqlalchemy
import json
from unittest import TestCase
from faker import Faker
from faker.generator import random
from app import app
from datetime import datetime


class TestTrainingPlan(TestCase):
    
    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()
        self.endpoint = "/training_plan"


    def test_post_not_None(self):
        nuevo_training_plan_fake = {
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks":self.data_factory.name(),
            "lunes_enabled": self.data_factory.random_digit() ,
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled":self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.random_digit(),
            "sport": self.data_factory.word(),
            "Objectives" : None,
            "createdAt" : str(datetime.now()),
            "updatedAt" : str(datetime.now())
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_post_succes(self):
        nuevo_training_plan_fake = {
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks":self.data_factory.name(),
            "lunes_enabled": self.data_factory.random_digit() ,
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled":self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.random_digit(),
            "sport": self.data_factory.word(),
            "Objectives" : None,
            "createdAt" : str(datetime.now()),
            "updatedAt" : str(datetime.now())
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint + "123",
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.dumps(solicitud_crear_planEntrenamiento)
        print("solicitud_crear_planEntrenamiento::::::", solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento == 200 )
