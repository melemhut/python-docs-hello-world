from flask import Flask, render_template
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import dash
import dash_core_components as dcc
import dash_html_components as html

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Azure!"
