import pickle
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model', 'titanic.model.pkl')

def load_model():
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    return model

def predict_survival(input_data):
    model = load_model()
    # input_data debe ser un array 2D, por ejemplo: [[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]]
    prediction = model.predict(input_data)
    return int(prediction[0])