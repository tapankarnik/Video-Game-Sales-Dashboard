import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.offline as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot


df = pd.read_csv('data/vgsaleswithratings.csv')

BACKGROUND = '#FFFFFF'

# In[59]:


#Plot 1
def plot1graph(genre_value):
    if(genre_value == 'all'):
        x1 = df.groupby(['Year_of_Release']).count()['Global_Sales'] 
    else:
        x1 = df[df['Genre'] == genre_value].groupby(['Year_of_Release']).count()['Global_Sales'] 
    y1 = x1.index.astype(int)

    data1 = [go.Bar(x=y1, y=x1)]
    layout = dict(
        title='Time series with range slider and selectors - Video Game data',
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                        label='1m',
                        step='month',
                        stepmode='backward'),
                    dict(count=6,
                        label='6m',
                        step='month',
                        stepmode='backward'),
                    dict(count=1,
                        label='YTD',
                        step='year',
                        stepmode='todate'),
                    dict(count=1,
                        label='1y',
                        step='year',
                        stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(
                visible = True
            ),
            type='date'
        ),
        paper_bgcolor= BACKGROUND,
        plot_bgcolor= BACKGROUND
    )
    fig1 = dict(data=data1, layout=layout)
    return fig1



#Plot 2

platformdata = df['Platform'].value_counts() 
platformdata = platformdata.sort_values()

platformdata = platformdata.reset_index()
labels = platformdata['index']
values = platformdata['Platform']
trace = go.Pie(labels=labels, values=values)
data4 = [trace]


# platformdata.plot(kind='pie',labels='index', values='Platform')



#Plot 3

df2 = df.copy() 
df2 = df2.drop_duplicates(subset = "Name") 
df2 = df2['Developer'].value_counts().sort_values(ascending = False) 
df2 = df2[:20] 
df2 = df2.reset_index()
data2 = [go.Bar(x=df2['index'], y=df2['Developer'], name = 'Top 20 Developers by Number of Games Released', marker=dict(color='rgb(255, 0, 20)'))]

# py.plot(data2)



# Plot 4
df2 = df.copy()
df2.drop(['Name','Year_of_Release','Platform','Genre','Publisher','Developer','Rating','User_Count','User_Score'],axis = 1,inplace = True) 
df2.dropna(inplace=True)
trace = {
    "x" : [x for x in df2.columns.values],
    "y" : [x for x in df2.columns.values],
    "z" : df2.corr().values,
    "type" : 'heatmap',
    "reversescale": True
}
data = [trace]
layout = {
  "title": "Correlation Map", 
  "xaxis": {"ticks": ""}, 
  "yaxis": {"ticks": ""},
  'paper_bgcolor': BACKGROUND,
    'plot_bgcolor': BACKGROUND
}
fig4 = dict(data = data, layout = layout)
# py.plot(fig)








