import sys
sys.path.append('..')
import dash_gif_component as gif
import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)


app.layout = html.Div([
    dcc.Tabs(
        id='tabs',
        value='main',
        children=[
            dcc.Tab(
                label='main',
                value='main',
                children=[html.H1('main')],
            ),
            dcc.Tab(
                label='gif',
                value='gif',
                children=[
                    gif.GifPlayer(
                        gif='assets/giphy.gif',
                        still='assets/giphy.png',
                    )]
            )
        ])
])


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port='3002')
