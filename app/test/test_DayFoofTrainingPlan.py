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
        self.endpoint_id = "/day_food_training_plan/1ec7b141"
        self.endpoint = "/day_food_training_plan"


    def test_post_not_None(self):
        nuevo_training_plan_fake = {
            "day_food_plan": self.data_factory.name(),
            "food" : self.data_factory.word(),
            "calories" : self.data_factory.random_digit(),
            "value": self.data_factory.random_digit(),
            "id_eating_routine": None,

        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
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
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
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
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "No se pudo crear el plan de alimentacion diario de la rutina de comida de la sesion de entrenamiento exitosamante")

    def test_get_not_None(self):
        solicitud_crear_planEntrenamiento = self.client.get(self.endpoint_id,
                                                             data= '',
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_get_succes(self):
        solicitud_crear_planEntrenamiento = self.client.get(self.endpoint_id,
                                                             data= '',
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertFalse(solicitud_crear_planEntrenamiento["message"] == "Se Encontro el plan de comida diario buscado")

    def test_get_error(self):
        endpoint = "/day_food_training_plan/123"
        solicitud_crear_planEntrenamiento = self.client.get(endpoint,
                                                             data= '',
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "No se ha encontrado el plan de comida diario buscado")
    
    def test_get_ex_error(self):
        endpoint = "/day_food_training_plan/error"
        solicitud_crear_planEntrenamiento = self.client.get(endpoint,
                                                             data= '',
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
    
    def test_get_integrity_error(self):
        endpoint = "/day_food_training_plan/integrity_error"
        solicitud_crear_planEntrenamiento = self.client.get(endpoint,
                                                             data= '',
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")


    def test_put_not_None(self):
        nuevo_training_plan_fake = {
            "day_food_plan": self.data_factory.name(),
            "food" : self.data_factory.word(),
            "calories" : self.data_factory.random_digit(),
            "value": self.data_factory.random_digit(),
            "id_eating_routine": None,

        }
        solicitud_crear_planEntrenamiento = self.client.put(self.endpoint_id,
                                                             data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_put_succes(self):
        nuevo_training_plan_fake = {
            "day_food_plan": self.data_factory.name(),
            "food" : self.data_factory.word(),
            "calories" : self.data_factory.random_digit(),
            "value": self.data_factory.random_digit(),
            "id_eating_routine": None,

        }
        solicitud_crear_planEntrenamiento = self.client.put(self.endpoint_id,
                                                             data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertFalse(solicitud_crear_planEntrenamiento["message"] == "Se actualizarón correctamente los campos")

    def test_put_error(self):
        endpoint = "/training_plan/372a7"
        nuevo_training_plan_fake = {
            "day_food_plan": self.data_factory.name(),
            "food" : self.data_factory.word(),
            "calories" : self.data_factory.random_digit(),
            "value": self.data_factory.random_digit(),
            "id_eating_routine": None,

        }
        solicitud_crear_planEntrenamiento = self.client.put(endpoint,
                                                              data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertFalse(solicitud_crear_planEntrenamiento["message"] == "No se encontre el plan diario de comida")

    def test_put_error_message2(self):
        nuevo_training_plan_fake = {
            "day_food_plan": self.data_factory.name(),
            "food" : self.data_factory.word(),
            "calories" : self.data_factory.random_digit(),
            "value": self.data_factory.word(),
            "id_eating_routine": None,

        }
        solicitud_crear_planEntrenamiento = self.client.put(self.endpoint_id,
                                                              data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "No se pudo realizar la Actualización")

    
    def test_put_get_integrity_error(self):
        endpoint = "/day_food_training_plan/integrity_error"
        nuevo_training_plan_fake = {
            "day_food_plan": self.data_factory.name(),
            "food" : self.data_factory.word(),
            "calories" : self.data_factory.random_digit(),
            "value": self.data_factory.random_digit(),
            "id_eating_routine": None,

        }
        self.client.put(endpoint,
                        data= json.dumps(nuevo_training_plan_fake),
                        headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.client.get(endpoint,
                        data= '',
                        headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        

    def test_put_get_error(self):
        endpoint = "/day_food_training_plan/error"
        nuevo_training_plan_fake = {
            "day_food_plan": self.data_factory.name(),
            "food" : self.data_factory.word(),
            "calories" : self.data_factory.random_digit(),
            "value": self.data_factory.random_digit(),
            "id_eating_routine": None,

        }
        self.client.put(endpoint,
                        data= json.dumps(nuevo_training_plan_fake),
                        headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        
