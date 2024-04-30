from dataclasses import dataclass

from datetime import datetime
import requests
from flask import request
from flask_jwt_extended import create_access_token, jwt_required
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from modelos.modelos import (
    TrainingPlan,
    EatingRoutine,
    Objective,
    RestRoutine,
    RiskAlerts,
    DayFoodPlan,
    Instruction,
    RestDevice,
    TrainingPlanSchema,
    EatingRoutineSchema,
    ObjectiveSchema,
    RestRoutineSchema,
    RiskAlertsSchema,
    DayFoodPlanSchema,
    InstructionSchema,
    RestDeviceSchema,
    db,
)
from pathlib import Path
from decouple import config
import json
import uuid


def generate_uuid():
    uid = uuid.uuid4()
    parts = str(uid).split("-")
    return parts[0]


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
error_upd_msg = "No se pudo realizar la Actualización"


class VistaStatusCheck(Resource):
    def get(self):
        return {"status": "OK", "code": 200}, 200


class VistaTrainingPlan(Resource):
    def post(self):
        try:
            training_plan_id = generate_uuid()
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
                sport=request.json["sport"],
                id_eating_routine=request.json["id_eating_routine"],
                id_rest_routine=request.json["id_rest_routine"],
                createdAt=datetime.now(),
                updatedAt=datetime.now(),
            )

            db.session.add(training_plan)
            db.session.commit()
            return {
                "message": "Se pudo crear la sesión de entrenamiento exitosamante",
                "training_plan": training_plan_schema.dump(training_plan),
                "code": 200,
            }, 200

        except IntegrityError as e:
            print(error_msg, e)
            db.session.rollback()
            return {
                "message": "No se pudo crear la sesión de entrenamiento",
                "code": 500,
            }, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {
                "message": "No se pudo crear la sesión de entrenamiento",
                "code": 500,
            }, 500
    
    def get(self):
        try:
            training_plans = TrainingPlan.query.all()
            if training_plans is None or len(training_plans) == 0:
                return {
                    "message": "No se ha encontrado la sesión de entrenamiento buscada",
                    "code": 404,
                }, 404

            result_training_plans = []
            for training_plan in training_plans:
                tp = training_plan_schema.dump(training_plan)
                print("tp", tp)
                objectives = Objective.query.filter(Objective.id_routine == tp["id"]).all()
                objetivos = []
                for obj in objectives:
                    obj_i = objective_schema.dump(obj) 
                    print("obj_i", obj_i)
                    obj_i["instructions"] = instruction_schema.dump(Instruction.query.filter(Instruction.id_objective == obj_i["id"]).all(), many=True)
                    objetivos.append(obj_i)
                tp["objectives"] = objetivos
                result_training_plans.append(tp)

            return {
                "message": "Se Encontraron las sesiones",
                "training_plans": result_training_plans,
                "code": 200,
            }, 200

        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": "Error al consultar los planes de entrenamiento", "code": 500}, 500


class VistaTrainingPlanID(Resource):
    def put(self, id):
        def get_request_data(self):
            return {
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
                "id_eating_routine": request.json["id_eating_routine"],
                "id_rest_routine": request.json["id_rest_routine"],
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
            training_plan.type_plan = data["typePlan"]
            training_plan.sport = data["sport"]
            training_plan.id_eating_routine = data["id_eating_routine"]
            training_plan.id_rest_routine = data["id_rest_routine"]
            training_plan.updatedAt = datetime.now()

        try:
            if id == "integrity_error":
                raise IntegrityError(
                    "IntegrityError", "IntegrityError", "IntegrityError"
                )

            data = get_request_data(self)

            training_plan = TrainingPlan.query.filter(TrainingPlan.id == id).first()
            if training_plan is None:
                return {
                    "message": "El plan de entranamiento no existe",
                    "code": 404,
                }, 404

            update_training_plan(self, training_plan, data)
            db.session.commit()

            return {
                "message": "Se actualizarón correctamente los campos",
                "training_plan": training_plan_schema.dump(training_plan),
                "code": 200,
            }, 200

        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500

    def get(self, id):
        try:
            if id == "integrity_error":
                raise IntegrityError(
                    "IntegrityError", "IntegrityError", "IntegrityError"
                )

            training_plan = TrainingPlan.query.filter(TrainingPlan.id == id).first()
            if training_plan is None:
                return {
                    "message": "No se ha encontrado coninsidencia del plan de entranamiento buscado",
                    "code": 404,
                }, 404

            return {
                "message": "Se Encontro el plan de entranamiento buscado",
                "training_plan": training_plan_schema.dump(training_plan),
                "code": 200,
            }, 200

        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500

    def delete(self, id):
        training_plan = TrainingPlan.query.get_or_404(id)
        db.session.delete(training_plan)
        db.session.commit()


class VistaObjectives(Resource):
    def post(self):
        try:
            print("request.json", request.json)
            objective_id = generate_uuid()
            objective = Objective(
                id=objective_id,
                day=request.json["day"],
                repeats=request.json["objective_repeats"],
                type_objective=request.json["type_objective"],
                id_routine=request.json["id_routine"],
                createdAt=datetime.now(),
                updatedAt=datetime.now(),
            )

            db.session.add(objective)
            db.session.commit()
            return {
                "message": "Se pudo crear el objetivo sesion exitosamante",
                "objective": objective_schema.dump(objective),
                "code": 200,
            }, 200

        except IntegrityError as e:
            print(error_msg, e)
            db.session.rollback()
            return {
                "message": "No se pudo crear el objetivo sesion",
                "code": 500,
            }, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {
                "message": "No se pudo crear el objetivo sesion",
                "code": 500,
            }, 500


class VistaObjectivesID(Resource):
    def put(self, id):

        def get_request_data(self):
            return {
                "day": request.json["day"],
                "objective_repeats": request.json["objective_repeats"],
                "type_objective": request.json["type_objective"],
                "id_routine": request.json["id_routine"],
            }

        def update_objective(self, objective, data):
            objective.id_routine = data["id_routine"]
            objective.day = data["day"]
            objective.repeats = data["objective_repeats"]
            objective.type_objective = data["type_objective"]
            objective.updatedAt = datetime.now()

        try:
            if id == "integrity_error":
                raise IntegrityError(
                    "IntegrityError", "IntegrityError", "IntegrityError"
                )
            data = get_request_data(self)
            objective = Objective.query.filter(Objective.id == id).first()
            if objective is None:
                return {
                    "message": "El objetivo de plan deportivo no existe",
                    "code": 400,
                }, 400

            update_objective(self, objective, data)
            db.session.commit()
            return {
                "message": "Se actualizarón correctamente los campos",
                "objective": objective_schema.dump(objective),
                "code": 200,
            }, 200
        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500

    def get(self, id):
        try:
            print("VistaObjectivesID", id)
            if id == "integrity_error":
                raise IntegrityError(
                    "IntegrityError", "IntegrityError", "IntegrityError"
                )
            objective = Objective.query.filter(Objective.id == id).first()
            if objective is None:
                return {
                    "message": "No se ha encontrado coninsidencia del objetivo del plan entranamiento buscado",
                    "code": 404,
                }, 404

            return {
                "message": "Se Encontro el objetivo del plan de entranamiento buscado",
                "objective": objective_schema.dump(objective),
                "code": 200,
            }, 200

        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500


class VistaInstructions(Resource):
    def post(self):
        try:
            instruction_id = generate_uuid()
            instruction = Instruction(
                id=instruction_id,
                instruction_description=request.json["instruction_description"],
                instruction_time=request.json["instruction_time"],
                id_objective=request.json["id_objective"],
                createdAt=datetime.now(),
                updatedAt=datetime.now(),
            )

            db.session.add(instruction)
            db.session.commit()
            return {
                "message": "Se pudo crear la instruiccion del objetivo que pertenence a la sesión de entrenamiento exitosamante",
                "instruction": instruction_schema.dump(instruction),
                "code": 200,
            }, 200

        except IntegrityError as e:
            print(error_msg, e)
            db.session.rollback()
            return {
                "message": "No se pudo crear la instruicción del objetivo que pertenence a la sesión de entrenamiento exitosamante",
                "code": 500,
            }, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {
                "message": "No se pudo crear la instruicción del objetivo que pertenence a la sesión de entrenamiento exitosamante",
                "code": 500,
            }, 500


class VistaInstructionsID(Resource):
    def put(self, id):

        def get_request_data(self):
            return {
                "instruction_time": request.json["instruction_time"],
                "instruction_description": request.json["instruction_description"],
                "id_objective": request.json["id_objective"],
            }

        def update_instruction(self, instruction, data):
            instruction.instruction_description = data["instruction_description"]
            instruction.instruction_time = data["instruction_time"]
            instruction.id_objective = data["id_objective"]
            instruction.updatedAt = datetime.now()

        try:
            if id == "integrity_error":
                raise IntegrityError(
                    "IntegrityError", "IntegrityError", "IntegrityError"
                )
            data = get_request_data(self)
            instruction = Instruction.query.filter(Instruction.id == id).first()
            if instruction is None:
                return {
                    "message": "No se encontro la Instruccion del plan de entrenamiento buscada",
                    "code": 400,
                }, 400

            update_instruction(self, instruction, data)
            db.session.commit()
            return {
                "message": "Se actualizarón correctamente los campos",
                "instruction": instruction_schema.dump(instruction),
                "code": 200,
            }, 200
        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500

    def get(self, id):
        try:
            if id == "integrity_error":
                raise IntegrityError(
                    "IntegrityError", "IntegrityError", "IntegrityError"
                )
            instruction = Instruction.query.filter(Instruction.id == id).first()
            if instruction is None:
                return {
                    "message": "No se ha encontrado coninsidencia de la instruccion buscada",
                    "code": 404,
                }, 404

            return {
                "message": "Se Encontro la instruccion buscada",
                "instruction": instruction_schema.dump(instruction),
                "code": 200,
            }, 200

        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500


class VistaRestRoutine(Resource):
    def post(self):
        try:
            rest_routine_id = generate_uuid()
            rest_routine = RestRoutine(
                id=rest_routine_id,
                name=request.json["rest_routine_name"],
                description=request.json["rest_routine_description"],
                createdAt=datetime.now(),
                updatedAt=datetime.now(),
            )

            db.session.add(rest_routine)
            db.session.commit()
            return {
                "message": "Se pudo crear la rutina de descanso de la sesion de entrenamiento exitosamante",
                "rest_routine": rest_routine_schema.dump(rest_routine),
                "code": 200,
            }, 200

        except IntegrityError as e:
            print(error_msg, e)
            db.session.rollback()
            return {
                "message": "No se pudo crear la rutina de descanso de la sesion de entrenamiento exitosamante",
                "code": 500,
            }, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {
                "message": "No se pudo crear la rutina de descanso de la sesion de entrenamiento exitosamante",
                "code": 500,
            }, 500
        
    def get(self):
        try:
            rest_routine = RestRoutine.query.all()
            if rest_routine is None:
                return {
                    "message": "No se ha encontrado la rutina de descanso buscada",
                    "code": 404,
                }, 404

            result_rest_routines = []
            for rest_routine in rest_routine:
                rest_rt = rest_routine_schema.dump(rest_routine)
                rest_obj = Objective.query.filter(Objective.id_routine == rest_rt["id"]).all()
                objetivos = []
                for obj in rest_obj:
                    obj_i = objective_schema.dump(obj) 
                    obj_i["instructions"] = instruction_schema.dump(Instruction.query.filter(Instruction.id_objective == obj_i["id"]).all(), many=True)
                    objetivos.append(obj_i)
                rest_rt["objectives"] = objetivos
                rest_devices = RestDevice.query.filter(RestDevice.id_rest_routine == rest_rt["id"]).all()
                rest_rt["rest_devices"] = rest_device_schema.dump(rest_devices, many=True)
                result_rest_routines.append(rest_rt)
        
            return {
                "message": "Se Encontraron las rutinas de descanso",
                "rest_routines": result_rest_routines,
                "code": 200,
            }, 200

        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500


class VistaRestRoutineID(Resource):
    def put(self, id):

        def get_request_data(self):
            return {
                "rest_routine_name": request.json["rest_routine_name"],
                "rest_routine_description": request.json["rest_routine_description"],
            }

        def update_rest_routine(self, rest_routine, data):
            rest_routine.name = data["rest_routine_name"]
            rest_routine.description = data["rest_routine_description"]
            rest_routine.updatedAt = datetime.now()

        try:
            if id == "integrity_error":
                raise IntegrityError(
                    "IntegrityError", "IntegrityError", "IntegrityError"
                )
            data = get_request_data(self)
            rest_routine = RestRoutine.query.filter(RestRoutine.id == id).first()
            if rest_routine is None:
                return {
                    "message": "No se enconcotro la rutina de escanso buscada",
                    "code": 400,
                }, 400

            update_rest_routine(self, rest_routine, data)
            db.session.commit()

            return {
                "message": "Se actualizarón correctamente los campos",
                "rest_routine": rest_routine_schema.dump(rest_routine),
                "code": 200,
            }, 200
        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500

    def get(self, id):
        try:
            if id == "integrity_error":
                raise IntegrityError(
                    "IntegrityError", "IntegrityError", "IntegrityError"
                )
            rest_routine = RestRoutine.query.filter(RestRoutine.id == id).first()
            if rest_routine is None:
                return {
                    "message": "No se ha encontrado la rutina de descanso buscada",
                    "code": 404,
                }, 404

            return {
                "message": "Se Encontro la rutina de descanso buscada",
                "rest_routine": rest_routine_schema.dump(rest_routine),
                "code": 200,
            }, 200

        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500


class VistaRestDevice(Resource):
    def post(self):
        try:
            rest_device_id = generate_uuid()
            rest_device = RestDevice(
                id=rest_device_id,
                name=request.json["rest_device_name"],
                qty=request.json["rest_device_qty"],
                rental_value=request.json["rental_value"],
                id_rest_routine=request.json["id_rest_routine"],
                createdAt=datetime.now(),
                updatedAt=datetime.now(),
            )

            db.session.add(rest_device)
            db.session.commit()
            return {
                "message": "Se pudo crear el dispositio de descanso de la rutina de descanso de la sesion de entrenamiento exitosamante",
                "rest_device": rest_device_schema.dump(rest_device),
                "code": 200,
            }, 200

        except IntegrityError as e:
            print(error_msg, e)
            db.session.rollback()
            return {
                "message": "No se pudo crear el dispositio de descanso de la rutina de descanso de la sesion de entrenamiento exitosamante",
                "code": 500,
            }, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {
                "message": "No se pudo crear el dispositio de descanso de la rutina de descanso de la sesion de entrenamiento exitosamante",
                "code": 500,
            }, 500


class VistaRestDeviceID(Resource):
    def put(self, id):

        def get_request_data(self):
            return {
                "rest_device_name": request.json["rest_device_name"],
                "rest_device_qty": request.json["rest_device_qty"],
                "rental_value": request.json["rental_value"],
                "id_rest_routine": request.json["id_rest_routine"],
            }

        def update_rest_device(self, rest_device, data):
            rest_device.name = data["rest_device_name"]
            rest_device.qty = data["rest_device_qty"]
            rest_device.rental_value = data["rental_value"]
            # rest_device.id_rest_routine = data["id_rest_routine"]
            rest_device.updatedAt = datetime.now()

        try:
            if id == "integrity_error":
                raise IntegrityError(
                    "IntegrityError", "IntegrityError", "IntegrityError"
                )
            data = get_request_data(self)
            rest_device = RestDevice.query.filter(RestDevice.id == id).first()
            if rest_device is None:
                return {
                    "message": "No se encuentra el dispositivo de descanso buscado",
                    "code": 400,
                }, 400

            update_rest_device(self, rest_device, data)
            db.session.commit()

            return {
                "message": "Se actualizarón correctamente los campos",
                "rest_device": rest_device_schema.dump(rest_device),
                "code": 200,
            }, 200
        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500

    def get(self, id):
        try:
            if id == "integrity_error":
                raise IntegrityError(
                    "IntegrityError", "IntegrityError", "IntegrityError"
                )
            rest_device = RestDevice.query.filter(RestDevice.id == id).first()
            if rest_device is None:
                return {
                    "message": "No se ha encontrado el dispositivo de descanso buscado",
                    "code": 404,
                }, 404

            return {
                "message": "Se Encontro el dispositivo de descanso buscado",
                "rest_device": rest_device_schema.dump(rest_device),
                "code": 200,
            }, 200

        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500


class VistaRiskAlerts(Resource):
    def post(self):
        try:
            risk_alerts = RiskAlerts(
                stop_training=request.json["stop_training"],
                notifications=request.json["notifications"],
                enable_phone=request.json["enable_phone"],
                training_plan_id=request.json["id_training_plan"],
                createdAt=datetime.now(),
                updatedAt=datetime.now(),
            )
            db.session.add(risk_alerts)
            db.session.commit()
            return {
                "message": "Se pudo crear la alerta de riesgo de la sesion de entrenamiento exitosamante",
                "risk_alerts": risk_alerts_schema.dump(risk_alerts),
                "code": 200,
            }, 200

        except IntegrityError as e:
            print(error_msg, e)
            db.session.rollback()
            return {
                "message": "No se pudo crear la alerta de riesgo de la sesion de entrenamiento exitosamante",
                "code": 500,
            }, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {
                "message": "No se pudo crear la alerta de riesgo de la sesion de entrenamiento exitosamante",
                "code": 500,
            }, 500


class VistaRiskAlertsID(Resource):
    def put(self, id):

        def get_request_data(self):
            return {
                "stop_training": request.json["stop_training"],
                "notifications": request.json["notifications"],
                "enable_phone": request.json["enable_phone"],
            }

        def update_risk_alerts(self, risk_alerts, data):
            risk_alerts.stop_training = data["stop_training"]
            risk_alerts.notifications = data["notifications"]
            risk_alerts.enable_phone = data["enable_phone"]
            risk_alerts.updatedAt = datetime.now()

        try:
            if id == "integrity_error":
                raise IntegrityError(
                    "IntegrityError", "IntegrityError", "IntegrityError"
                )
            data = get_request_data(self)
            risk_alerts = RiskAlerts.query.filter(RiskAlerts.training_plan_id == id).first()
            if risk_alerts is None:
                return {
                    "message": "No se encontro la alerta de riesgo buscada",
                    "code": 400,
                }, 400

            update_risk_alerts(self, risk_alerts, data)
            db.session.commit()

            return {
                "message": "Se actualizarón correctamente los campos",
                "risk_alerts": risk_alerts_schema.dump(risk_alerts),
                "code": 200,
            }, 200
        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500

    def get(self, id):
        try:
            if id == "integrity_error":
                raise IntegrityError(
                    "IntegrityError", "IntegrityError", "IntegrityError"
                )
            risk_alerts = RiskAlerts.query.filter(RiskAlerts.training_plan_id == id).first()
            if risk_alerts is None:
                return {
                    "message": "Se Encontro la alerta de riesgo buscada",
                    "code": 404,
                }, 404

            return {
                "message": "Se Encontro la alerta de riesgo buscada",
                "risk_alerts": risk_alerts_schema.dump(risk_alerts),
                "code": 200,
            }, 200

        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500


class VistaEatingRoutine(Resource):
    def post(self):
        try:
            eating_routine_id = generate_uuid()
            eating_routine = EatingRoutine(
                id=eating_routine_id,
                name=request.json["eating_routine_name"],
                description=request.json["eating_routine_description"],
                weeks=request.json["eating_routine_weeks"],
                max_weight=request.json["max_weight"],
                min_weight=request.json["min_weight"],
                createdAt=datetime.now(),
                updatedAt=datetime.now(),
            )

            db.session.add(eating_routine)
            db.session.commit()
            return {
                "message": "Se pudo crear la rutina de alimentacion de la sesion de entrenamiento exitosamante",
                "eating_routine": eating_routine_schema.dump(eating_routine),
                "code": 200,
            }, 200

        except IntegrityError as e:
            print(error_msg, e)
            db.session.rollback()
            return {
                "message": "No se pudo crear la rutina de alimentacion de la sesion de entrenamiento exitosamante",
                "code": 500,
            }, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {
                "message": "No se pudo crear la rutina de alimentacion de la sesion de entrenamiento exitosamante",
                "code": 500,
            }, 500
    
    def get(self):
        try:
            eating_routines = EatingRoutine.query.all()
            if eating_routines is None:
                return {
                    "message": "No se ha encontrado la rutina de alimentacion buscada",
                    "code": 404,
                }, 404
            
            result_eating_routine = []
            for routine in eating_routines:
                routine_dict = eating_routine_schema.dump(routine)
                day_food_plans = DayFoodPlan.query.filter(DayFoodPlan.id_eating_routine == routine.id).all()
                routine_dict["day_food_plans"] = day_food_plan_schema.dump(day_food_plans, many=True)
                result_eating_routine.append(routine_dict)

            return {
                "message": "Se Encontraron las rutinas de alimentacion",
                "eating_routine": result_eating_routine,
                "code": 200,
            }, 200

        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500


class VistaEatingRoutineID(Resource):
    def put(self, id):

        def get_request_data(self):
            return {
                "eating_routine_name": request.json["eating_routine_name"],
                "eating_routine_description": request.json[
                    "eating_routine_description"
                ],
                "eating_routine_weeks": request.json["eating_routine_weeks"],
                "max_weight": request.json["max_weight"],
                "min_weight": request.json["min_weight"],
            }

        def update_eating_routine(self, eating_routine, data):
            eating_routine.name = data["eating_routine_name"]
            eating_routine.description = data["eating_routine_description"]
            eating_routine.weeks = data["eating_routine_weeks"]
            eating_routine.max_weight = data["max_weight"]
            eating_routine.min_weight = data["min_weight"]
            eating_routine.updatedAt = datetime.now()

        try:
            if id == "integrity_error":
                raise IntegrityError(
                    "IntegrityError", "IntegrityError", "IntegrityError"
                )
            data = get_request_data(self)
            eating_routine = EatingRoutine.query.filter(EatingRoutine.id == id).first()
            if eating_routine is None:
                return {
                    "message": "No se econtro la rutina de alimentacion buscada",
                    "code": 400,
                }, 400

            update_eating_routine(self, eating_routine, data)
            db.session.commit()

            return {
                "message": "Se actualizarón correctamente los campos",
                "eating_routine": eating_routine_schema.dump(eating_routine),
                "code": 200,
            }, 200
        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500

    def get(self, id):
        try:
            if id == "integrity_error":
                raise IntegrityError(
                    "IntegrityError", "IntegrityError", "IntegrityError"
                )
            eating_routine = EatingRoutine.query.filter(EatingRoutine.id == id).first()
            if eating_routine is None:
                return {
                    "message": "No se ha encontrado la rutina de alimentacion buscada",
                    "code": 404,
                }, 404

            return {
                "message": "Se Encontro la rutina de alimentacion buscada",
                "eating_routine": eating_routine_schema.dump(eating_routine),
                "code": 200,
            }, 200

        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500


class VistaDayFoodPlan(Resource):
    def post(self):
        try:
            day_food_plan_id = generate_uuid()
            day_food_plan = DayFoodPlan(
                id=day_food_plan_id,
                day=request.json["day_food_plan"],
                food=request.json["food"],
                qty=request.json["qty"],
                calories=request.json["calories"],
                value=request.json["value"],
                id_eating_routine=request.json["id_eating_routine"],
                createdAt=datetime.now(),
                updatedAt=datetime.now(),
            )

            db.session.add(day_food_plan)
            db.session.commit()
            return {
                "message": "Se pudo crear el plan de alimentacion diario de la rutina de comida de la sesion de entrenamiento exitosamante",
                "day_food_plan": day_food_plan_schema.dump(day_food_plan),
                "code": 200,
            }, 200

        except IntegrityError as e:
            print(error_msg, e)
            db.session.rollback()
            return {
                "message": "No se pudo crear el plan de alimentacion diario de la rutina de comida de la sesion de entrenamiento exitosamante",
                "code": 500,
            }, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {
                "message": "No se pudo crear el plan de alimentacion diario de la rutina de comida de la sesion de entrenamiento exitosamante",
                "code": 500,
            }, 500


class VistaDayFoodPlanID(Resource):
    def put(self, id):

        def get_request_data(self):
            return {
                "day_food_plan": request.json["day_food_plan"],
                "food": request.json["food"],
                "qty": request.json["qty"],
                "calories": request.json["calories"],
                "value": request.json["value"],
                "id_eating_routine": request.json["id_eating_routine"],
            }

        def update_day_food_plan(self, day_food_plan, data):
            day_food_plan.day = data["day_food_plan"]
            day_food_plan.food = data["food"]
            day_food_plan.qty = data["qty"]
            day_food_plan.calories = data["calories"]
            day_food_plan.value = data["value"]
            day_food_plan.id_eating_routine = data["id_eating_routine"]
            day_food_plan.updatedAt = datetime.now()

        try:
            if id == "integrity_error":
                raise IntegrityError(
                    "IntegrityError", "IntegrityError", "IntegrityError"
                )
            data = get_request_data(self)
            day_food_plan = DayFoodPlan.query.filter(DayFoodPlan.id == id).first()
            if day_food_plan is None:
                return {
                    "message": "No se encontre el plan diario de comida",
                    "code": 400,
                }, 400

            update_day_food_plan(self, day_food_plan, data)
            db.session.commit()

            return {
                "message": "Se actualizarón correctamente los campos",
                "day_food_plan": day_food_plan_schema.dump(day_food_plan),
                "code": 200,
            }, 200
        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500

    def get(self, id):
        try:
            if id == "integrity_error":
                raise IntegrityError(
                    "IntegrityError", "IntegrityError", "IntegrityError"
                )
            day_food_plan = DayFoodPlan.query.filter(DayFoodPlan.id == id).first()
            if day_food_plan is None:
                return {
                    "message": "No se ha encontrado el plan de comida diario buscado",
                    "code": 404,
                }, 404

            return {
                "message": "Se Encontro el plan de comida diario buscado",
                "day_food_plan": day_food_plan_schema.dump(day_food_plan),
                "code": 200,
            }, 200

        except IntegrityError as e:
            db.session.rollback()
            print(error_msg, e)
            return {"message": error_upd_msg, "code": 500}, 500
        except Exception as e:
            print(error_msg, e)
            db.session.rollback()
            return {"message": error_upd_msg, "code": 500}, 500
