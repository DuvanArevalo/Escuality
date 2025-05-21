import re
from flask import Flask, render_template, request
from datetime import datetime
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')