__author__ = 'Sergio'

import pandas as pd
from flask import Flask
from flask import render_template
from flask import request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
