from dataclasses import dataclass
import time
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
#usuario_schema = UsuarioSchema()
#definitionTask_schema = DefinitionTaskSchema()
#task_schema = TaskSchema()


class statusCheck(Resource):
    def get(self):
        return {'status': 'ok'}

  

class VistaTrainingPlan(Resource):

      def post(self):
        training_session = TrainingSession(event_category = request.json["event_category"],
                                          sport_type = request.json["sport_type"],
                                          session_date = request.json["session_date"])
        
        print(training_session.id)

        sports_session = SportsSession(name =,
                                       week = ,
                                       day = ,
                                       repeats = ,
                                       location = ,
                                       total_time = ,
                                       session_date = ,
                                       qty_objectives_achived = ,
                                       id_training_session = training_session.id)

        print(sports_session.id)

        objective_instruction = ObjectiveInstruction(instruction_description =,
                                                     instruction_time =,
                                                     target_achieved =,
                                                     id_sports_session = sports_session.id

        )
        
        db.session.add(training_session)
        db.session.add(sports_session)
        db.session.add(objective_instruction)
        db.session.commit()
        if usuario is None:
            return "El usuario no existe", 404
        else:
            token_de_acceso = create_access_token(identity=usuario.id)
            return {"mensaje": "Inicio de sesión exitoso", "token": token_de_acceso, 'usuarioId': usuario.id}
"""    
    def put(self):
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"],
                                        Usuario.id == request.json["id"],
                                        Usuario.rol == request.json["rol"]).first()
        if(usuario is None):
            return "El usuario no existe", 404
        usuario.contrasena = request.json.get("contrasena_new", usuario.contrasena)
        db.session.commit()
        return usuario_schema.dump(usuario)
    
    def delete(self):
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"],
                                        Usuario.id == request.json["id"],
                                        Usuario.rol == request.json["rol"]).first()
        if(usuario is None):
            return "El usuario no existe", 404
        db.session.delete(usuario)
        db.session.commit()
        return '', 204

    def post(self, id_task):
        #@jwt_required()
        try:
            file_name = request.json['fileName']
            new_format = request.json['newFormat']

            timestamp = datetime.timestamp(datetime.now())
            status = 'upLoaded'

            usuario = Usuario.query.get_or_404(id_task)
            task = Task(time_stamp = timestamp, 
                        file_name = file_name.split('.')[1],
                        path_file_name = file_name,
                        new_format = new_format,
                        status = status,
                        id_usuario = usuario.id)
            db.session.add(task)
            db.session.commit()
            
            data = {'file_name' : file_name, 
                    'new_format' : new_format, 
                    'id_task': task.id}
            args = (data,)
            print(args)
            escribir_cola.apply_async(args = args)
            return {'status': 'Tarea encolada correctamente', 'id_task': task.id }, 200
        except ConnectionError as e:
            return {'error': 'Backend postTask offline -- Connection'}, 404
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            return {'error': 'Backend postTask offline -- Timeout'}, 404
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            return {'error': 'Backend postTask offline -- ManyRedirects'}, 404
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            return {'error': 'Backend postTask offline -- Request'}, 404
        except Exception as e:
            return {'error': 'Backend postTask - Error desconocido -' + str(e)}, 404 
    
    def get(self):
        #@jwt_required()
        print("Entre al tema")
        try:
            task = Task.query.get_or_404(id_task)
            if task is not None:
                return task_schema.dump(task, many=False)
            return 'La tarea no se encontro' , 404 
        except ConnectionError as e:
            return {'error': 'Backend getTask offline -- Connection'}, 404
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            return {'error': 'Backend getTask offline -- Timeout'}, 404
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            return {'error': 'Backend getTask offline -- ManyRedirects'}, 404
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            return {'error': 'Backend getTask offline -- Request'}, 404
        except Exception as e:
            return {'error': 'Backend getTask - Error desconocido -' + str(e)}, 404 
    
    def put(self, id_task):
         #@jwt_required()
        try:
            task = Task.query.get_or_404(id_task)
            if task is not None:
                new_format = request.json['newFormat']
                task.new_format = new_format
                db.session.commit()
                return task_schema.dump(task)     
            return 'La tarea a actualizar no se encontro' , 404
        except ConnectionError as e:
            return {'error': 'Backend putTask offline -- Connection'}, 404
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            return {'error': 'Backend putTask offline -- Timeout'}, 404
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            return {'error': 'Backend putTask offline -- ManyRedirects'}, 404
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            return {'error': 'Backend putTask offline -- Request'}, 404
        except Exception as e:
            return {'error': 'Backend putTask - Error desconocido -' + str(e)}, 404

    def delete(self, id_task):
         #@jwt_required()
        try:
            task = Task.query.get_or_404(id_task)
            if task is not None :
                db.session.delete(task)
                db.session.commit()
                return 'la tarea se elimino correctamente', 200
            return 'la tarea a eliminar no se encontro', 404
        except ConnectionError as e:
            return {'error': 'Backend deleteTask offline -- Connection'}, 404
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            return {'error': 'Backend deleteTask offline -- Timeout'}, 404
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            return {'error': 'Backend deleteTask offline -- ManyRedirects'}, 404
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            return {'error': 'Backend deleteTask offline -- Request'}, 404
        except Exception as e:
            return {'error': 'Backend deleteTask - Error desconocido -' + str(e)}, 404 

"""