import sqlalchemy
import json
from unittest import TestCase
from faker import Faker
from faker.generator import random
from app import app
from datetime import datetime


class TestEatingRoutineTrainingPlan(TestCase):
    
    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()
        self.endpoint = "/eating_routing_training_plan"
        self.endpoint_id = "/eating_routing_training_plan/b76ff61a"


    def test_post_not_None(self):
        nuevo_training_plan_fake = {
            "eating_routine_name": self.data_factory.name(),
            "eating_routine_description" : self.data_factory.word(),
            "eating_routine_weeks" :self.data_factory.random_digit(),
            "max_weight": 5.5,
            "min_weight": 6.6
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_post_succes(self):
        nuevo_training_plan_fake = {
            "eating_routine_name": self.data_factory.name(),
            "eating_routine_description" : self.data_factory.word(),
            "eating_routine_weeks" :self.data_factory.random_digit(),
            "max_weight": 5.5,
            "min_weight": 6.6
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "Se pudo crear la rutina de alimentacion de la sesion de entrenamiento exitosamante")


    def test_post_error(self):
        nuevo_training_plan_fake = {
            "eating_routine_name": self.data_factory.name(),
            "eating_routine_description" : self.data_factory.word(),
            "eating_routine_weeks" :self.data_factory.random_digit(),
            "max_weight": self.data_factory.word(),
            "min_weight": 6.6
        }
        solicitud_crear_planEntrenamiento = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "No se pudo crear la rutina de alimentacion de la sesion de entrenamiento exitosamante")

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
        self.assertFalse(solicitud_crear_planEntrenamiento["message"] == "Se Encontro la rutina de alimentacion buscada")

    def test_get_error(self):
        endpoint = "/eating_routing_training_plan/123"
        solicitud_crear_planEntrenamiento = self.client.get(endpoint,
                                                             data= '',
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertTrue(solicitud_crear_planEntrenamiento["message"] == "No se ha encontrado la rutina de alimentacion buscada")

    def test_put_not_None(self):
        nuevo_training_plan_fake = {
            "eating_routine_name": self.data_factory.name(),
            "eating_routine_description" : self.data_factory.word(),
            "eating_routine_weeks" :self.data_factory.random_digit(),
            "max_weight": 5.5,
            "min_weight": 6.6
        }
        solicitud_crear_planEntrenamiento = self.client.put(self.endpoint_id,
                                                             data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_put_succes(self):
        nuevo_training_plan_fake = {
            "eating_routine_name": self.data_factory.name(),
            "eating_routine_description" : self.data_factory.word(),
            "eating_routine_weeks" :self.data_factory.random_digit(),
            "max_weight": 5.5,
            "min_weight": 6.6
        }
        solicitud_crear_planEntrenamiento = self.client.put(self.endpoint_id,
                                                             data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertFalse(solicitud_crear_planEntrenamiento["message"] == "Se actualizarón correctamente los campos")

    def test_put_error(self):
        endpoint = "/training_plan/372a7"
        nuevo_training_plan_fake = {
            "eating_routine_name": self.data_factory.name(),
            "eating_routine_description" : self.data_factory.word(),
            "eating_routine_weeks" :self.data_factory.random_digit(),
            "max_weight": 5.5,
            "min_weight": 6.6
        }
        solicitud_crear_planEntrenamiento = self.client.put(endpoint,
                                                              data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertFalse(solicitud_crear_planEntrenamiento["message"] == "No se econtro la rutina de alimentacion buscada")

    def test_put_error_mesaage2(self):
        nuevo_training_plan_fake = {
            "eating_routine_name": self.data_factory.name(),
            "eating_routine_description" : self.data_factory.random_digit(),
            "eating_routine_weeks" :self.data_factory.random_digit(),
            "max_weight": 5.5,
            "min_weight": 6.6
        }
        solicitud_crear_planEntrenamiento = self.client.put(self.endpoint_id,
                                                              data= json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_planEntrenamiento = json.loads(solicitud_crear_planEntrenamiento)
        self.assertFalse(solicitud_crear_planEntrenamiento["message"] == "No se pudo realizar la Actualización")
    
    def test_put_get_integrity_error(self):
        endpoint = "/eating_routing_training_plan/integrity_error"
        self.client.put(endpoint,
                        data= {},
                        headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.client.get(endpoint,
                        data= '',
                        headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
    
    def test_put_get_ex_error(self):
        endpoint = "/eating_routing_training_plan/error"
        self.client.put(endpoint,
                        data= {},
                        headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.client.get(endpoint,
                        data= '',
                        headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")


    def test_all_fields(self):
        nuevo_training_plan_fake = {
            "eating_routine_name": self.data_factory.name(),
            "eating_routine_description" : self.data_factory.word(),
            "eating_routine_weeks" :self.data_factory.random_digit(),
            "max_weight": 5.5,
            "min_weight": 6.6
        }
        solicitud_crear_plan_alimentacion = self.client.post(self.endpoint,
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_plan_alimentacion = json.loads(solicitud_crear_plan_alimentacion)
        print('test_all_fields 1: --------------',solicitud_crear_plan_alimentacion)
        id_eating_routine = solicitud_crear_plan_alimentacion["eating_routine"]["id"]
        nuevo_training_food_fake = {
            "day_food_plan": self.data_factory.name(),
            "food" : self.data_factory.word(),
            "qty": self.data_factory.random_digit(),
            "calories" : self.data_factory.random_digit(),
            "value": self.data_factory.random_digit(),
            "id_eating_routine": id_eating_routine,

        }
        solicitud_crear_alimento = self.client.post('/day_food_training_plan',
                                                    data = json.dumps(nuevo_training_food_fake),
                                                    headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        solicitud_crear_alimento = json.loads(solicitud_crear_alimento)
        print('test_all_fields 2: --------------',solicitud_crear_alimento)
        get_all_eating_routines = (self.client.get(self.endpoint, headers={"Content-Type": "application/json"}).get_data().decode("utf-8"))
        get_all_eating_routines = json.loads(get_all_eating_routines)
        print('test_all_fields 3: --------------',get_all_eating_routines)
        


