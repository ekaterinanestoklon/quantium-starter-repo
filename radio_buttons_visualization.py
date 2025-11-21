from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv("./output/pink_mosels_sales.csv")
df["date"] = pd.to_datetime(df["date"])

app.layout = html.Div(
    className="page-container",
    children=[
        html.H1("Pink Morsel Sales Dashboard"),

        html.Div(
            className="radio-block",
            children=[
                dcc.RadioItems(
                    id="region-radio",
                    options=[
                        {"label": html.Span("North"), "value": "north"},
                        {"label": html.Span("East"), "value": "east"},
                        {"label": html.Span("South"), "value": "south"},
                        {"label": html.Span("West"), "value": "west"},
                        {"label": html.Span("All"), "value": "all"},
                    ],
                    value="all",
                    inputStyle={"margin-right": "6px"}
                )
            ]
        ),

        dcc.Graph(id="sales-line-chart")
    ]
)


@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-radio", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"].str.lower() == selected_region]

    filtered_df = filtered_df.sort_values("date")

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Sales in the {selected_region.capitalize()} Region" 
              if selected_region != "all" else "Sales in All Regions",
        markers=True
    )

    # Clean mint theme styling
    fig.update_layout(
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff",
        title_x=0.5,
        font=dict(color="#2d8f82", size=16)
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)