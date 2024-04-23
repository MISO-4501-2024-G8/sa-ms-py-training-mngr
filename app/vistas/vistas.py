from dataclasses import dataclass

from datetime import datetime
import requests
from flask import request
from flask_jwt_extended import create_access_token, jwt_required
from flask_restful import Resource

from modelos.modelos import (TrainingSession, SportsSession, ObjectiveInstruction, TrainingSessionSchema, SportsSessionSchema, ObjectiveInstructionSchema, db)

from pathlib import Path
from decouple import config


from sqlalchemy.exc import IntegrityError

training_session_schema = TrainingSessionSchema()
sports_session_schema = SportsSessionSchema()
objective_instruction_schema = ObjectiveInstructionSchema()

date_format = '%Y-%m-%d %H:%M:%S'

class statusCheck(Resource):
    def get(self):
        return {'status': 'ok'}

class VistaTrainingPlan(Resource):
      def post(self):
        
        session_date = datetime.strptime(request.json["session_date"], date_format)
        sport_session_date = datetime.strptime(request.json["sport_session_date"], date_format)
    

        training_session = TrainingSession(event_category = request.json["event_category"],
                                          sport_type = request.json["sport_type"],
                                          session_date = session_date)
        
        db.session.add(training_session)
        db.session.commit()

        sports_session = SportsSession(name = request.json["name"],
                                       week = request.json["week"],
                                       day = request.json["day"],
                                       repeats = request.json["repeats"],
                                       location = request.json["location"],
                                       total_time = request.json["total_time"],
                                       session_event = sport_session_date,
                                       qty_objectives_achived = request.json["objectives_achived"],
                                       id_training_session = training_session.id)
        
        db.session.add(sports_session)
        db.session.commit()

        objective_instruction = ObjectiveInstruction(instruction_description = request.json["instruction_description"],
                                                     instruction_time = request.json["instruction_time"],
                                                     target_achieved = request.json["target_achieved"],
                                                     id_sport_session = sports_session.id)
        
        
        
        db.session.add(objective_instruction)
        db.session.commit()
        if training_session is None:
            return {"message": "No se pudo crear el plan de entrenamiento"}, 404 
        else:
           return {"message": "Se pudo crear el plan de entrenamiento exitosamante"}, 200
  
      def put(self):
        name = request.json["name"]
        day = request.json["day"]
        session_date = datetime.strptime(request.json["session_date"], date_format)
        sport_session_date = datetime.strptime(request.json["sport_session_date"], date_format)
        event_category = request.json["event_category"]
        sport_type= request.json["sport_type"]
        week = request.json["week"]
        repeats = request.json["repeats"]
        location = request.json["location"]
        total_time = request.json["total_time"]
        qty_objectives_achived = request.json["objectives_achived"]
        instruction_description = request.json["instruction_description"]
        instruction_time = request.json["instruction_time"]
        target_achieved = request.json["target_achieved"]


        sport_session = SportsSession.query.filter(name == name,
                                                   day = day).first()
        if(sport_session is None):
            return {"message": "La sesion deportiva buscada no Existe"}, 404
        else:
            training_session = TrainingSession.query.filter(id == sport_session.id_training_session).first()
            objective_instruction =  ObjectiveInstruction.query.filter(id == sport_session.id_sport_session).first()

            sport_session.event_category if sport_session.event_category == event_category else event_category
            sport_session.sport_type if sport_session.sport_type == sport_type else sport_type
            sport_session.session_date if sport_session.session_date == session_date else session_date
            db.session.commit()

            training_session.week if training_session.week == week else week
            training_session.repeats if training_session.repeats == repeats else repeats
            training_session.location if training_session.location == location else location
            training_session.total_time if training_session.total_time == total_time else total_time
            training_session.session_event if training_session.session_event == sport_session_date else sport_session_date
            training_session.qty_objectives_achived if training_session.qty_objectives_achived == qty_objectives_achived else qty_objectives_achived
            db.session.commit()

            objective_instruction.instruction_description if objective_instruction.instruction_description == instruction_description else instruction_description
            objective_instruction.instruction_time if objective_instruction.instruction_time == instruction_time else instruction_time
            objective_instruction.target_achieved if objective_instruction.target_achieved == target_achieved else target_achieved
            db.session.commit()

            return {"message": "Se actualizaron correctmente los campos", 
                    "training_session" : training_session_schema.dump(training_session),
                    "sport_session" : sports_session_schema.dump(sport_session),
                    "objective_instruction" : objective_instruction_schema.dump(objective_instruction)}, 200
            
            





 