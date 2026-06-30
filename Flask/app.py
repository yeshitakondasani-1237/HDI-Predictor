import numpy as np
import pandas as pd
import pickle
try:
    from flask import Flask, render_template, request
except ImportError as e:
    raise ImportError("Flask is not installed. Install it with 'pip install flask'.") from e

app = Flask(__name__)
model = pickle.load(open('HDI.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Prediction', methods=['POST', 'GET'])
def prediction():
    return render_template('indexnew.html')

@app.route('/Home', methods=['POST', 'GET'])
def my_home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    features_name = ['Country', 'Life expectancy', 'Mean years of schooling', 'Gross national income (GNI) per capita']
    df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict(df)
    y_pred = round(output[0][0], 2)

    if 0.3 <= y_pred <= 0.549:
        result = f'Low HDI — Score: {y_pred}'
    elif 0.55 <= y_pred <= 0.699:
        result = f'Medium HDI — Score: {y_pred}'
    elif 0.7 <= y_pred <= 0.799:
        result = f'High HDI — Score: {y_pred}'
    elif 0.8 <= y_pred <= 0.94:
        result = f'Very High HDI — Score: {y_pred}'
    else:
        result = f'Score: {y_pred} — Please check input values'

    return render_template('resultnew.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)