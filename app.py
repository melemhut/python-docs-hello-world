from flask import Flask, render_template
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import dash
import dash_core_components as dcc
import dash_html_components as html
from azure.storage.blob import BlockBlobService
from io import StringIO

app = Flask(__name__)

@server.route("/")
def hello():
    return "Hello from azure"
