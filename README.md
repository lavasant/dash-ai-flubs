# dash-ai-flubs
An exercise in creating a customized line chart using Python libraries.

I previously created this chart in [Datawrapper](https://www.datawrapper.de/_/LpjxR/?v=2):

![Datawrapper chart](./images/datawrapper_chart.png?raw=true "Title")

Then in [Flourish](https://public.flourish.studio/visualisation/24516000/):

![Flourish chart](./images/flourish_chart.png?raw=true "Title")

Then I wanted to see if I could re-create the chart using Python, so I started playing with Dash and Plotly.

Here's what I have as of August 14, 2025:

![Dash chart](./images/dash_chart.png?raw=true "Title")

To view the chart locally, run the app and then go to this address in your browser:
http://127.0.0.1:8050/

## TODO:
- Remove axes labels
- Clean up ticks on x-axis
- Refactor getcasesbymonth.py
