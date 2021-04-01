from flask import Flask
from flask import render_template

import pandas as pd
import json

app = Flask(__name__)


@app.route('/')
def weather():
    return render_template('weather.html')
