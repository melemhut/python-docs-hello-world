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

def connexion_blob_storage():
    return(BlockBlobService(account_name='prodthermalmanagementst', account_key='Az2kaMF26Vwd3lzztIIiteX2Ytbmn8tIriazHTu74Lm1O8lyui9i8o8qNdaZ1ceZ7Kh+Nn7BaxnOtLIBQBbK9g=='))
    
block_blob_service = connexion_blob_storage()
blobstring = block_blob_service.get_blob_to_text("processeddata","Cu_Cu_p.csv").content
df = pd.read_csv(StringIO(blobstring), sep=";", decimal=".",header=0)

@server.route("/")
def hello():
    return "Hello from azure"
