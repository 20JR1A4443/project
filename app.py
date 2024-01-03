from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/" , methods=['GET' ,'POST'])
def index():
    return render_template('index.html')
@app.route("/secound")
def secound():
    return 'i love'

@app.route('/<name>/')
def Ilove(name):
    return f'I love you {name}'
# if __name__ == '__main__':
#     app.run(use_reloader=True, debug=True)