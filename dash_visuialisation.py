import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv("./output/pink_mosels_sales.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = dash.Dash(__name__)

fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales Over Time")

app.layout = html.Div(children=[
    html.H1(children="Soul Foods Sales Visualizer"),
    dcc.Graph(figure=fig)
])


if __name__ == "__main__":
    app.run(debug=True)