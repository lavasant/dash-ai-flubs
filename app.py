# https://dash.plotly.com/tutorial?utm_medium=graphing_libraries&utm_content=python_footer
# https://dash-example-index.herokuapp.com/line-charts
# https://plotly.com/python/line-charts/
# https://plotly.com/python/styling-plotly-express/


# Import packages
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('csv/Charlotin-hallucination_cases - Plotly Data.csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    dcc.Graph(figure=px.line(df, x='Month', y='Number of Cases',
                             title='AI Flubs in Court Cases Have Been Steadily Rising Since Late 2024',
                             width=1200, height=800,
                             template='simple_white',
                             color_discrete_map={'Number of Cases': 'Orange'},
    ))
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

# Go to this address in your browser to see the app
# http://127.0.0.1:8050/
