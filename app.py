# https://dash.plotly.com/tutorial?utm_medium=graphing_libraries&utm_content=python_footer
# https://dash-example-index.herokuapp.com/line-charts
# https://plotly.com/python/line-charts/
# https://plotly.com/python/styling-plotly-express/


# Import packages
from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('csv/Charlotin-hallucination_cases - Plotly Data.csv')

# Initialize the app
app = Dash()

fig=px.line(df, x='Month', y='Number of Cases',
            title='AI Flubs in Court Cases Have Been Steadily Rising Since Late 2024',
            subtitle='Legal decisions in cases where generative AI produced hallucinated content.',
            width=900, height=600, template='simple_white')

fig.update_traces(line_color='#ffa500')

fig.add_shape(type='rect',
    xref='x', yref='y',
    x0=17, y0=0,
    x1=25, y1=43,
    line=dict(
        color='#c0c0c0',
        width=3,
    ),
    fillcolor='#c0c0c0',
)

# App layout
app.layout = [
    dcc.Graph(figure=fig),
    html.Div([
        html.P('Hat tip to Jeremy Singer-Vine\'s \"Data is Plural\" Newsletter'),
        html.P(['Chart: ',
                html.A('Vasant Alex Laplam', href='https://www.lavasant.com'),
                ' | Source: ',
                html.A('Damien Charlotin', href='https://www.damiencharlotin.com/hallucinations/'),
                ' | Created with ',
                html.A('Dash', href='https://pypi.org/project/dash/')
              ])
    ]),
]


# Run the app
if __name__ == '__main__':
    app.run(debug=True)

# Go to this address in your browser to see the app
# http://127.0.0.1:8050/
