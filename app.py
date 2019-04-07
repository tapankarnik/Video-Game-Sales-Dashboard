import dash
import dash_core_components as dcc
import dash_html_components as html
from review2 import *
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import plotly.offline as py
# import plotly.graph_objs as go
# from plotly.offline import download_plotlyjs, plot


# print(df)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

BACKGROUND = 'rgb(230, 230, 230)'

colors = {
    'background': '#29E3FF',
    'text': '#111111',
    'wow' : '#29E3FF'
}

app.layout = html.Div([
    html.Div([
        # html.Img(src="https://s3-us-west-1.amazonaws.com/plotly-tutorials/logo/new-branding/dash-logo-by-plotly-stripe.png",
        #         style={
        #             'height': '100px',
        #             'float': 'right',
        #             'position': 'relative'
        #             # 'bottom': '0px',
        #             # 'left': '00px'
        #         },
        #         ),
        html.H2('Dash',
                style={
                    'position': 'relative',
                    'top': '0px',
                    'left': '10px',
                    'font-family': 'Dosis',
                    'display': 'inline',
                    'font-size': '6.0rem',
                    'color': '#4D637F'
                }),
        html.H2('for',
                style={
                    'position': 'relative',
                    'top': '0px',
                    'left': '20px',
                    'font-family': 'Dosis',
                    'display': 'inline',
                    'font-size': '4.0rem',
                    'color': '#4D637F'
                }),
        html.H2('Video Game Sales',
                style={
                    'position': 'relative',
                    'top': '0px',
                    'left': '27px',
                    'font-family': 'Dosis',
                    'display': 'inline',
                    'font-size': '6.0rem',
                    'color': '#4D637F'
                }),
    ], className='row twelve columns', style={'position': 'relative', 'right': '15px','backgroundColor' :BACKGROUND}),

    # html.H1(
    #     children='Video Game Sales with Ratings Dashboard',
    #     style={
    #         'textAlign': 'center',
    #         'color': colors['text']
    #         # 'backgroundColor': colors['']
    #     }
    # ),

    html.Div([
        html.H1('This is a Dashboard having various visualisations taken from the Video Game Sales with Ratings dataset.',
        style={
            'textAlign': 'left',
            'color': colors['text'],
            'backgroundColor':BACKGROUND
        }),
        html.Br(),
        html.Div([
            html.Div([
                html.Span('Plot 1',
                style={
                    'textAlign': 'center'
                }),
                dcc.Graph(
                    id='Plot1',
                    figure = fig1,
                    style=dict(width='1000px'),
                )
            ],style={'display': 'inline-block'}),
            html.Div([
                html.Span('Plot 2',
                style={
                    'textAlign': 'center'
                }),
                dcc.Graph(
                    id='Plot2',
                    style=dict(width='800px'),
                    figure = {
                        'data': data4,
                        'layout': {
                            'font': {
                                'color': colors['text'],
                            },
                            'paper_bgcolor': BACKGROUND,
                            'plot_bgcolor': BACKGROUND
                        },
                        'title' : 'Plote 2'
                    }
                )
            ],style={'display': 'inline-block'})
        ],style={'width': '100%', 'display': 'inline-block'}),
        html.Div(children='Plot3',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }),        
        dcc.Graph(
            id = 'Plot3',
            figure = {
                'data': data2,
                'layout' : {
                    'paper_bgcolor': BACKGROUND,
                    'plot_bgcolor': BACKGROUND
                }
            },
            
        ),
        html.Div([
            html.Div('Plot4',
            style={
                'textAlign': 'center',
                'color': colors['text']
            },
            className = 'two columns'
            ),
        dcc.Graph(
            id = 'Plot4',
            style=dict(width='800px',height = '800px',float = 'center',position = 'relative'),
            figure = fig4,
            className='ten columns'
            
        )
        ],className='row',style={'width': '100%', 'display': 'inline-block'})
        #,style={'width': '50%', 'display': 'inline-block','float' : 'center','position':'relative'})
    ])
],style = {'backgroundColor':BACKGROUND})

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "//fonts.googleapis.com/css?family=Dosis:Medium",
                "https://cdn.rawgit.com/plotly/dash-app-stylesheets/0e463810ed36927caf20372b6411690692f94819/dash-drug-discovery-demo-stylesheet.css"]

if __name__ == '__main__':
    app.run_server(debug=True,dev_tools_hot_reload = True)