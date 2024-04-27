import sqlalchemy
import json
from unittest import TestCase
from faker import Faker
from faker.generator import random
from app import app
from datetime import datetime


class TestRiskAlertsTrainingPlan(TestCase):
    
    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()
        self.endpoint = "/risk_alerts_training_plan/3ae94e42"


    def test_post_not_None(self):
        nuevo_training_plan_fake = {
            "stop_training": self.data_factory.random_digit(),
            "notifications" : None ,
            "enable_phone": self.data_factory.random_digit(),
            "id_training_plan": None ,
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_post_succes(self):
        nuevo_training_plan_fake = {
            "stop_training": self.data_factory.random_digit(),
            "notifications" : None ,
            "enable_phone": self.data_factory.random_digit(),
            "id_training_plan": None ,
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "Se pudo crear la alerta de riesgo de la sesion de entrenamiento exitosamante")


    def test_post_error(self):
        nuevo_training_plan_fake = {
            "stop_training": self.data_factory.random_digit(),
            "notifications" : None ,
            "enable_phone": self.data_factory.name(),
            "id_training_plan": None ,
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "No se pudo crear la alerta de riesgo de la sesion de entrenamiento exitosamante")

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
        self.assertFalse(solicitud_crear_planEntrenamiento["message"] == "Se Encontro el plan de entranamiento buscado")

    def test_get_error(self):
        endpoint = "/risk_alerts_training_plan/123"
        solicitud_crear_planEntrenamiento = self.client.get(endpoint,
                                                             data= '',
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertFalse(solicitud_crear_planEntrenamiento["message"] == "No se ha encontrado al  alerta de riesgo buscada")

    def test_put_not_None(self):
        nuevo_training_plan_fake = {
            "stop_training": self.data_factory.random_digit(),
            "notifications" : None ,
            "enable_phone": self.data_factory.random_digit(),
            "id_training_plan": None ,
        }
        solicitud_crear_planEntrenamiento = self.client.put(self.endpoint,
                                                             data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_put_succes(self):
        nuevo_training_plan_fake = {
            "stop_training": self.data_factory.random_digit(),
            "notifications" : None ,
            "enable_phone": self.data_factory.random_digit(),
            "id_training_plan": None ,
        }
        solicitud_crear_planEntrenamiento = self.client.put(self.endpoint,
                                                             data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "Se actualizarón correctamente los campos")

    def test_put_error(self):
        endpoint = "/training_plan/372a7"
        nuevo_training_plan_fake = {
            "stop_training": self.data_factory.random_digit(),
            "notifications" : None ,
            "enable_phone": self.data_factory.random_digit(),
            "id_training_plan": None ,
        }
        solicitud_crear_planEntrenamiento = self.client.put(endpoint,
                                                              data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertFalse(solicitud_crear_planEntrenamiento["message"] == "No se encontro la alerta de riesgo buscada")

    def test_put_error(self):
        nuevo_training_plan_fake = {
            "stop_training": self.data_factory.random_digit(),
            "notifications" : None ,
            "enable_phone": self.data_factory.word(),
            "id_training_plan": None ,
        }
        solicitud_crear_planEntrenamiento = self.client.put(self.endpoint,
                                                              data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "No se pudo realizar la Actualización")


