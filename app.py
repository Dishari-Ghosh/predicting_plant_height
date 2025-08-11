# app.py
from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib

app = Flask(__name__)

# If not using a model file, manually set your computed values:
COEF = 0.7631813247797825
INTERCEPT = 4.571382116198556
R2 = 0.5457811295214343
MSE = 4.24232378085471

@app.route('/')
def index():
    return render_template('index.html')  # see HTML snippet below

@app.route('/predict', methods=['POST'])
def predict():
    try:
        sunlight = float(request.form['sunlight'])
    except (KeyError, ValueError):
        return render_template('result.html', error="Invalid input\nPlease try with some numeric values")
    
    pred = COEF * sunlight + INTERCEPT
    return render_template('result.html', prediction=round(pred, 4))

@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json(force=True)
    try:
        sunlight = float(data.get('sunlight'))
    except (TypeError, ValueError):
        return jsonify({'error': 'Please provide a numeric "sunlight" value'}), 400
    
    pred = COEF * sunlight + INTERCEPT
    return jsonify({
        'prediction': pred,
        'model': {
            'coef': COEF,
            'intercept': INTERCEPT,
            'R2': R2,
            'MSE': MSE
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
