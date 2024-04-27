import sqlalchemy
import json
from unittest import TestCase
from faker import Faker
from faker.generator import random
from app import app


class TestTrainingSession(TestCase):
    
    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()

    def testHealthCheck(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

