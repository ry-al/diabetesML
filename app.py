from joblib import load
import json
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
    age = request.form['age']
    print(age)
    # # read data, do for each question, make sure the features are in correct order
    # age = request.form['age']
    # height = request.form['height']
    # weight = request.form['weight']
    # pregnancy = request.form['pregnancy']
    # glucose = request.form['glucose']
    # bp = request.form['bp']
    # skin = request.form['skin']
    # insulin = request.form['insulin']
                
    # bmi = (703 * weight)/(height^2)

    # # user input list
    # features = [pregnancy, glucose, bp, skin, insulin, bmi, age]
    
    
    # # load model
    # model = load("result_complete.sav")
    # prediction = model.predict(features)
    # # result is a 1 or 0 

    # if prediction == 1:
    #     return render_template("high.html")
    # else:
    #     return render_template("low.html")

    return render_template('index.html')

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")


if __name__ == '__main__':
    app.run()


