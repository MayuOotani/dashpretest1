import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import sqlite3

app = dash.Dash(__name__)
server = app.server

def getTreeData(dbname):
    db = sqlite3.connect(dbname)
    c = db.cursor()
    q = c.execute("SELECT * FROM QiU")
    qiu = []
    ach = 0
    for row in q:
        list = [row[1], "", row[2], row[3]]
        qiu.append(list)
    #print(qiu)
    colums = ["qiu", "parent", "priority", "achievement"]
    qiu_data = pd.DataFrame(data=qiu, columns=colums)
    return qiu_data

dash_app.layout = html.Div(
    [
        html.Div(id="description", className="text"),
        dcc.Location(id="my_location"),
        html.Div(
            id="show_location",
            #style={"fontSize":30, "textAlign": "center", "height": 400}
        ),
        html.Br(),
        html.Div(
            [
                dcc.Link(
                    "home", 
                    href="home",
                    style={"margin":"5px"}
                ),
                dcc. Link(
                    "Q1",
                    href="Q1",
                    style={"margin":"5px"}
                ),
                dcc.Link(
                    "Q2",
                    href="Q2",
                    style={"margin":"5px"}
                ),
                dcc.Link(
                    "Q3",
                    href="Q3",
                    style={"margin": "5px"}
                ),
                dcc.Link(
                    "Q4",
                    href="Q4",
                    style={"margin": "5px"}
                ),
                dcc.Link(
                    "Q5",
                    href="Q5",
                    style={"margin": "5px"}
                ),
                dcc.Link(
                    "Q6",
                    href="Q6",
                    style={"margin": "5px"}
                ),
                dcc.Link(
                    "Q7",
                    href="Q7",
                    style={"margin": "5px"}
                )
            ],
            className="link"
        )
    ],
    style={
        "position": "relative",
        "padding-bottom;": "3rem"
    }
)

#スタート画面
start = html.Div(
    [
        html.H1(
            "予備実験",
            style={"textAlign": "center"}
        ),
        dcc.Link("Q1", href="Q1",),
        html.Br(),
        dcc.Link("Q2", href="Q2"),
        html.Br(),
        dcc.Link("Q3", href="Q3"),
        html.Br(),
        dcc.Link("Q4", href="Q4"),
        html.Br(),
        dcc.Link("Q5", href="Q5"),
        html.Br(),
        dcc.Link("Q6", href="Q6"),
        html.Br(),
        dcc.Link("Q7", href="Q7"),
    ],
    style={
        "textAlign": "center"
    }
)

#数値*面積(QSM.db)
test1 = html.Div([
    html.Div(
        [
            html.P(
                "実用性",
                className="qiu",
            ),
            html.P(
                "75.8%",
                className="achieve"
            ),
        ],
        id = "high1",
        className="box"
    ),
    html.Div(
        [
            html.P(
                "効率性",
                className="qiu",
            ),
            html.P(
                "76.9%",
                className="achieve"
            )
        ],
        id = "low1",
        className="box",
    ), 
    html.Div(
        [
            html.P(
                "信用性",
                className="qiu",
            ),
            html.P(
                "59.0%",
                className="achieve"
            )
        ],
        id = "middle1",
        className="box"
    ),
],
    style={
        "display": "flex",
        "align-items": "flex-end"
    }
)

#数値*色(QSM6)
colorlist = px.colors.sequential.Blues
test2 = html.Div(
    [
        html.Div(
        [
            html.P(
                "実用性",
                className="qiu"
            ),
            html.P(
                "80.1%",
                className="achieve"
            ),
        ],
        className="test2",
        style={
            "color": colorlist[3]
        }
        ),
        html.Div(
        [
            html.P(
                "効率性",
                className="qiu"
            ),
            html.P(
                "79.1%",
                className="achieve"
            )
        ],
        className="test2",
        style={
            "color": colorlist[2]
        }
        ),
        html.Div(
        [
            html.P(
                "信用性",
                className="qiu"
            ),
            html.P(
                "56.6%",
                className="achieve"
            )
        ],
        className="test2",
        style={
            "color": colorlist[7]
        }
        ),
    ]
)

#数値*レイアウト(QSM4)
test3 = html.Div(
    [
        html.Div(
        [
            html.P(
                "信用性",
                className="qiu",
            ),
            html.P(
                "59.0%",
                className="achieve"
            ),
        ],
        className="test5"
        ),
        html.Div(
            style={
                "width": "100px",
                "height": "10px",
                "display": "inline-block"
            }
        ),
        html.Div(
        [
            html.P(
                "実用性",
                className="qiu",
            ),
            html.P(
                "75.8%",
                className="achieve"
            )
        ],
        className="test5"
        ), 
        html.Div(
        [
            html.P(
                "効率性",
                className="qiu",
            ),
            html.P(
                "76.9%",
                className="achieve"
            )
        ],
        className="test5",
        ),
        html.P(
            "　　　　　　5　　　　　　　　　　4　　　　　　　　　3　　　　　　　　　　　　2　　　　　　　　　　　1",
            style={
                "display": "flex",
            }
        ),
        html.P(
            "高　　　　　　　　　　　　　　　　　　　　　　←重要度→　　　　　　　　　　　　　　　　　　　　　　低",
            style={
                "display": "flex",
            }
        )
    ],
    style={
        "display": "flex-box",
        "justify-content": "flex-start"
    }
)

#面積*色(QSM3)
db3 = getTreeData("QSM3.db")
tree = px.treemap(
            db3, path=["parent", "qiu"], 
            values="achievement", 
            color="priority",
            color_continuous_scale=px.colors.sequential.Blues,
            range_color=[0, 5]             
        )
tree.update_traces(hovertemplate=None, hoverinfo="skip")
test4 = html.Div(
    [
        dcc.Graph(
            figure=tree
        )
    ]    
)

#面積*レイアウト(QSM)
db = getTreeData("QSM.db")
db.iat[0,0] = "実用性(5)"
db.iat[1,0] = "効率性(3)"
db.iat[2,0] = "信用性(4)"
#print(db)
bar = px.bar(
            db.reindex(index=[0, 2, 1]), 
            x="qiu",
            y="achievement",       
        )
bar.update_yaxes(
    showgrid=False,
    showticklabels=False,
    title={"text": "達成度"}
)
bar.update_xaxes(title={"text": "利用時の品質(高←重要度→低)"})
bar.update_traces(hovertemplate=None, hoverinfo="skip")

test5 = html.Div(
    [
        dcc.Graph(figure=bar)
    ]
)

#色*面積(QSM2)
db2 = getTreeData("QSM2.db")
tree2 = px.treemap(
            db2, path=["parent", "qiu"], 
            values="priority", 
            color="achievement",
            color_continuous_scale=[
                [0, "red"],
                [0.5, "yellow"],
                [1, "lime"]
            ],
            range_color=[0, 100]             
        )
tree2.update_traces(hovertemplate=None, hoverinfo="skip")
test6 = html.Div(
    [
        dcc.Graph(figure=tree2)
    ]
)

#色*レイアウト(QSM7)
db7 = getTreeData("QSM7.db")
db7.iat[0,0] = "実用性(5)"
db7.iat[1,0] = "効率性(4)"
db7.iat[2,0] = "信用性(2)"
db7["val"] = 1
bar2 = px.bar(
            db7, 
            x="qiu",
            y="val",
            color="achievement",
            color_continuous_scale=[
                [0, "red"],
                [0.5, "yellow"],
                [1, "lime"]
            ],
            range_color=[0, 100]      
        )
bar2.update_yaxes(
    showgrid=False,
    showticklabels=False,
    title={"text": ""}
)
bar2.update_xaxes(title={"text": "利用時の品質(高←重要度→低)"})
bar2.update_traces(hovertemplate=None, hoverinfo="skip")
test7 = html.Div(
    [
        dcc.Graph(figure=bar2)
    ]
)

@app.callback(
    Output("show_location", "children"), Output("description", "children"), Input("my_location", "pathname")
)
def update_location(pathname):
    text = ["ここに説明が出ます"]
    if pathname == "/Q1":
        text=[
            html.H2("Q1"),
            html.P("面積：重要度(大きい方が重要)"),
            html.P("数値：達成度(数値が大きい方が達成度が高い)")
        ]
        return test1, text
    elif pathname == "/Q2":
        text=[
            html.H2("Q2"),
            html.P("色：重要度(色が濃い方が重要)"),
            html.P("数値：達成度(数値が大きい方が達成度が高い)")
        ]
        return test2, text
    elif pathname == "/Q3":
        text=[
            html.H2("Q3"),
            html.P("並び順：重要度(左側の方が重要 下の数値が重要度)"),
            html.P("数値：達成度(数値が大きい方が達成度が高い)")
        ]
        return test3, text
    elif pathname == "/Q4":
        text=[
            html.H2("Q4"),
            html.P("色：重要度(色が濃い方が重要)"),
            html.P("面積：達成度(大きい方が達成度が高い)")
        ]
        return test4, text
    elif pathname == "/Q5":
        text=[
            html.H2("Q5"),
            html.P("並び順：重要度(左側の方が重要　カッコ内の数値が重要度)"),
            html.P("面積：達成度(大きい方が達成度が高い)")
        ]
        return test5, text
    elif pathname == "/Q6":
        text=[
            html.H2("Q6"),
            html.P("面積：重要度(大きい方が重要)"),
            html.P("色：達成度(緑の方が達成度が高い，赤の方が達成度が低い)")
        ]
        return test6, text
    elif pathname == "/Q7":
        text=[
            html.H2("Q7"),
            html.P("並び順：重要度(左側の方が重要　カッコ内の数値が重要度)"),
            html.P("色：達成度(緑の方が達成度が高い，赤の方が達成度が低い)")
        ]
        return test7, text
    else:
        return start, text

if __name__ == "__main__":
    app.run_server(debug=True)