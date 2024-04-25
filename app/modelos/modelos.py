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
    type_plan = db.Column(db.String(255))
    sport = db.Column(db.String(255))
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

    objectives = db.relationship('Objective', backref='training_plan', lazy=True)

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

    id_training_plan = db.Column(db.String(255), db.ForeignKey('training_plan.id'))
    dayFoodPlanes = db.relationship('DayFoodPlan', backref='eating_routine', lazy=True)


class Objective(db.Model):
    __tablename__ = 'objective'

    id = db.Column(db.String(255), primary_key=True)
    day = db.Column(db.String(255))
    repeats = db.Column(db.Integer)
    type_objective = db.Column(db.String(255))
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

    id_training_plan = db.Column(db.String(255), db.ForeignKey('training_plan.id'))
    instructions = db.relationship('Instruction', backref='objective', lazy=True)
    id_rest_routine = db.Column(db.String(255), db.ForeignKey('rest_routine.id'))

class RestRoutine(db.Model):
    __tablename__ = 'rest_routine'

    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255))
    description  = db.Column(db.String(255))
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

    id_training_plan = db.Column(db.String(255), db.ForeignKey('training_plan.id'))
    objectives = db.relationship('Objective', backref='rest_routine', lazy=True)
    restDevices = db.relationship('RestDevice', backref='rest_routine', lazy=True)

class RiskAlerts(db.Model):
    __tablename__ = 'risk_alerts'

    id = db.Column(db.String(255), primary_key=True)
    stop_training = db.Column(db.Integer)
    notifications = db.Column(db.Integer)
    enable_phone = db.Column(db.Integer)
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

    id_training_plan = db.Column(db.String(255), db.ForeignKey('training_plan.id'))

class DayFoodPlan(db.Model):
    __tablename__ = 'day_food_plan'

    id = db.Column(db.String(255), primary_key=True)
    day = db.Column(db.String(255))
    food = db.Column(db.String(255))
    qty = db.Column(db.Integer)
    calories = db.Column(db.Integer)
    value = db.Column(db.Float)
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

    id_eating_routine = db.Column(db.String(255), db.ForeignKey('eating_routine.id'))

class Instruction(db.Model):
    __tablename__ = 'instruction'

    id = db.Column(db.String(255), primary_key=True)
    instruction_description = db.Column(db.String(255))
    instruction_time = db.Column(db.Integer)
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

    id_objective = db.Column(db.String(255), db.ForeignKey('objective.id'))

class RestDevice(db.Model):
    __tablename__ = 'rest_device'

    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255))
    qty = db.Column(db.Integer)
    rental_value = db.Column(db.Float)
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

    id_rest_routine = db.Column(db.String(255), db.ForeignKey('rest_routine.id'))

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


class TrainingSession(db.Model):
    __tablename__ = 'training_session'

    id = db.Column(db.String(255), primary_key=True)
    id_sport_user = db.Column(db.String(255))
    id_event  = db.Column(db.String(255))
    event_category = db.Column(db.String(50))
    sport_type = db.Column(db.String(50))
    session_date = db.Column(db.DateTime, default=datetime.now)
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)


class SportsSession(db.Model):
    __tablename__ = 'sports_session'

    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(50))
    week = db.Column(db.Integer)
    day = db.Column(db.String(50))
    repeats = db.Column(db.Integer)
    location = db.Column(db.String(50))
    total_time = db.Column(db.Integer)
    session_event = db.Column(db.DateTime, default=datetime.now)
    qty_objectives_achived = db.Column(db.Integer)
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

    id_training_session = db.Column(db.Integer, db.ForeignKey('training_session.id'))

class ObjectiveInstruction(db.Model):
    __tablename__ = 'objective_instruction'

    id = db.Column(db.String(255), primary_key=True)
    instruction_description = db.Column(db.String(50))
    instruction_time = db.Column(db.Integer)
    target_achieved = db.Column(db.Integer)
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

    id_sport_session = db.Column(db.Integer, db.ForeignKey('sports_session.id'))

class TrainingSessionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TrainingSession
        include_relationships = True
        load_instance = True

class SportsSessionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SportsSession
        include_relationships = True
        load_instance = True

class ObjectiveInstructionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ObjectiveInstruction
        include_relationships = True
        load_instance = True
