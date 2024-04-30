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
        self.endpoint = "/risk_alerts_training_plan"
        self.endpoint_id = "/risk_alerts_training_plan/3ae94e42"

    def test_post_not_None(self):
        nuevo_training_plan_fake = {
            "stop_training": self.data_factory.random_digit(),
            "notifications": None,
            "enable_phone": self.data_factory.random_digit(),
            "id_training_plan": None,
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
            "id_eating_routine": self.data_factory.name(),
            "id_rest_routine": self.data_factory.name(),
        }
        solicitud_crear_planEntrenamiento = self.client.post("/training_plan",
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        id_training_plan = json.loads(solicitud_crear_planEntrenamiento)["training_plan"]["id"]
        nuevo_training_plan_fake = {
            "stop_training": self.data_factory.random_digit(),
            "notifications": None,
            "enable_phone": self.data_factory.random_digit(),
            "id_training_plan": id_training_plan,
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
            == "Se pudo crear la alerta de riesgo de la sesion de entrenamiento exitosamante"
        )

    def test_post_error(self):
        nuevo_training_plan_fake = {
            "stop_training": self.data_factory.random_digit(),
            "notifications": None,
            "enable_phone": self.data_factory.name(),
            "id_training_plan": None,
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
            == "No se pudo crear la alerta de riesgo de la sesion de entrenamiento exitosamante"
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
        solicitud_crear_planEntrenamiento = (
            self.client.get(
                self.endpoint_id, data="", headers={"Content-Type": "application/json"}
            )
            .get_data()
            .decode("utf-8")
        )
        solicitud_crear_planEntrenamiento = json.loads(
            solicitud_crear_planEntrenamiento
        )
        self.assertFalse(
            solicitud_crear_planEntrenamiento["message"]
            == "Se Encontro el plan de entranamiento buscado"
        )

    def test_get_error(self):
        endpoint = "/risk_alerts_training_plan/123"
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
        self.assertFalse(
            solicitud_crear_planEntrenamiento["message"]
            == "No se ha encontrado al  alerta de riesgo buscada"
        )

    def test_put_not_None(self):
        nuevo_training_plan_fake = {
            "stop_training": self.data_factory.random_digit(),
            "notifications": None,
            "enable_phone": self.data_factory.random_digit(),
            "id_training_plan": None,
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
            "id_eating_routine": self.data_factory.name(),
            "id_rest_routine": self.data_factory.name(),
        }
        solicitud_crear_planEntrenamiento = self.client.post("/training_plan",
                                                             data = json.dumps(nuevo_training_plan_fake),
                                                             headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        id_training_plan = json.loads(solicitud_crear_planEntrenamiento)["training_plan"]["id"]
        nuevo_training_plan_fake = {
            "stop_training": self.data_factory.random_digit(),
            "notifications": None,
            "enable_phone": self.data_factory.random_digit(),
            "id_training_plan": id_training_plan,
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
        id_risk_alert = solicitud_crear_planEntrenamiento["risk_alerts"]["training_plan_id"]
        nuevo_training_plan_fake = {
            "stop_training": self.data_factory.random_digit(),
            "notifications": None,
            "enable_phone": self.data_factory.random_digit(),
        }
        solicitud_crear_planEntrenamiento = (
            self.client.put(
                self.endpoint_id.replace("3ae94e42", id_risk_alert),
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
            "stop_training": self.data_factory.random_digit(),
            "notifications": None,
            "enable_phone": self.data_factory.random_digit(),
            "id_training_plan": None,
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
            == "No se encontro la alerta de riesgo buscada"
        )

    def test_put_get_integrity_error(self):
        endpoint = "/risk_alerts_training_plan/integrity_error"
        self.client.put(endpoint,
                        data= {},
                        headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")
        self.client.get(endpoint,
                        data= '',
                        headers={'Content-Type': 'application/json'}).get_data().decode("utf-8")