import os
import sys
import json
import pickle
import numpy as np

# Obtener la ruta absoluta del directorio del script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construir ruta absoluta al modelo
model_path = os.path.join(script_dir, 'titanic.model.pkl')

# Carga el modelo guardado en model.pkl usando la ruta absoluta
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# El resto igual
data_json = sys.argv[1]
data = json.loads(data_json)

X = np.array([[ 
    data['Pclass'], 
    data['Sex'], 
    data['Age'], 
    data['SibSp'], 
    data['Parch'], 
    data['Fare'], 
    data['Embarked'] 
]])

pred = model.predict(X)

print(json.dumps({'prediction': int(pred[0])}))
