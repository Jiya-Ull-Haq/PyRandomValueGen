from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse, abort,request
import random


app = Flask(__name__)
api = Api(app)
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True


@app.route('/result', methods=['POST'])
def generate_values():
    A = request.form.get("entry")
    B = request.form.get("end")
    N = request.form.get("Num")
    your_list = []
    for i in range(int(N)):
        your_list.append(round(random.uniform(float(A), float(B)), 2))
    print(your_list)
    return render_template('generator.html', your_list=your_list)

@app.route('/Random-Generator')
def generator():
    return render_template('generator.html')

@app.route('/')
def main_app():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
