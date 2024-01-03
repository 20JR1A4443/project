from flask import Flask
from flask import render_template
from flask import request
from args import *
app = Flask(__name__)
print(location_mapping)
@app.route("/" , methods=['GET' ,'POST'])
def index():
    if request.method == 'POST':
        return request.form  
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