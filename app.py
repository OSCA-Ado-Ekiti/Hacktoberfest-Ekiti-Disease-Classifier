#importing needed library
import numpy as np
from flask import Flask, request, jsonify, render_template, Request
from joblib import load
import sklearn

# Create flask app
app = Flask(__name__)
# model = load("model.joblib")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

# @app.route("/loan_status", methods = ["POST"])
# def loan_status():
#     person_age = request.form.get('person_age')
#     person_income = request.form.get('person_income')
#     home_ownership = request.form.get('home_ownership')
#     emp_length = request.form.get('emp_length')
#     loan_intent = request.form.get('loan_intent')
#     loan_grade = request.form.get('loan_grade')
#     loan_amnt = request.form.get('loan_amnt')
#     cred_hist_length = request.form.get('cred_hist_length')

#     pred = model.predict([[person_age, person_income, home_ownership, 
#                            emp_length, loan_intent, loan_grade, loan_amnt, cred_hist_length]])

#     if pred[0] == 0:
#         return render_template('non_default.html')
#     else:
#         return render_template('default.html')


if __name__ == "__main__":
    app.run(debug=True)