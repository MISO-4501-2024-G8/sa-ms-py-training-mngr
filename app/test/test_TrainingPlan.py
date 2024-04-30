import sqlalchemy
import json
from unittest import TestCase
from faker import Faker
from faker.generator import random
from app import app
from datetime import datetime
from unittest.mock import patch, MagicMock
from sqlalchemy.exc import IntegrityError
from decouple import config
import pytest
import sqlite3


class TestTrainingPlan(TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()
        self.endpoint = "/training_plan"
        self.endpoint_id = "/training_plan/3872a743"

    def test_post_not_None(self):
        nuevo_training_plan_fake = {
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks": self.data_factory.random_digit(),
            "lunes_enabled": self.data_factory.random_digit(),
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled": self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word(),
            "id_eating_routine": "123",
            "id_rest_routine": "123",
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
        get_all_plans = (self.client.get(self.endpoint, headers={"Content-Type": "application/json"}).get_data().decode("utf-8"))
        get_all_plans = json.loads(get_all_plans)
        print('test_all_fields 1: ',get_all_plans)
        nuevo_training_plan_fake = {
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks": self.data_factory.random_digit(),
            "lunes_enabled": self.data_factory.random_digit(),
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled": self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word(),
            "id_eating_routine": "123",
            "id_rest_routine": "123",
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
            == "Se pudo crear la sesión de entrenamiento exitosamante"
        )
        
    def test_post_error(self):
        nuevo_training_plan_fake = {
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks": self.data_factory.random_digit(),
            "lunes_enabled": self.data_factory.name(),
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled": self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word(),
            "id_eating_routine": "123",
            "id_rest_routine": "123",
        }
        solicitud_crear_planEntrenamiento = (
            self.client.post(
                self.endpoint + "123",
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
            == "No se pudo crear la sesión de entrenamiento"
        )

    def test_post_error(self):
        nuevo_training_plan_fake = {
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks": self.data_factory.random_digit(),
            "lunes_enabled": self.data_factory.name(),
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled": self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word(),
            "id_eating_routine": "123",
            "id_rest_routine": "123",
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
        print('test_post_error ',solicitud_crear_planEntrenamiento)
        solicitud_crear_planEntrenamiento = json.loads(
            solicitud_crear_planEntrenamiento
        )
        self.assertTrue(
            solicitud_crear_planEntrenamiento["message"]
            == "No se pudo crear la sesión de entrenamiento"
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
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks": self.data_factory.random_digit(),
            "lunes_enabled": self.data_factory.random_digit(),
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled": self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word(),
            "id_eating_routine": "123",
            "id_rest_routine": "123",
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
        print('test_get_succes ',solicitud_crear_planEntrenamiento)
        id_training_plan = solicitud_crear_planEntrenamiento["training_plan"]["id"]
        solicitud_crear_planEntrenamiento = (
            self.client.get(
                self.endpoint_id.replace("3872a743", id_training_plan),
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
            == "Se Encontro el plan de entranamiento buscado"
        )

    def test_get_error(self):
        endpoint = "/training_plan/372a7"
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
            == "No se ha encontrado coninsidencia del plan de entranamiento buscado"
        )

    def test_get_integrity_error(self):
        endpoint = "/training_plan/integrity_error"
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
    
    def test_get_error(self):
        # Configura el endpoint para la solicitud que generará la excepción IntegrityError
        endpoint = "/training_plan/error"
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
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks": self.data_factory.random_digit(),
            "lunes_enabled": self.data_factory.random_digit(),
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled": self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word(),
            "id_eating_routine": "123",
            "id_rest_routine": "123",
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
            "lunes_enabled": self.data_factory.random_digit(),
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled": self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word(),
            "id_eating_routine": "123",
            "id_rest_routine": "123",
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
        id_training_plan = solicitud_crear_planEntrenamiento["training_plan"]["id"]
        nuevo_training_plan_fake = {
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks": self.data_factory.random_digit(),
            "lunes_enabled": self.data_factory.random_digit(),
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled": self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word(),
            "id_eating_routine": "123",
            "id_rest_routine": "123",
        }
        solicitud_crear_planEntrenamiento = (
            self.client.put(
                self.endpoint_id.replace("3872a743", id_training_plan),
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
            "Se actualizarón correctamente los campos"
        )

    def test_put_error(self):
        endpoint = "/training_plan/372a7"
        nuevo_training_plan_fake = {
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks": self.data_factory.random_digit(),
            "lunes_enabled": self.data_factory.random_digit(),
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled": self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word(),
            "id_eating_routine": "123",
            "id_rest_routine": "123",
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
        self.assertTrue(
            solicitud_crear_planEntrenamiento["message"]
            == "El plan de entranamiento no existe"
        )

    def test_put_integrity_error(self):
        ttraining_plan_fake = {
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks": self.data_factory.random_digit(),
            "lunes_enabled": self.data_factory.random_digit(),
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled": self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word(),
            "id_eating_routine": "123",
            "id_rest_routine": "123",
        }
        endpoint = "/training_plan/integrity_error"
        solicitud_crear_planEntrenamiento = (
            self.client.put(
                endpoint,
                data=json.dumps(ttraining_plan_fake),
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
            "No se pudo realizar la Actualización"
        )

    def test_put_error(self):
        ttraining_plan_fake = {
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks": self.data_factory.random_digit(),
            "lunes_enabled": self.data_factory.random_digit(),
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled": self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word(),
            "id_eating_routine": "123",
            "id_rest_routine": "123",
        }
        endpoint = "/training_plan/error"
        solicitud_crear_planEntrenamiento = (
            self.client.put(
                endpoint,
                data=json.dumps(ttraining_plan_fake),
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
            "No se pudo realizar la Actualización"
        )

    def test_all_fields(self):
        nuevo_training_plan_fake = {
            "name": self.data_factory.name(),
            "description": self.data_factory.name(),
            "weeks": self.data_factory.random_digit(),
            "lunes_enabled": self.data_factory.random_digit(),
            "martes_enabled": self.data_factory.random_digit(),
            "miercoles_enabled": self.data_factory.random_digit(),
            "jueves_enabled": self.data_factory.random_digit(),
            "viernes_enabled": self.data_factory.random_digit(),
            "typePlan": self.data_factory.word(),
            "sport": self.data_factory.word(),
            "id_eating_routine": "123",
            "id_rest_routine": "123",
        }
        solicitud_crear_plan_entrenamiento = (
            self.client.post(
                self.endpoint,
                data=json.dumps(nuevo_training_plan_fake),
                headers={"Content-Type": "application/json"},
            )
            .get_data()
            .decode("utf-8")
        )
        solicitud_crear_plan_entrenamiento = json.loads(
            solicitud_crear_plan_entrenamiento
        )
        id_training_plan = solicitud_crear_plan_entrenamiento["training_plan"]["id"]
        nuevo_objetivo_plan = {
            "day": self.data_factory.name(),
            "objective_repeats": self.data_factory.random_digit(),
            "type_objective": self.data_factory.random_digit(),
            "id_routine": id_training_plan,
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
        get_all_plans = (self.client.get(self.endpoint, headers={"Content-Type": "application/json"}).get_data().decode("utf-8"))
        get_all_plans = json.loads(get_all_plans)
        print('test_all_fields 3: --------------',get_all_plans)