from joblib import load
import json
import numpy as np
from flask import Flask, jsonify, render_template, url_for, request


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
def treatment():
    return render_template("treatment.html")

@app.route("/test")
def test():
    return render_template("test.html")

    
# @app.route("/quickTest", methods=["POST", "GET"])
# def quickTest():
#     # read data, do for each question, make sure the features are in correct order
#     age1 = request.form['age1']
#     height1 = request.form['height1']
#     weight1 = request.form['weight1']

#     bmi1 = (703 * weight1)/(height1^2)
    
#     # user input list
#     features1 = [age1, bmi1]
    
#     # load model
#     model = load("predictions_1.sav")
#     prediction = model.predict(features)
    
#     # result is a 1 or 0 
#     if prediction == 1:
#         return render_template("high.html")
#     else 
#         return render_template("low.html")


@app.route("/completeTest", methods=["POST", "GET"])
def completeTest():
    print("hello")
    print(request.form.keys())
    # read data, do for each question, make sure the features are in correct order
    age = int(request.form['age'])
    print(type(age))
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    pregnancy = int(request.form['pregnancy'])
    glucose = int(request.form['glucose'])
    bp = int(request.form['bp'])
    skin = int(request.form['skin'])
    insulin = int(request.form['insulin'])
    pedigree = float(request.form['pedigree'])

    height = float(height)
    weight = float(weight)
                
    bmi = (703 * weight)/(height*height)

    # user input list
    features = [pregnancy, glucose, bp, skin, insulin, bmi, pedigree, age]
    
    final_features = [np.array(features)]
    final_shape = np.reshape(final_features,(1,-1))
    
    # load model
    model = load("classifier_complete.sav")
    prediction = model.predict(final_shape)
    print(prediction)
    final_predict = prediction[0]
    

    if prediction == 1:
        return render_template("high.html")
    else:
        return render_template("low.html")

    return render_template('index.html')



@app.route("/analytics")
def analytics():
    return render_template("analytics.html")


if __name__ == '__main__':
    app.run(debug=True)


