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
        self.endpoint = "/training_plan/3872a743"


    def test_post_not_None(self):
        nuevo_training_plan_fake = {
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks": self.data_factory.random_digit(),
            "lunes_enabled": self.data_factory.random_digit() ,
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled":self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word(),
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint +"/123",
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_post_succes(self):
        nuevo_training_plan_fake = {
           "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks": self.data_factory.random_digit(),
            "lunes_enabled": self.data_factory.random_digit() ,
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled":self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word(),
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint + "123",
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "Se pudo crear la sesión de entrenamiento exitosamante")

    def test_post_error(self):
        nuevo_training_plan_fake = {
            "name": self.data_factory.name(),
                "description": self.data_factory.name(),
                "weeks": self.data_factory.random_digit(),
                "lunes_enabled": self.data_factory.name() ,
                "martes_enabled": self.data_factory.random_digit(),
                "miercoles_enabled": self.data_factory.random_digit(),
                "jueves_enabled":self.data_factory.random_digit(),
                "viernes_enabled": self.data_factory.random_digit(),
                "typePlan": self.data_factory.word(),
                "sport": self.data_factory.word(),
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint + "123",
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "No se pudo crear la sesión de entrenamiento")

    def test_get_not_None(self):
        solicitud_crear_planEntrenamiento = self.client.get(self.endpoint,
                                                             data= '',
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_get_succes(self):
        solicitud_crear_planEntrenamiento = self.client.get(self.endpoint,
                                                             data= '',
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "Se Encontro el plan de entranamiento buscado")

    def test_get_error(self):
        endpoint = "/training_plan/372a7"
        solicitud_crear_planEntrenamiento = self.client.get(endpoint,
                                                             data= '',
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "No se ha encontrado coninsidencia del plan de entranamiento buscado")

    def test_put_not_None(self):
        nuevo_training_plan_fake = {
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks": self.data_factory.random_digit(),
            "lunes_enabled": self.data_factory.random_digit() ,
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled":self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word()
        }
        solicitud_crear_planEntrenamiento = self.client.put(self.endpoint,
                                                             data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_put_succes(self):
        nuevo_training_plan_fake = {
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks": self.data_factory.random_digit(),
            "lunes_enabled": self.data_factory.random_digit() ,
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled":self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word()
        }
        solicitud_crear_planEntrenamiento = self.client.put(self.endpoint,
                                                             data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "Se actualizarón correctamente los campos")

    def test_put_error(self):
        endpoint = "/training_plan/372a7"
        nuevo_training_plan_fake = {
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks": self.data_factory.random_digit(),
            "lunes_enabled": self.data_factory.random_digit() ,
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled":self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word()
        }
        solicitud_crear_planEntrenamiento = self.client.put(endpoint,
                                                              data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "El plan de entranamiento no existe")

    def test_put_error_message2(self):
        nuevo_training_plan_fake = {
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks": self.data_factory.random_digit(),
            "lunes_enabled": self.data_factory.random_digit() ,
            "martes_enabled": self.data_factory.word(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled":self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word()
        }
        solicitud_crear_planEntrenamiento = self.client.put(self.endpoint,
                                                              data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "No se pudo realizar la Actualización")

