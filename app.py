import dash
import dash_core_components as dcc
import dash_html_components as html
from review2 import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



colors = {
    'background': '#29E3FF',
    'text': '#111111',
}

app.layout = html.Div([
    html.Div([
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
        html.Img(src="assets/dash-logo-by-plotly-stripe.png",
                style={
                    'height': '110px',
                    'float': 'right',
                    'position': 'relative'
                },
                ),        
        html.Hr(style={'margin': '30', 'margin-bottom': '5'}),
    ], style={'margin':30,'position': 'relative', 'right': '15px','backgroundColor' :BACKGROUND}),

    html.Div([
        html.H3('This is a Dashboard having various visualisations taken from the Video Game Sales with Ratings dataset.',
        style={
            'color': colors['text'],
            'backgroundColor':BACKGROUND,
            'margin': '30px'
        }),
        html.Br(),
        html.Div([
            html.Div([
                html.Div('Plot 1',
                    style={
                        'textAlign': 'center'
                    }
                ),
                html.Div('From this plot, we can see that approx. from the 2000s there is a boom in the release of video games. More and more developers\n started releasing games and it peaked at 2008 and 2009 after which the number declined. This might have happened due to the\n increase in price of the biggest titles. The resize bar in this plot allows us to zoom into the plot and see detailed information.\n\n The following Graph has been initialized with all genres of games. Use the Dropdown list below to view data for individual genres',
                    style={
                        'white-space': 'pre',
                        'margin': '30px',
                    }
                ),
                dcc.Dropdown(
                    id='plot1-dropdown',
                    options=[
                        {'label': 'All','value':'all'},
                        {'label': 'Sports', 'value': 'Sports'},
                        {'label': 'Platform', 'value': 'Platform'},
                        {'label': 'Racing', 'value': 'Racing'},
                        {'label': 'Role-Playing', 'value': 'Role-Playing'},
                        {'label': 'Puzzle', 'value': 'Puzzle'},
                        {'label': 'Misc', 'value': 'Misc'},
                        {'label': 'Shooter', 'value': 'Shooter'},
                        {'label': 'Simulation', 'value': 'Simulation'},
                        {'label': 'Action', 'value': 'Action'},
                        {'label': 'Fighting', 'value': 'Fighting'},
                        {'label': 'Adventure', 'value': 'Adventure'},
                        {'label': 'Strategy', 'value': 'Strategy'},
                    ],
                    value='all'
                ),
                dcc.Graph(
                    id='Plot1',
                    figure = plot1graph('all'),
                    style=dict(width='1000px')
                )
            ],style={'display': 'inline-block','margin':5}),
            html.Div([
                html.Div('Plot 2',
                style={
                    'textAlign': 'center',
                    'white-space': 'pre'
                }),
                html.Br(),
                html.Div('This visualization shows us the number of unique games released on each gaming console as a pie chart. At a \nglance, it is apparent that the PS2 and Nintendo DS have the greatest number of games released. This chart \nis for those people who are worried about buying a console without enough games released on it. The interactivity \nin this pie chart allows us to hover the mouse over a section and see the numeric value and percentage of the\n portion occupied by the game console.',
                style={
                    'textAlign': 'center',
                    'white-space': 'pre'
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
            ],style={'display': 'inline-block','margin':5})
        ],style={'width': '100%', 'display': 'inline-block','margin':5}),
        html.Div(children='Plot3',
            style={
                'textAlign': 'center',
                'color': colors['text'],
                'margin': '30px',
                'fontSize':19
            }
        ), 
        html.Div(children='This plot shows us the top 20 developers by the number of games released. It gives us information about prolific developers in the industry and is a good measure to see if they make quality games. There is a very good chance that a new game by any of these developers will be a big hit.',
            style={
                'textAlign': 'center',
                'color': colors['text'],
                'margin': '30px',
                'fontSize':19            
            }
        ),        
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
            html.Div('Plot 4',
            style = {
                'margin': '30px',
                'fontSize':19,
            }),
            html.Div("This plot shows us the correlation of the regional sales, global sales and the critic score and count. The most important part  of this graph should be the critic score. We need to see if the critic score corresponds with the various sales data. Here the critic score seems to correspond the most with the global sales and least with the Japan Sales. This means that a higher critic score corresponds to a higher global sales number while it may not be true considering Sales in Japan.",
            style={
                'margin': '30px',
                'top':'50px',
                'fontSize':19
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
    ])
],style = {'backgroundColor':BACKGROUND,'margin':30,'backgroundImage':'assets/zelda_bg.jpg'})

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "//fonts.googleapis.com/css?family=Dosis:Medium",
                "https://cdn.rawgit.com/plotly/dash-app-stylesheets/0e463810ed36927caf20372b6411690692f94819/dash-drug-discovery-demo-stylesheet.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

@app.callback(
    dash.dependencies.Output('Plot1', 'figure'),
    [dash.dependencies.Input('plot1-dropdown', 'value')])
def update_plot1(genre_value):
    return plot1graph(genre_value)


if __name__ == '__main__':
    app.run_server(debug=True,dev_tools_hot_reload = True)