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
        self.endpoint_id = "/rest_routine_training_plan/b76ff61a"

    def test_post_not_None(self):
        nuevo_training_plan_fake = {
            "rest_routine_name": self.data_factory.name(),
            "rest_routine_description": self.data_factory.name(),
        }
        solicitud_crear_planEntrenamiento = (
            self.client.post(
                self.endpoint,
                data=json.dumps(nuevo_training_plan_fake),
                headers={"Content-Type": "application/json"},
            )
            .get_data()
            .decode("utf-8")
        )
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_post_succes(self):
        nuevo_training_plan_fake = {
            "rest_routine_name": self.data_factory.name(),
            "rest_routine_description": self.data_factory.name(),
        }
        solicitud_crear_planEntrenamiento = (
            self.client.post(
                self.endpoint,
                data=json.dumps(nuevo_training_plan_fake),
                headers={"Content-Type": "application/json"},
            )
            .get_data()
            .decode("utf-8")
        )
        solicitud_crear_planEntrenamiento = json.loads(
            solicitud_crear_planEntrenamiento
        )
        self.assertTrue(
            solicitud_crear_planEntrenamiento["message"]
            == "Se pudo crear la rutina de descanso de la sesion de entrenamiento exitosamante"
        )

    def test_post_error(self):
        nuevo_training_plan_fake = {
            "rest_routine_name": self.data_factory.name(),
            "rest_routine_description": None,
        }
        solicitud_crear_planEntrenamiento = (
            self.client.post(
                self.endpoint,
                data=json.dumps(nuevo_training_plan_fake),
                headers={"Content-Type": "application/json"},
            )
            .get_data()
            .decode("utf-8")
        )
        solicitud_crear_planEntrenamiento = json.loads(
            solicitud_crear_planEntrenamiento
        )
        print(solicitud_crear_planEntrenamiento)
        self.assertFalse(
            solicitud_crear_planEntrenamiento["message"]
            == "No se pudo crear la rutina de descanso de la sesion de entrenamiento exitosamante"
        )

    def test_get_not_None(self):
        solicitud_crear_planEntrenamiento = (
            self.client.get(
                self.endpoint_id, data="", headers={"Content-Type": "application/json"}
            )
            .get_data()
            .decode("utf-8")
        )
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_get_succes(self):
        nuevo_training_plan_fake = {
            "rest_routine_name": self.data_factory.name(),
            "rest_routine_description": self.data_factory.name(),
        }
        solicitud_crear_planEntrenamiento = (
            self.client.post(
                self.endpoint,
                data=json.dumps(nuevo_training_plan_fake),
                headers={"Content-Type": "application/json"},
            )
            .get_data()
            .decode("utf-8")
        )
        id_rest_routine = json.loads(solicitud_crear_planEntrenamiento)["rest_routine"][
            "id"
        ]
        solicitud_crear_planEntrenamiento = (
            self.client.get(
                self.endpoint_id.replace("b76ff61a", id_rest_routine),
                data="",
                headers={"Content-Type": "application/json"},
            )
            .get_data()
            .decode("utf-8")
        )
        solicitud_crear_planEntrenamiento = json.loads(
            solicitud_crear_planEntrenamiento
        )
        self.assertTrue(
            solicitud_crear_planEntrenamiento["message"]
            == "Se Encontro la rutina de descanso buscada"
        )

    def test_get_error(self):
        endpoint = "/rest_routine_training_plan/123"
        solicitud_crear_planEntrenamiento = (
            self.client.get(
                endpoint, data="", headers={"Content-Type": "application/json"}
            )
            .get_data()
            .decode("utf-8")
        )
        solicitud_crear_planEntrenamiento = json.loads(
            solicitud_crear_planEntrenamiento
        )
        self.assertTrue(
            solicitud_crear_planEntrenamiento["message"]
            == "No se ha encontrado la rutina de descanso buscada"
        )

    def test_put_not_None(self):
        nuevo_training_plan_fake = {
            "rest_routine_name": self.data_factory.name(),
            "rest_routine_description": self.data_factory.name(),
        }
        solicitud_crear_planEntrenamiento = (
            self.client.put(
                self.endpoint_id,
                data=json.dumps(nuevo_training_plan_fake),
                headers={"Content-Type": "application/json"},
            )
            .get_data()
            .decode("utf-8")
        )
        self.assertIsNotNone(solicitud_crear_planEntrenamiento)

    def test_put_succes(self):
        nuevo_training_plan_fake = {
            "rest_routine_name": self.data_factory.name(),
            "rest_routine_description": self.data_factory.name(),
        }
        solicitud_crear_planEntrenamiento = (
            self.client.post(
                self.endpoint,
                data=json.dumps(nuevo_training_plan_fake),
                headers={"Content-Type": "application/json"},
            )
            .get_data()
            .decode("utf-8")
        )
        id_rest_routine = json.loads(solicitud_crear_planEntrenamiento)["rest_routine"][
            "id"
        ]
        nuevo_training_plan_fake = {
            "rest_routine_name": self.data_factory.name(),
            "rest_routine_description": self.data_factory.name(),
        }
        solicitud_crear_planEntrenamiento = (
            self.client.put(
                self.endpoint_id.replace("b76ff61a", id_rest_routine),
                data=json.dumps(nuevo_training_plan_fake),
                headers={"Content-Type": "application/json"},
            )
            .get_data()
            .decode("utf-8")
        )
        solicitud_crear_planEntrenamiento = json.loads(
            solicitud_crear_planEntrenamiento
        )
        self.assertTrue(
            solicitud_crear_planEntrenamiento["message"]
            == "Se actualizarón correctamente los campos"
        )

    def test_put_error(self):
        endpoint = "/training_plan/372a7"
        nuevo_training_plan_fake = {
            "rest_routine_name": self.data_factory.name(),
            "rest_routine_description": self.data_factory.name(),
        }
        solicitud_crear_planEntrenamiento = (
            self.client.put(
                endpoint,
                data=json.dumps(nuevo_training_plan_fake),
                headers={"Content-Type": "application/json"},
            )
            .get_data()
            .decode("utf-8")
        )
        solicitud_crear_planEntrenamiento = json.loads(
            solicitud_crear_planEntrenamiento
        )
        self.assertFalse(
            solicitud_crear_planEntrenamiento["message"]
            == "El plan de entranamiento no existe"
        )

    def test_put_error_mesaage2(self):
        nuevo_training_plan_fake = {
            "rest_routine_name": self.data_factory.name(),
            "rest_routine_description": self.data_factory.random_digit(),
        }
        solicitud_crear_planEntrenamiento = (
            self.client.put(
                self.endpoint_id,
                data=json.dumps(nuevo_training_plan_fake),
                headers={"Content-Type": "application/json"},
            )
            .get_data()
            .decode("utf-8")
        )
        solicitud_crear_planEntrenamiento = json.loads(
            solicitud_crear_planEntrenamiento
        )
        self.assertFalse(
            solicitud_crear_planEntrenamiento["message"]
            == "No se pudo realizar la Actualización"
        )

    def test_put_get_integrity_error(self):
        endpoint = "/rest_routine_training_plan/integrity_error"
        self.client.put(
            endpoint, data={}, headers={"Content-Type": "application/json"}
        ).get_data().decode("utf-8")
        self.client.get(
            endpoint, data="", headers={"Content-Type": "application/json"}
        ).get_data().decode("utf-8")
    
    def test_all_fields(self):
        nuevo_rest_plan_fake = {
            "rest_routine_name": self.data_factory.name(),
            "rest_routine_description": self.data_factory.name(),
        }
        solicitud_crear_plan_rest = (
            self.client.post(
                self.endpoint,
                data=json.dumps(nuevo_rest_plan_fake),
                headers={"Content-Type": "application/json"},
            )
            .get_data()
            .decode("utf-8")
        )
        solicitud_crear_plan_rest = json.loads(solicitud_crear_plan_rest)
        print('solicitud_crear_plan_rest 1: --------------',solicitud_crear_plan_rest)
        id_restroutine = solicitud_crear_plan_rest["rest_routine"]["id"]
        nuevo_objetivo_plan = {
            "day": self.data_factory.name(),
            "objective_repeats": self.data_factory.random_digit(),
            "type_objective": self.data_factory.random_digit(),
            "id_routine": id_restroutine,
        }
        solicitud_crear_objetivo = (
            self.client.post(
                "/objetive_training_plan",
                data=json.dumps(nuevo_objetivo_plan),
                headers={"Content-Type": "application/json"},
            )
            .get_data()
            .decode("utf-8")
        )
        solicitud_crear_objetivo = json.loads(
            solicitud_crear_objetivo
        )
        print('test_all_fields 2: --------------',solicitud_crear_objetivo)
        get_all_routines = (self.client.get(self.endpoint, headers={"Content-Type": "application/json"}).get_data().decode("utf-8"))
        get_all_routines = json.loads(get_all_routines)
        print('test_all_fields 3: --------------',get_all_routines)


    def test_put_get_integrity_error(self):
        endpoint = "/rest_routine_training_plan/integrity_error"
        self.client.put(endpoint,
                        data= {},
                        headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.client.get(endpoint,
                        data= '',
                        headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
    
    def test_put_get_ex_error(self):
        endpoint = "/rest_routine_training_plan/error"
        self.client.put(endpoint,
                        data= {},
                        headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.client.get(endpoint,
                        data= '',
                        headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")