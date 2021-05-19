from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse, abort,request
import random


app = Flask(__name__)
api = Api(app)


@app.route('/attack', methods=['POST'])
def generate_values():
    A = request.form.get("entry")
    B = request.form.get("end")
    N = request.form.get("Num")
    your_list = []
    for i in range(int(N)):
        your_list.append(round(random.uniform(float(A), float(B)), 2))
    print(your_list)
    return render_template('items.html', your_list=your_list)

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
