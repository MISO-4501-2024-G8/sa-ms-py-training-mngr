from flask import Flask, render_template, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_restful import Api
from modelos.modelos import db
import uuid
from vistas import (
    VistaStatusCheck, 
    VistaTrainingPlan,
    VistaTrainingPlanID,
    VistaObjectives,
    VistaObjectivesID,
    VistaInstructions,
    VistaInstructionsID,
    VistaRestRoutine,
    VistaRestRoutineID,
    VistaRestDevice,
    VistaRestDeviceID,
    VistaRiskAlerts,
    VistaRiskAlertsID,
    VistaEatingRoutine,
    VistaEatingRoutineID,
    VistaDayFoodPlan,
    VistaDayFoodPlanID,
    )
from decouple import config

app=Flask(__name__) # NOSONAR
def generate_uuid():
    uid = uuid.uuid4()
    parts = str(uid).split("-")
    return parts[0]
DATABASE_URI = config('DATABASE_URL', default=f'sqlite:///training_plan_{generate_uuid()}.db')
print(' * DATABASE_URI:', DATABASE_URI)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()
cors = CORS(app) # NOSONAR
api = Api(app) # NOSONAR


api.add_resource(VistaStatusCheck, '/')
api.add_resource(VistaTrainingPlan, '/training_plan')
api.add_resource(VistaTrainingPlanID, '/training_plan/<id>')
api.add_resource(VistaObjectives, '/objetive_training_plan')
api.add_resource(VistaObjectivesID, '/objetive_training_plan/<id>')
api.add_resource(VistaInstructions, '/instruction_training_plan')
api.add_resource(VistaInstructionsID, '/instruction_training_plan/<id>')
api.add_resource(VistaRestRoutine, '/rest_routine_training_plan')
api.add_resource(VistaRestRoutineID, '/rest_routine_training_plan/<id>')
api.add_resource(VistaRestDevice, '/rest_device_training_plan')
api.add_resource(VistaRestDeviceID, '/rest_device_training_plan/<id>')
api.add_resource(VistaRiskAlerts, '/risk_alerts_training_plan')
api.add_resource(VistaRiskAlertsID, '/risk_alerts_training_plan/<id>')
api.add_resource(VistaEatingRoutine, '/eating_routing_training_plan')
api.add_resource(VistaEatingRoutineID, '/eating_routing_training_plan/<id>')
api.add_resource(VistaDayFoodPlan, '/day_food_training_plan')
api.add_resource(VistaDayFoodPlanID, '/day_food_training_plan/<id>')


jwt = JWTManager(app)


print(' * TRAINING MNGR corriendo ----------------')

if __name__=='__main__': 
    app.run(port=5001)