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
        self.endpoint_id = "/objetive_training_plan/fcd6e4af"

    def test_post_not_None(self):
        nuevo_training_plan_fake = {
            "day": self.data_factory.name(),
            "objective_repeats": self.data_factory.random_digit(),
            "type_objective": self.data_factory.random_digit(),
            "id_routine": "b76ff61a",
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
            "day": self.data_factory.name(),
            "objective_repeats": self.data_factory.random_digit(),
            "type_objective": self.data_factory.random_digit(),
            "id_routine": "b76ff61a",
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
            == "Se pudo crear el objetivo sesion exitosamante"
        )

    def test_post_error(self):
        nuevo_training_plan_fake = {
            "day": self.data_factory.name(),
            "objective_repeats": self.data_factory.name(),
            "type_objective": self.data_factory.name(),
            "id_routine": "b76ff61a",
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
            == "No se pudo crear el objetivo sesion"
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
            "day": self.data_factory.name(),
            "objective_repeats": self.data_factory.random_digit(),
            "type_objective": self.data_factory.random_digit(),
            "id_routine": "b76ff61a",
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
        id_objective = json.loads(solicitud_crear_planEntrenamiento)["objective"]["id"]
        solicitud_crear_planEntrenamiento = (
            self.client.get(
                self.endpoint_id.replace("fcd6e4af", id_objective),
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
            == "Se Encontro el objetivo del plan de entranamiento buscado"
        )

    def test_get_error(self):
        endpoint = "/objetive_training_plan/noexiste"
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

        self.assertEqual(
            solicitud_crear_planEntrenamiento["message"],
            "No se ha encontrado coninsidencia del objetivo del plan entranamiento buscado"
        )

    def test_get_integrity_error(self):
        endpoint = "/objetive_training_plan/integrity_error"
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

        self.assertEqual(
            solicitud_crear_planEntrenamiento["message"],
            "No se pudo realizar la Actualización"
        )
    def test_get_ex_error(self):
        endpoint = "/objetive_training_plan/error"
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

        self.assertEqual(
            solicitud_crear_planEntrenamiento["message"],
            "No se pudo realizar la Actualización"
        )

    def test_put_not_None(self):
        nuevo_training_plan_fake = {
            "day": self.data_factory.name(),
            "objective_repeats": self.data_factory.random_digit(),
            "type_objective": self.data_factory.random_digit(),
            "id_routine": "b76ff61a",
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
            "day": self.data_factory.name(),
            "objective_repeats": self.data_factory.random_digit(),
            "type_objective": self.data_factory.random_digit(),
            "id_routine": "b76ff61a",
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
        id_objective = json.loads(solicitud_crear_planEntrenamiento)["objective"]["id"]
        nuevo_training_plan_fake = {
            "day": self.data_factory.name(),
            "objective_repeats": self.data_factory.random_digit(),
            "type_objective": self.data_factory.random_digit(),
            "id_routine": "b76ff61a",
        }
        solicitud_crear_planEntrenamiento = (
            self.client.put(
                self.endpoint_id.replace("fcd6e4af", id_objective),
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
            "day": self.data_factory.name(),
            "objective_repeats": self.data_factory.random_digit(),
            "type_objective": self.data_factory.random_digit(),
            "id_routine": "b76ff61a",
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
            == "El objetivo de plan deportivo no existe"
        )

    def test_put_integrity_error(self):
        endpoint = "/objetive_training_plan/integrity_error"
        nuevo_training_plan_fake = {
            "day": self.data_factory.name(),
            "objective_repeats": self.data_factory.random_digit(),
            "type_objective": self.data_factory.random_digit(),
            "id_routine": "b76ff61a",
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
        self.assertEqual(
            solicitud_crear_planEntrenamiento["message"],
            "No se pudo realizar la Actualización",
        )
        self.client.get(
            endpoint,
            data=json.dumps(nuevo_training_plan_fake),
            headers={"Content-Type": "application/json"},
        ).get_data().decode("utf-8")

    def test_put_error(self):
        endpoint = "/objetive_training_plan/error"
        nuevo_training_plan_fake = {
            "day": self.data_factory.name(),
            "objective_repeats": self.data_factory.random_digit(),
            "type_objective": self.data_factory.random_digit(),
            "id_routine": "b76ff61a",
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
        self.assertEqual(
            solicitud_crear_planEntrenamiento["message"],
            "No se pudo realizar la Actualización",
        )
        self.client.get(
            endpoint,
            data=json.dumps(nuevo_training_plan_fake),
            headers={"Content-Type": "application/json"},
        ).get_data().decode("utf-8")
