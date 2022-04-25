import re
import joblib
from flask import Flask, render_template, request
import preprocess  
import numpy as np

app = Flask(__name__)

scaler = joblib.load(r'C:\Users\ascom\Downloads\Heart-Disease\Models\scaler.h5')
model = joblib.load(r'C:\Users\ascom\Downloads\Heart-Disease\Models\model.h5')

@app.route('/') 
def index() :
    return render_template('index.html')

@app.route('/predict', methods = ['POST', 'GET']) 
def get_prediction() :
    
    if request.method == 'POST' :
        BMI = request.form['BMI']
        Smoking = request.form['smoker']
        AlcoholDrinking = request.form['Alcohol_drink']
        Stroke = request.form['stroke']
        PhysicalHealth = request.form['PhysicalHealth']
        MentalHealth = request.form['MentalHealth']
        DiffWalking = request.form['Diff_walk']
        Sex = request.form['sex']
        AgeCategory = request.form['age_category']
        Race = request.form['race']
        Diabetic = request.form['diabetic']
        PhysicalActivity = request.form['physical_activity']
        GenHealth = request.form['general_health']
        SleepTime = request.form['sleep_time']
        Asthma = request.form['asthma']
        KidneyDisease = request.form['kidney_disease']
        SkinCancer = request.form['skin_cancer']



        data = {'BMI': BMI, 'Smoking': Smoking, 'AlcoholDrinking': AlcoholDrinking, 'Stroke': Stroke, 
        'PhysicalHealth': PhysicalHealth, 'MentalHealth': MentalHealth, 'DiffWalking': DiffWalking, 'Sex':Sex,
         'AgeCategory': AgeCategory, 'Race': Race, 'Diabetic': Diabetic, 'PhysicalActivity': PhysicalActivity,
          'GenHealth': GenHealth, 'SleepTime': SleepTime, 'Asthma': Asthma, 'KidneyDisease': KidneyDisease,
           'SkinCancer': SkinCancer }
    
    final_data = preprocess.Preprocess(data)
    scaled_data= scaler.transform([final_data])
    prediction = model.predict(scaled_data)
    prediction=prediction[0]
    
    #return str(round(prediction))
    return render_template('prediction.html',heart_disease=str(prediction))

if __name__ == '__main__' :

    app.run(debug = True)


