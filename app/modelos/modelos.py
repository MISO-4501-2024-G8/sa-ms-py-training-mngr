from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from decimal import Decimal as D 
import sqlalchemy.types as types
from sqlalchemy.orm import relationship

class SqliteNumeric(types.TypeDecorator):     
    impl = types.String     
    def load_dialect_impl(self, dialect):         
        return dialect.type_descriptor(types.VARCHAR(100))     
    def process_bind_param(self, value, dialect):         
        return str(value)     
    def process_result_value(self, value, dialect):         
        return D(value)  


db = SQLAlchemy()

class TrainingPlan(db.Model):
    __tablename__ = 'training_plan'

    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255))
    description  = db.Column(db.String(255))
    weeks = db.Column(db.Integer)
    lunes_enabled = db.Column(db.Integer)
    martes_enabled = db.Column(db.Integer)
    miercoles_enabled = db.Column(db.Integer)
    jueves_enabled = db.Column(db.Integer)
    viernes_enabled = db.Column(db.Integer)
    typePlan = db.Column(db.String(255))
    sport = db.Column(db.String(255))
    id_eating_routine = db.Column(db.String(255))
    id_rest_routine = db.Column(db.String(255))
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

class RestRoutine(db.Model):
    __tablename__ = 'rest_routine'

    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255))
    description  = db.Column(db.String(255))
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

class Objective(db.Model):
    __tablename__ = 'objective'

    id = db.Column(db.String(255), primary_key=True)
    id_routine = db.Column(db.String(255))
    day = db.Column(db.String(255))
    repeats = db.Column(db.Integer)
    type_objective = db.Column(db.String(255))
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

class RiskAlerts(db.Model):
    __tablename__ = 'risk_alerts'

    training_plan_id = db.Column(db.String(255), primary_key=True)
    stop_training = db.Column(db.Integer)
    notifications = db.Column(db.Integer)
    enable_phone = db.Column(db.Integer)
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)


class EatingRoutine(db.Model):
    __tablename__ = 'eating_routine'

    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255))
    description  = db.Column(db.String(255))
    weeks = db.Column(db.Integer)
    max_weight = db.Column(db.Float)
    min_weight = db.Column(db.Float)
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)


class DayFoodPlan(db.Model):
    __tablename__ = 'day_food_plan'

    id = db.Column(db.String(255), primary_key=True)
    id_eating_routine = db.Column(db.String(255))
    day = db.Column(db.String(255))
    food = db.Column(db.String(255))
    qty = db.Column(db.Integer)
    calories = db.Column(db.Integer)
    value = db.Column(db.Float)
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

class Instruction(db.Model):
    __tablename__ = 'instruction'

    id = db.Column(db.String(255), primary_key=True)
    id_objective = db.Column(db.String(255))
    instruction_description = db.Column(db.String(255))
    instruction_time = db.Column(db.Integer)
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

class RestDevice(db.Model):
    __tablename__ = 'rest_device'

    id = db.Column(db.String(255), primary_key=True)
    id_rest_routine = db.Column(db.String(255))
    name = db.Column(db.String(255))
    qty = db.Column(db.Integer)
    rental_value = db.Column(db.Float)
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

class TrainingPlanSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TrainingPlan
        include_relationships = True
        load_instance = True

class EatingRoutineSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = EatingRoutine
        include_relationships = True
        load_instance = True

class ObjectiveSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Objective
        include_relationships = True
        load_instance = True

class RestRoutineSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RestRoutine
        include_relationships = True
        load_instance = True

class RiskAlertsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RiskAlerts
        include_relationships = True
        load_instance = True

class DayFoodPlanSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DayFoodPlan
        include_relationships = True
        load_instance = True

class InstructionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Instruction
        include_relationships = True
        load_instance = True

class RestDeviceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RestDevice
        include_relationships = True
        load_instance = True

