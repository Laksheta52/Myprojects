from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle

app = Flask(__name__)
CORS(app)

with open('models.pkl', 'rb') as file:
    models = pickle.load(file)

with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

def output_label(n):
    return "Fake news" if n == 0 else "Not a Fake news"

@app.route('/process', methods=['POST'])
def process_input():
    data = request.json
    input_text = data.get('input_text', '')

    vectorized_text = vectorizer.transform([input_text])
    
    predictions = {}

    for model_name, model in models.items():
        prediction = model.predict(vectorized_text)[0]
        predictions[model_name] = output_label(prediction)
    
    return jsonify(predictions)
    
    """predictions = []

    # Generate predictions for each model and add to the list
    for model_name, model in models.items():
        prediction = model.predict(vectorized_text)[0]
        predictions.append(output_label(prediction))
    
    return jsonify(predictions)"""

if __name__ == '__main__':
    app.run(debug=True, port=5000)
