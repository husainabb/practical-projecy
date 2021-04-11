from flask import Flask, render_template, request, Response, jsonify, url_for
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)


class Prize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    letter = db.Column(db.String(20), nullable=False)
    number = db.Column(db.String(10), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def main():
    service4 = requests.get('http://10.154.0.13:5050/').text

    prize_reward = Prize(letter = letter_response.text, number=number_response.text)
    db.session.add(prize_reward)
    db.session.commit()

    all_prize = Prize.query.all()
  
    return render_template("main.html", title='Frontend', var=service4, letter=letter_response.text, number=number_response.text, all_prize=all_prize)

if __name__ == '__main__':
    app.run(port=5500, host='0.0.0.0', debug=True)   