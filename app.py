from flask import Flask
from flask import render_template
from flask import request
from args import *
app = Flask(__name__)
import numpy as np
import pickle
with open('Model.pkl', 'rb') as mod:
    model = pickle.load(mod)
with open('Scaler.pkl' ,'rb') as mod:
    scaler = pickle.load(mod)
@app.route("/" , methods=['GET' ,'POST'])
def index():
    if request.method == 'POST':
        bedrooms = request.form['bedrooms']
        bathrooms = request.form['bathrooms']
        location = request.form['location']
        sqf = request.form['sqf']
        status = request.form['status']
        direction = request.form['direction']
        property_type = request.form['property type']
        input_array = np.array([[
            bedrooms,bathrooms,location,sqf,status,direction,property_type
        ]])
    else:
        return render_template('index.html',location_mapping=location_mapping,
                               status_mapping=status_mapping,
                               direction_mapping=direction_mapping,
                               property_type_mapping=property_type_mapping)
@app.route("/secound")
def secound():
    return 'i love'

@app.route('/<name>/')
def Ilove(name):
    return f'I love you {name}'
# if __name__ == '__main__':
#     app.run(use_reloader=True, debug=True)