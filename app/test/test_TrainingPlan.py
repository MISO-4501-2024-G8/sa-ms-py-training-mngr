import sqlalchemy
import json
from unittest import TestCase
from faker import Faker
from faker.generator import random
from app import app


class TestTrainingPlan(TestCase):
    
    def setUp(self):
        self.data_factory = Faker()
        self.client = app.test_client()


    def test_post_not_None(self):
        return None

