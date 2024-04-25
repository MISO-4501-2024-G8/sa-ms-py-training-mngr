from dataclasses import dataclass

from datetime import datetime
import requests
from flask import request
from flask_jwt_extended import create_access_token, jwt_required
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from modelos.modelos import (
    TrainingSession,
    SportsSession,
    ObjectiveInstruction,
    TrainingPlan,
    EatingRoutine,
    Objective,
    RestRoutine,
    RiskAlerts,
    DayFoodPlan,
    Instruction,
    RestDevice,
    TrainingSessionSchema,
    SportsSessionSchema,
    ObjectiveInstructionSchema,
    TrainingPlanSchema,
    EatingRoutineSchema,
    ObjectiveSchema,
    RestRoutineSchema,
    RiskAlertsSchema,
    DayFoodPlanSchema,
    InstructionSchema,
    RestDeviceSchema,
    db
)
from pathlib import Path
from decouple import config
import json
import uuid




def generate_uuid():
    uid = uuid.uuid4()
    parts = str(uid).split("-")
    return parts[0]


training_session_schema = TrainingSessionSchema()
sports_session_schema = SportsSessionSchema()
objective_instruction_schema = ObjectiveInstructionSchema()


training_plan_schema = TrainingPlanSchema()
eating_routine_schema = EatingRoutineSchema()
objective_schema = ObjectiveSchema()
rest_routine_schema = RestRoutineSchema()
risk_alerts_schema = RiskAlertsSchema()
day_food_plan_schema = DayFoodPlanSchema()
instruction_schema = InstructionSchema()
rest_device_schema = RestDeviceSchema()
date_format = "%Y-%m-%d %H:%M:%S"

error_msg = "Error: "
error_upd_msg = "No se pudo realizar la Actualización "


class VistaStatusCheck(Resource):
    def get(self):
        return {"status": "ok"}


class VistaTrainingSession(Resource):
    def post(self):
        try:
            session_date = datetime.strptime(
                request.json["session_date"], date_format
            )
            sport_session_date = datetime.strptime(
                request.json["sport_session_date"], date_format
            )
            training_session_id = generate_uuid()
            sport_session_id = generate_uuid()
            objective_instruction_id = generate_uuid()
           
            training_session = TrainingSession(
                id=training_session_id,
                id_sport_user=request.json["id_sport_user"],
                id_event=request.json["id_event"],
                event_category=request.json["event_category"],
                sport_type=request.json["sport_type"],
                session_date=session_date,
                createdAt=datetime.now(),
                updatedAt=datetime.now(),
            )

            db.session.add(training_session)
            db.session.commit()

            sports_session = SportsSession(
                id=sport_session_id,
                id_training_session=training_session.id,
                name=request.json["name"],
                week=request.json["week"],
                day=request.json["day"],
                repeats=request.json["repeats"],
                location=request.json["location"],
                total_time=request.json["total_time"],
                min_weight=sport_session_date,
                qty_objectives_achived=request.json["objectives_achived"],
                createdAt=datetime.now(),
                updatedAt=datetime.now(),
            )

            db.session.add(sports_session)
            db.session.commit()

            objective_instruction = ObjectiveInstruction(
                id=objective_instruction_id,
                id_sport_session=sports_session.id,
                instruction_description=request.json["instruction_description"],
                instruction_time=request.json["instruction_time"],
                target_achieved=request.json["target_achieved"],
                createdAt=datetime.now(),
                updatedAt=datetime.now(),
            )

            db.session.add(objective_instruction)
            db.session.commit()
            return {
                "message": "Se pudo crear la sesión de entrenamiento exitosamante"
            }, 200

        except IntegrityError as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": "No se pudo crear la sesión de entrenamiento"}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": "No se pudo crear la sesión de entrenamiento"}, 500

    def put(self):
        def get_request_data(self):
            return {
                "name": request.json["name"],
                "day": request.json["day"],
                "id_event": request.json["id_event"],
                "session_date": datetime.strptime(
                    request.json["session_date"], date_format
                ),
                "sport_session_date": datetime.strptime(
                    request.json["sport_session_date"], date_format
                ),
                "event_category": request.json["event_category"],
                "sport_type": request.json["sport_type"],
                "week": request.json["week"],
                "repeats": request.json["repeats"],
                "location": request.json["location"],
                "total_time": request.json["total_time"],
                "qty_objectives_achived": request.json["objectives_achived"],
                "instruction_description": request.json["instruction_description"],
                "instruction_time": request.json["instruction_time"],
                "target_achieved": request.json["target_achieved"],
            }

        def update_training_session(self, training_session, data):
            training_session.event_category = data["event_category"]
            training_session.sport_type = data["sport_type"]
            training_session.session_date = data["session_date"]
            training_session.updatedAt = datetime.now()

        def update_sport_session(self, sport_session, data):
            sport_session.week = data["week"]
            sport_session.repeats = data["repeats"]
            sport_session.location = data["location"]
            sport_session.total_time = data["total_time"]
            sport_session.session_event = data["sport_session_date"]
            sport_session.qty_objectives_achived = data["qty_objectives_achived"]
            sport_session.updatedAt = datetime.now()

        def update_objective_instruction(self, objective_instruction, data):
            objective_instruction.instruction_description = data[
                "instruction_description"
            ]
            objective_instruction.instruction_time = data["instruction_time"]
            objective_instruction.target_achieved = data["target_achieved"]
            objective_instruction.updatedAt = datetime.now()

        try:
            data = get_request_data(self)

            sport_session = SportsSession.query.filter(
                SportsSession.name == data["name"]
            ).first()
            if sport_session is None:
                return {"message": "La sesion deportiva buscada no Existe"}, 404

            training_session = TrainingSession.query.filter(
                TrainingSession.id_event == data["id_event"]
            ).first()
            if training_session is None:
                return {"message": error_upd_msg, "code": 400}, 400

            objective_instruction = ObjectiveInstruction.query.filter(
                ObjectiveInstruction.id_sport_session == sport_session.id
            ).first()
            if objective_instruction is None:
                return {"message": error_upd_msg, "code": 400}, 400

            update_training_session(self, training_session, data)
            update_sport_session(self, sport_session, data)
            update_objective_instruction(self, objective_instruction, data)

            db.session.commit()

            return {
                "message": "Se actualizaron correctamente los campos",
                "training_session": training_session_schema.dump(training_session),
                "sport_session": sports_session_schema.dump(sport_session),
                "objective_instruction": objective_instruction_schema.dump(
                    objective_instruction
                ),
                "code": 200,
            }, 200

        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg}, 500
        
class VistaTrainingPlan(Resource):
    def post(self):
        try:
            training_plan_id = generate_uuid()
            eating_routine_id = generate_uuid()
            objective_id = generate_uuid()
            risk_alerts_id = generate_uuid()
            day_food_plan_id = generate_uuid()
            rest_routine_id = generate_uuid()
            instruction_id = generate_uuid()
            rest_device_id = generate_uuid()

            day_food_plan = DayFoodPlan(
                id=day_food_plan_id,
                day=request.json["day_food_plan"],
                food=request.json["food"],
                qty=request.json["qty"],
                calories=request.json["calories"],
                value=request.json["value"],
                id_eating_routine = eating_routine_id,
                createdAt=datetime.now(),
                updatedAt=datetime.now()
            )

            db.session.add(day_food_plan)
            db.session.commit()
      
            eating_routine = EatingRoutine(
                id=eating_routine_id,
                name=request.json["eating_routine_name"],
                description=request.json["eating_routine_description"],
                weeks=request.json["eating_routine_weeks"],
                max_weight=request.json["max_weight"],
                min_weight=request.json["min_weight"],
                location=request.json["location"],
                id_training_plan = training_plan_id,
                dayFoodPlanes = [day_food_plan],
                createdAt=datetime.now(),
                updatedAt=datetime.now()
            )

            db.session.add(eating_routine)
            db.session.commit()

            instruction = Instruction(
                id=instruction_id,
                instruction_description=request.json["instruction_description"],
                instruction_time=request.json["instruction_time"],
                id_objective=objective_id,
                createdAt=datetime.now(),
                updatedAt=datetime.now()
            )

            db.session.add(instruction)
            db.session.commit()

            objective = Objective(
                id=objective_id,
                day=request.json["day"],
                repeats=request.json["objective_repeats"],
                type_objective=request.json["type_objective"],
                id_training_plan = training_plan_id,
                instructions = [instruction],
                id_rest_routine = rest_routine_id,
                createdAt=datetime.now(),
                updatedAt=datetime.now()
            )

            db.session.add(objective)
            db.session.commit()

            training_plan = TrainingPlan(
                id=training_plan_id,
                name=request.json["name"],
                description=request.json["description"],
                weeks=request.json["weeks"],
                lunes_enabled=request.json["lunes_enabled"],
                martes_enabled=request.json["martes_enabled"],
                miercoles_enabled=request.json["miercoles_enabled"],
                jueves_enabled=request.json["jueves_enabled"],
                viernes_enabled=request.json["viernes_enabled"],
                typePlan=request.json["typePlan"],
                sport= request.json["sport"],
                Objectives = [objective],
                createdAt=datetime.now(),
                updatedAt=datetime.now()
            )

            db.session.add(training_plan)
            db.session.commit()

            rest_device = RestDevice(
                id=rest_device_id,
                rest_device_name=request.json["rest_device_name"],
                rest_device_qty=request.json["rest_device_qty"],
                rental_value= request.json["rental_value"],
                id_rest_routine= rest_routine_id,
                createdAt=datetime.now(),
                updatedAt=datetime.now()
            )

            db.session.add(rest_device)
            db.session.commit()

            rest_routine = RestRoutine(
                id=rest_routine_id,
                name=request.json["rest_routine_name"],
                description=request.json["rest_routine_description"],
                id_training_plan = training_plan_id,
                objectives = [Objective],
                restDevices = [rest_device],
                createdAt=datetime.now(),
                updatedAt=datetime.now()
            )

            db.session.add(rest_routine)
            db.session.commit()

            risk_alerts = RiskAlerts(
                id=risk_alerts_id,
                stop_training=request.json["stop_training"],
                notifications=request.json["notifications"],
                enable_phone=request.json["enable_phone"],
                id_training_plan = training_plan_id,
                createdAt=datetime.now(),
                updatedAt=datetime.now()
            )

            db.session.add(risk_alerts)
            db.session.commit()

            return {
                "message": "Se pudo crear la sesión de entrenamiento exitosamante"
            }, 200

        except IntegrityError as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": "No se pudo crear la sesión de entrenamiento"}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": "No se pudo crear la sesión de entrenamiento"}, 500
    def put(self):
        def get_request_data(self):
            return {
                "day_food_plan": request.json["day_food_plan"],
                "food": request.json["food"],
                "qty": request.json["qty"],
                "calories": request.json["calories"],
                "value": request.json["value"],
                "eating_routine_name": request.json["eating_routine_name"],
                "eating_routine_description": request.json["eating_routine_description"],
                "eating_routine_weeks": request.json["eating_routine_weeks"],
                "max_weight": request.json["max_weight"],
                "min_weight": request.json["min_weight"],
                "instruction_time": request.json["instruction_time"],
                "instruction_description": request.json["instruction_description"],
                "day": request.json["day"],
                "objective_repeats": request.json["objective_repeats"],
                "type_objective": request.json["type_objective"],
                "name": request.json["name"],
                "description": request.json["description"],
                "weeks": request.json["weeks"],
                "lunes_enabled": request.json["lunes_enabled"],
                "martes_enabled": request.json["martes_enabled"],
                "miercoles_enabled": request.json["miercoles_enabled"],
                "jueves_enabled": request.json["jueves_enabled"],
                "viernes_enabled": request.json["viernes_enabled"],
                "typePlan": request.json["typePlan"],
                "sport": request.json["sport"],
                "rest_device_name": request.json["rest_device_name"],
                "rest_device_qty": request.json["rest_device_qty"],
                "rental_value": request.json["rental_value"],
                "rest_routine_name": request.json["rest_routine_name"],
                "rest_routine_description": request.json["rest_routine_description"],
                "stop_training": request.json["stop_training"],
                "notifications": request.json["notifications"],
                "enable_phone": request.json["enable_phone"]
            }

        def update_training_plan(self, training_plan, data):
            training_plan.name = data["name"]
            training_plan.description = data["description"]
            training_plan.weeks = data["weeks"]
            training_plan.lunes_enabled = data["lunes_enabled"]
            training_plan.martes_enabled = data["martes_enabled"]
            training_plan.miercoles_enabled = data["miercoles_enabled"]
            training_plan.jueves_enabled = data["jueves_enabled"]
            training_plan.viernes_enabled = data["viernes_enabled"]
            training_plan.typePlan = data["typePlan"]
            training_plan.sport = data[" sport"]
            training_plan.updatedAt = datetime.now()

        def update_eating_routine(self, eating_routine, data):
            eating_routine.name = data["eating_routine_name"]
            eating_routine.description = data["eating_routine_description"]
            eating_routine.weeks = data["eating_routine_weeks"]
            eating_routine.max_weight = data["max_weight"]
            eating_routine.min_weight = data["min_weight"]
            eating_routine.updatedAt = datetime.now()

        def update_objective(self, objective, data):
            objective.day = data["day"]
            objective.objective_repeats = data["objective_repeats"]
            objective.type_objective = data["type_objective"]
            objective.updatedAt = datetime.now()

        def update_rest_routine(self, rest_routine, data):
            rest_routine.name = data["rest_routine_name"]
            rest_routine.description = data["rest_routine_description"]
            rest_routine.updatedAt = datetime.now()

        def update_risk_alerts(self, risk_alerts, data):
            risk_alerts.stop_training = data["stop_training"]
            risk_alerts.notifications = data["notifications"]
            risk_alerts.enable_phone = data["enable_phone"]
            risk_alerts.updatedAt = datetime.now()

        def update_day_food_plan(self, day_food_plan, data):
            day_food_plan.day = data["day_food_plan"]
            day_food_plan.food = data["food"]
            day_food_plan.qty = data["qty"]
            day_food_plan.calories = data["calories"]
            day_food_plan.value = data["value"]
            day_food_plan.updatedAt = datetime.now()

        def update_instruction(self, instruction, data):
            instruction.instruction_description = data["instruction_description"]
            instruction.instruction_time = data["instruction_time"]
            instruction.updatedAt = datetime.now()

        def update_rest_device(self, rest_device, data):
            rest_device.name = data["rest_routine_name"]
            rest_device.qty = data["rest_device_qty"]
            rest_device.rental_value = data["rental_value"] 
            rest_device.updatedAt = datetime.now()

        try:
            data = get_request_data(self)

            training_plan = TrainingPlan.query.filter(
                TrainingPlan.name == data["name"]
            ).first()
            if training_plan is None:
                return {"message": "La sesion deportiva buscada no existe"}, 404

            eating_routine = EatingRoutine.query.filter(
                EatingRoutine.id_training_plan == training_plan.id
            ).first()
            if eating_routine is None:
                return {"message": error_upd_msg, "code": 400}, 400

            objective = Objective.query.filter(
                Objective.id_training_plan == training_plan.id
            ).first()
            if objective is None:
                return {"message": error_upd_msg, "code": 400}, 400
            
            rest_routine = RestRoutine.query.filter(
                RestRoutine.id_training_plan == training_plan.id
            ).first()
            if rest_routine is None:
                return {"message": error_upd_msg, "code": 400}, 400
            
            risk_alerts = RiskAlerts.query.filter(
                RiskAlerts.id_training_plan == training_plan.id
            ).first()
            if risk_alerts is None:
                return {"message": error_upd_msg, "code": 400}, 400
            
            day_food_plan = DayFoodPlan.query.filter(
                DayFoodPlan.id_eating_routine == eating_routine.id
            ).first()
            if day_food_plan is None:
                return {"message": error_upd_msg, "code": 400}, 400
            
            instruction = Instruction.query.filter(
                Instruction.id_objective == objective.id
            ).first()
            if instruction is None:
                return {"message": error_upd_msg, "code": 400}, 400
            
            rest_device = RestDevice.query.filter(
                RestDevice.id_rest_routine == rest_routine.id
            ).first()
            if rest_device is None:
                return {"message": error_upd_msg, "code": 400}, 400

            update_training_plan(self, training_plan, data)
            update_eating_routine(self, eating_routine, data)
            update_objective(self, objective, data)
            update_rest_routine(self, rest_routine, data)
            update_risk_alerts(self, risk_alerts, data)
            update_day_food_plan(self, day_food_plan, data)
            update_instruction(self, instruction, data)
            update_rest_device(self, rest_device, data)
            
            db.session.commit()

            return {
                "message": "Se actualizarón correctamente los campos",
                "training_plan": training_plan_schema.dump(training_plan),
                "eating_routine": eating_routine_schema.dump(eating_routine),
                "objective": objective_schema.dump(objective),
                "rest_routine": rest_routine_schema.dump(rest_routine),
                "risk_alerts": risk_alerts_schema.dump(risk_alerts),
                "day_food_plan": day_food_plan_schema.dump(day_food_plan),
                "instruction": instruction_schema.dump(instruction),
                "rest_device": rest_device_schema.dump(rest_device),
                "code": 200,
            }, 200

        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg}, 500
        
    def get(self):
        try:
            name = request.json["name"]
            training_plan = TrainingPlan.query.filter(
                TrainingPlan.name == name
            ).all()
            if training_plan is None:
                return {"message": "La sesion deportiva buscada no existe"}, 404

            return {
                "message": "Se actualizarón correctamente los campos",
                "training_plan": training_plan_schema.dump(training_plan),
                "code": 200,
            }, 200

        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg}, 500
        
        