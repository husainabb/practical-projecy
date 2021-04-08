from flask import Flask, render_template, request, Response, jsonify, url_for
app = Flask(__name__)
import requests

@app.route('/', methods=['GET', 'POST'])
def main():
    service4 = requests.get('http://10.154.0.13:5050/').text
  
    return render_template("main.html", title='Frontend', var=service4)

if __name__ == '__main__':
    app.run(port=5500, host='0.0.0.0', debug=True)   