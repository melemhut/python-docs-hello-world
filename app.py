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
    
#block_blob_service = connexion_blob_storage()
#blobstring = block_blob_service.get_blob_to_text("processeddata","Cu_Cu_p.csv").content
#df = pd.read_csv(StringIO(blobstring), sep=";", decimal=".",header=0)

#blob_client = blob_service_client.get_blob_client(container=r"processeddata",blob="Cu_Cu_p.csv")
# cu = pd.read_csv(PROCESSDIRECTORY + "JLR-IPace-N1_Cu", encoding=FILEENCODING, sep=';', header=0)
# cup = pd.read_csv(PROCESSDIRECTORY + "JLR-IPace-N1_Cu_p", encoding=FILEENCODING, sep=';', header=0)


app = Flask(__name__)
app1 = dash.Dash(
    __name__,
    server=server,
    url_base_pathname='/dash/'
)

app1.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        This is Dash running on Azure App Service.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

@app.route("/")
def hello():
    sns.distplot(df["Cu"], rug=True, hist=False)
    return render_template('cu.html', name = plt.show())

@app.route("/dash")
def my_dash_app():
    return app1.index()
