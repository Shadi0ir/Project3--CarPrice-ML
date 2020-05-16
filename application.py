import numpy as np
import pandas as pd
from flask import Flask, render_template, request, jsonify
import pickle
import os, csv
os.environ['FOR_DISABLE_CONSOLE_CTRL_HANDLER'] = 'T'
from numpy import array
from sklearn.externals import joblib
from scipy import stats
from sklearn.preprocessing import MinMaxScaler

# Use pickle to load in the pre-trained model.



# create application
application = app = Flask(__name__, static_url_path='/static',
                        static_folder='static',
                        template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():

    if request.method == 'GET':
        return(render_template('index.html'))
    
    if request.method == 'POST':
        years = request.form['years']
        make = request.form['make']
        make = np.array(make)
        model = request.form['model']
        model = np.array(model)
        State = request.form['State']
        State = np.array(State)
        mileage = request.form['mileage']
        age = 2020 - int(years)
        mileage = int(mileage)
        # input_variables = pd.DataFrame([[age, make, model, State, mileage]],
        #                                columns=['age', 'make', 'model', 'State', 'mileage'],
        #                                dtype=float)

        # d = encoding(make,
        #             model)
        # print(d)

        # e = encoding2(State)
        # x = [[mileage,
        #      e[0],
        #      d[0],
        #      d[1],
        #      age]]
        # print(x)
        prediction = 8230.08
        # X_scaler = joblib.load("InputScaler")
        # x_scaled  = X_scaler.transform(x)
        # print(x_scaled)
        # model = joblib.load("UsedCarEstimator")
        # prediction = model.predict(x_scaled)
        # prediction = round(prediction[0],2)
        # print(prediction)
        return jsonify({'prediction':prediction})
@app.route('/get_options', methods=['GET'])
def options():
    df = pd.read_csv("data/form-values.csv",  dtype={"Year": int})
    data={}
    data['years'] = df['Year'].unique().tolist() 
    data['states'] = df['State'].unique().tolist() 
 
    data['makes'] = {}
    toyta_models = pd.read_csv("data/toyta_models.csv")
    data['makes']['Toyota'] = toyta_models['Model'].tolist()
    nishan_models =pd.read_csv("data/nishan_models.csv")
    data['makes']['Nissan'] = nishan_models['Model'].tolist()
    honda_models = pd.read_csv("data/honda_models.csv")
    data['makes']['Honda'] = honda_models['Model'].tolist()
    return jsonify(data)

# Read csv mapping file
# def encoding(make, model):
#     print(make)
#     print(model)
#     path_csv = os.path.join("data/mapping.csv")
#     with open(path_csv, newline="", encoding="UTF-8") as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         data = []
#         for row in csv_reader:
#             if ((row[3] == make) & (row[4] == model)).any():
#                 data.append(int(row[1]))
#                 data.append(int(row[2]))
                
#     return data

# def encoding2(State):
#     print(State)
#     path_csv = os.path.join("data/mappingstate.csv")
#     with open(path_csv, newline="", encoding="UTF-8") as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         data = []
#         for row in csv_reader:
#             if ((row[1] == State)).any():
#                 data.append(int(row[0]))

#     return data

if __name__ == '__main__':
    app.run(debug=True)