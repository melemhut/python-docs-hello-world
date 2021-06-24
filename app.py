from flask import Flask, render_template
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import dash
import dash_core_components as dcc
import dash_html_components as html

app = Flask(__name__)

# Folder where we go to read the merged files
PROCESSDIRECTORY = 'C:\\Test_processed\\'
# Encoding of files
FILEENCODING = 'latin1'

# cu = pd.read_csv(PROCESSDIRECTORY + "JLR-IPace-N1_Cu", encoding=FILEENCODING, sep=';', header=0)
# cup = pd.read_csv(PROCESSDIRECTORY + "JLR-IPace-N1_Cu_p", encoding=FILEENCODING, sep=';', header=0)


app = Flask(__name__)
# app = dash.Dash(
    # __name__,
    # server=server,
    # url_base_pathname='/dash/'
# )

# app.layout = html.Div(children=[
    # html.H1(children='Hello Dash'),

    # html.Div(children='''
        # This is Dash running on Azure App Service.
    # '''),

    # dcc.Graph(
        # id='example-graph',
        # figure={
            # 'data': [
                # {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                # {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            # ],
            # 'layout': {
                # 'title': 'Dash Data Visualization'
            # }
        # }
    # )
# ])

# @server.route("/")
# def hello():
    # sns.distplot(cu["Cu"], rug=True, hist=False)
    # return render_template('cu.html', name = plt.show())

# @server.route("/dash")
# def my_dash_app():
    # return app.index()

@app.route("/")
def hello():
    return "Hello from azure"


#if __name__ == '__main__':
#   server.run(debug = True,port=80)
