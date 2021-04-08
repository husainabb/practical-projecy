from flask import Flask, request
from random import randint
import random
import string
app = Flask(__name__)

@app.route('/', methods=['GET'])
def RanLetterGenerator():
    LetterGenerators = ["a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, v, u, w, x, y, z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, V, U, W, X, Y, Z"]
   
    return f'{random.choice(string.ascii_letters)}'

if __name__ == '__main__':
    app.run(port=5005, host='0.0.0.0', debug=True)