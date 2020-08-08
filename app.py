from joblib import load
import json
from flask import Flask, jsonify, render_template, url_for


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################


#################################################
# HTML ROUTES

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/treatment")
def profile():
    return render_template("treatment.html")

@app.route("/test.html")
def charts():
    return render_template("test.html")
    
@app.route("/test", methods=["POST", "GET"])
def test():
    # read data, do for each question, make sure the features are in correct order
    age = request.form['age']
    age = request.form['age']
    age = request.form['age']
    features = [age, x, x, x]
    
    
    # load model
    model = load("cancer_model.joblib")
    prediction = model.predict(features)
    # result is a 1 or 0 

    if prediciton == 1, diabetes
    else 

    return render_template ("prediction.html", prediction)


@app.route("/resources")
def bar():
    return render_template("resources.html")




