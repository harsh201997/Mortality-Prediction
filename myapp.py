import flask
import pickle
import pandas as pd
import numpy as np
import sys

with open(f'model/covid_classsification.pkl', 'rb') as f:
    model = pickle.load(f)
with open(f'model/covid_regression.pkl', 'rb') as f:
	model1=pickle.load(f)
app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])

def main():

	if flask.request.method == 'GET':
		return(flask.render_template('covid.html'))

	if flask.request.method == 'POST':
		sex = flask.request.form['sex']
		sex = int(sex)
		intubated = flask.request.form['intubated']
		intubated = int(intubated)
		pneumonia = flask.request.form['pneumonia']
		pneumonia = int(pneumonia)
		age = flask.request.form['age']
		age = int(age)
		pregnancy = flask.request.form['pregnancy']
		pregnancy = int(pregnancy)
		diabetes = flask.request.form['diabetes']
		diabetes = int(diabetes)
		copd = flask.request.form['copd']
		copd = int(copd)
		asthma = flask.request.form['asthma']
		asthma =int(asthma)
		immunosuppression = flask.request.form['immunosuppression']
		immunosuppression = int(immunosuppression)
		hypertension = flask.request.form['hypertension']
		hypertension = int(hypertension)
		other_disease = flask.request.form['other_disease']
		other_disease = int(other_disease)
		cardiovascular = flask.request.form['cardiovascular']
		cardiovascular = int(cardiovascular)
		obesity = flask.request.form['obesity']
		obesity = int(obesity)
		renal_chronic = flask.request.form['renal_chronic']
		renal_chronic = int(renal_chronic)
		tobacco = flask.request.form['tobacco']
		tobacco = int(tobacco)
		icu = flask.request.form['icu']
		icu = int(icu)
		hospitalized = flask.request.form['hospitalized']
		hospitalized = int(hospitalized)

		input_variables = pd.DataFrame([[sex, intubated, pneumonia, age, pregnancy, diabetes, copd, asthma, immunosuppression, hypertension, other_disease, cardiovascular, obesity, renal_chronic, tobacco, icu, hospitalized]],columns=['sex', 'intubated', 'pneumonia', 'age', 'pregnancy', 'diabetes', 'copd', 'asthma', 'immunosuppression', 'hypertension', 'other_disease', 'cardiovascular', 'obesity', 'renal_chronic', 'tobacco', 'icu', 'hospitalized'])
		#input_variables = in_variables.to_numeric()
		answer = model.predict(input_variables)[0]
		answer1 = model1.predict(input_variables)[0]
		total = answer1
		h = total%1
		d = total//1
		days = int(d)
		hours = int(h*24)
		str1 = '<h1 style = "font-size = 30px; color:red;">Patient may die in {} days and {} hours.</h1>'.format(int(days), int(hours))
		str2 = '<h1 style = "font-size = 30px; color:green;">Patient is Safe.</h1>'
		if(answer == 1):
			prediction = str1
		else:
			prediction = str2

		return flask.render_template('covid.html',original_input={'sex':sex,'intubated':intubated,'pneumonia':pneumonia,'age':age,'pregnancy':pregnancy,'diabetes':diabetes,'copd':copd,'asthma':asthma,'immunosuppression':immunosuppression,'hypertension':hypertension,'other_disease':other_disease,'cardiovascular':cardiovascular,'obesity':obesity,'renal_chronic':renal_chronic,'tobacco':tobacco, 'icu':icu, 'hospitalized':hospitalized}, result=prediction)


if __name__ == '__main__':
    app.run(debug=True)

