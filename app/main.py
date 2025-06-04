from app import app
from flask import request, jsonify
from app.predict import predict_survival
from flask import send_from_directory


@app.route('/titanic')
def front():
    return send_from_directory('../templates', 'index.html')

@app.route('/')
def home():
    return "Bienvenido a la predicción del Titanic"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Extrae y prepara los datos según tu modelo
    # Ejemplo: espera un JSON con las claves correctas
    features = [
        data['Pclass'],
        data['Sex'],
        data['Age'],
        data['SibSp'],
        data['Parch'],
        data['Fare'],
        data['Embarked']
    ]
    # Convierte Sex y Embarked si es necesario (por ejemplo, a números)
    # Aquí debes adaptar según cómo entrenaste tu modelo
    features[1] = 1 if features[1].lower() == 'male' else 0
    embarked_map = {'C': 0, 'Q': 1, 'S': 2}
    features[6] = embarked_map.get(features[6].upper(), 2)
    prediction = predict_survival([features])
    return jsonify({'survived': prediction})