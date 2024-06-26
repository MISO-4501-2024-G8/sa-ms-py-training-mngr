# sa-ms-py-training-mngr
Plan Entrenamiento, Rutina de Alimentación y Rutina de Descanso y Definición situación critica

generar archivo de dependencias
```
pip3 freeze > requirements.txt
```

## Instrucciones para correr el proyecto

crear un entorno virtual
```
python3 -m venv venv
```
activar venv
```
source venv/bin/activate
```
instalar dependencias del archivo requirements.txt
```
pip3 install -r requirements.txt
```

correr flask Ambiente alto
```
export FLASK_APP=app/app.py
export DATABASE_URL=mysql+pymysql://admin:c5d5e19030104ba38e131c2ee8e76dec@dbsportapprestore.cvweuasge1pc.us-east-1.rds.amazonaws.com/db_training_plan
flask run -p 5001
```

correr flask Ambiente Bajo
```
export FLASK_APP=app/app.py
DATABASE_URL=sqlite:///prueba.db
flask run -p 5001
```

correr tests con pytest local
```
export FLASK_APP=app/app.py
export DATABASE_URL=sqlite:///prueba.db
pytest -s --cov=app/ --cov-report xml --junitxml=pytest-report.xml
coverage xml
coverage html -d coverage_report
```

correr tests con pytest ambiente productivo
```
unset DATABASE_URL
pytest --cov=app/ --cov-report xml --junitxml=pytest-report.xml
pytest -s --cov=app/ --cov-report xml --junitxml=pytest-report.xml
coverage xml
coverage html -d coverage_report
```


Generar imagen de docker
```
docker build -t training-mngr .
```

Correr imagen de docker
```
docker run -p 5001:5001 training-mngr
```