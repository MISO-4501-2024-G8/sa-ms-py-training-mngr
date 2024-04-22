from flask import Flask, render_template, jsonify

from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from modelos.modelos import db
# from vistas import statusCheck, VistaTrainingPlan
from vistas import statusCheck
from decouple import config

app=Flask(__name__) # NOSONAR

#DATABASE_URI = config('DATABASE_URL')  
#app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI 
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['JWT_SECRET_KEY'] = 'frase-secreta'
#app.config['PROPAGATE_EXCEPTIONS'] = True
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()
cors = CORS(app)


api = Api(app)



api.add_resource(statusCheck, '/status')
# api.add_resource(VistaTrainingPlan, '/create_training_plan')
# api.add_resource(VistaLogIn, '/api/auth/login')
# api.add_resource(VistaTask, '/api/task/<int:id_task>')
# api.add_resource(VistaFiles, '/api/files/<string:file_name>')

# api.add_resource(VistaActualizar, '/api/taskUpd/<int:id_task>')

jwt = JWTManager(app)


print(' * BACKEND corriendo ----------------')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
def health_check():
    response = {
        'status': 'OK'
    }
    return jsonify(response), 200



if __name__=='__main__':
    app.run(port=5001)