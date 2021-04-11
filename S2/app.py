from flask import Flask, request
from random import randint
app = Flask(__name__)

@app.route('/', methods=['GET'])
def NumGenerator():

    RandomNum = randint(0, 9)

 

    random = randint(0, 20)

    return f'{RandomNum}'

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)