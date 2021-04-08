from flask import Flask, render_template, request, Response, jsonify, url_for
import requests
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def result():


    number = requests.get('http://10.154.0.13:5000/').text
    letter = requests.get('http://10.154.0.13:5005/').text
    PrizeResult = number + letter
    if letter == ("A", "B", "C", "S", "a", "b", "c", "s"):
        print("you have Won a Prize")
    # if number >= 75:
    #     print("you have won a Prize")
    else:
        print("you didn't win a prize, better luck next time")


    return f'{PrizeResult}'

if __name__ == '__main__':
    app.run(port=5050, host='0.0.0.0', debug=True)