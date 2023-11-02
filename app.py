#importing needed library
import numpy as np
from flask import Flask, request, jsonify, render_template, Request
from joblib import load
import sklearn

# Create flask app
app = Flask(__name__)
model = load("model.joblib")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods = ["POST"])
def result():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]

    prognosis = {'Allergy': 0, 'Peptic ulcer diseae': 1, 'Diabetes ': 2, 'Gastroenteritis': 3,
       'Bronchial Asthma': 4, 'Hypertension ': 5, 'Migraine': 6, 'Malaria': 7,
       'Chicken pox': 8, 'Typhoid': 9, 'hepatitis A': 10, 'Hepatitis B': 11,
       'Hepatitis C': 12, 'Hepatitis D': 13, 'Hepatitis E': 14, 'Tuberculosis': 15,
       'Common Cold': 16, 'Pneumonia': 17, 'Acne': 18, 'Urinary tract infection': 19}

    def get_result_key(prog_dict, result_value):
        for key, value in prog_dict.items():
            if value == result_value:
                return key

    prediction = model.predict(features)

    result_key = get_result_key(prognosis, prediction)

    return render_template("form.html", prediction_text = "The result of your diagnosis is {result_key}, visit your doctor")

if __name__ == "__main__":
    app.run(debug=True)