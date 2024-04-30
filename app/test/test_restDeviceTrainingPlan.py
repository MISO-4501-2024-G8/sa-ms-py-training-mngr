import sqlalchemy
import json
from unittest import TestCase
from faker import Faker
from faker.generator import random
from app import app
from datetime import datetime
from unittest.mock import patch, MagicMock
from sqlalchemy.exc import IntegrityError


class TestrestDeviceTrainingPlan(TestCase):
    
    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()
        self.endpoint = "/rest_device_training_plan"
        self.endpoint_id = "/rest_device_training_plan/499d9c17"


    def test_post_not_None(self):
        nuevo_training_plan_fake = {
            "rest_device_name": self.data_factory.name(),
            "rest_device_qty" : self.data_factory.random_digit() ,
            "rental_value": "5.2478",
            "id_rest_routine": "b76ff61a" ,
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_post_succes(self):
        nuevo_training_plan_fake = {
            "rest_device_name": self.data_factory.name(),
            "rest_device_qty" : self.data_factory.random_digit() ,
            "rental_value": 5.2478,
            "id_rest_routine": "b76ff61a" ,
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        print("solicitud_crear_planEntrenamiento::::::", solicitud_crear_planEntrenamiento)
        self.assertFalse(solicitud_crear_planEntrenamiento["message"] == "Se pudo crear el dispositio de descanso de la rutina de descanso de la sesion de entrenamiento")


    def test_post_error(self):
        nuevo_training_plan_fake = {
            "rest_device_name": self.data_factory.name(),
            "rest_device_qty" : self.data_factory.random_digit() ,
            "rental_value": self.data_factory.name(),
            "id_rest_routine": "b76ff61a" ,
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        print(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "No se pudo crear el dispositio de descanso de la rutina de descanso de la sesion de entrenamiento exitosamante")

    def test_get_not_None(self):
        solicitud_crear_planEntrenamiento = self.client.get(self.endpoint_id,
                                                             data= '',
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_get_succes(self):
        nuevo_training_plan_fake = {
            "rest_device_name": self.data_factory.name(),
            "rest_device_qty" : self.data_factory.random_digit() ,
            "rental_value": 5.2478,
            "id_rest_routine": "b76ff61a" ,
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        id_rest_device_training_plan = solicitud_crear_planEntrenamiento["rest_device"]["id"]
        solicitud_crear_planEntrenamiento = self.client.get(self.endpoint_id.replace("499d9c17", id_rest_device_training_plan),
                                                             data= '',
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "Se Encontro el dispositivo de descanso buscado")

    def test_get_error(self):
        endpoint = "/rest_device_training_plan/123"
        solicitud_crear_planEntrenamiento = self.client.get(endpoint,
                                                             data= '',
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "No se ha encontrado el dispositivo de descanso buscado")

    def test_put_not_None(self):
        nuevo_training_plan_fake = {
            "rest_device_name": self.data_factory.name(),
            "rest_device_qty" : self.data_factory.random_digit() ,
            "rental_value": "5.2478",
            "id_rest_routine": "b76ff61a" ,
        }
        solicitud_crear_planEntrenamiento = self.client.put(self.endpoint_id,
                                                             data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_put_succes(self):
        nuevo_training_plan_fake = {
            "rest_device_name": self.data_factory.name(),
            "rest_device_qty" : self.data_factory.random_digit() ,
            "rental_value": 5.2478,
            "id_rest_routine": "b76ff61a" ,
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        id_rest_device_training_plan = solicitud_crear_planEntrenamiento["rest_device"]["id"]
        nuevo_training_plan_fake = {
            "rest_device_name": self.data_factory.name(),
            "rest_device_qty" : self.data_factory.random_digit() ,
            "rental_value": "5.2478",
            "id_rest_routine": "b76ff61a" ,
        }
        solicitud_crear_planEntrenamiento = self.client.put(self.endpoint_id.replace("499d9c17", id_rest_device_training_plan),
                                                             data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "Se actualizarón correctamente los campos")

    def test_put_error(self):
        endpoint = "/training_plan/372a7"
        nuevo_training_plan_fake = {
            "rest_device_name": self.data_factory.name(),
            "rest_device_qty" : self.data_factory.random_digit() ,
            "rental_value": "5.2478",
            "id_rest_routine": "b76ff61a" ,
        }
        solicitud_crear_planEntrenamiento = self.client.put(endpoint,
                                                              data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertFalse(solicitud_crear_planEntrenamiento["message"] == "El plan de entranamiento no existe")
    
    def test_put_get_integrity_error(self):
        endpoint = "/rest_device_training_plan/integrity_error"
        self.client.put(endpoint,
                        data= {},
                        headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.client.get(endpoint,
                        data= '',
                        headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")



