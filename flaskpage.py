import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__)
model = pickle.load(open('liver.pkl', 'rb'))

def getParameters():
    parameters = []
    parameters.append(request.form['age'])
    parameters.append(request.form['sex'])
    parameters.append(request.form['Total_Bilirubin'])
    parameters.append(request.form['Direct_Bilirubin'])
    parameters.append(request.form['Alkaline_Phosphotase'])
    parameters.append(request.form['Alamine_Aminotransferase'])
    parameters.append(request.form['Aspartate_Aminotransferase'])
    parameters.append(request.form['Total_Protiens'])
    parameters.append(request.form['Albumin'])
    parameters.append(request.form['Albumin_and_Globulin_Ratio'])
    return parameters


@app.route("/")
def home():
    return render_template('form.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    parameters = getParameters()
    inputFeature = np.asarray(parameters).reshape(1, -1)
    my_prediction = model.predict(inputFeature)



    print(inputFeature)
    print(my_prediction)

    output = round(float(my_prediction[0]), 2)
    if(output == 1):
        return render_template('form.html',prediction_text='High chances of Liver disease.Consult doctor!')
    if (output == 0):
        return render_template('form.html', prediction_text='Low chances of Liver disease. Chill !!')

if __name__ == "__main__":
    app.run(debug=True)