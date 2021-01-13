import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import pandas as pd
from bit.models import values

app = DjangoDash('Ethereum' ,  style = dict( color='#448D9B'))


qs = values.objects.get( name = "ethereum")

obj = qs.data.all()
date = [ _.date for _ in obj]
close = [ _.close for _ in obj]
opens = [ _.opens for _ in obj]

ethereum = {"Date" : date , "Closing_price" : close , "Opens" : opens}
df_ethereum = pd.DataFrame( data = ethereum)


app.layout = html.Div(
    html.Div([
        html.H1(children='Ethereum' ,  style = dict( color='#448D9B')),

      
        dcc.Graph(
            id='graph',
            
        ),
       
        dcc.Slider(
            id='year-slider',
            min= 1,
            max= 20 ,
            value=1,
            marks=[ x for x in range(21)],
            step=None
        )

       
])

)

@app.callback(  
    Output('graph', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected):
   
 if selected == 1:
        figure={
                    'data': [
                            {'x':  df_ethereum['Date'].values.tolist() , 'y':  df_ethereum['Closing_price'].values.tolist(), 'type': 'scatter' , "name":"Close"},
                            {'x':  df_ethereum['Date'].values.tolist() , 'y':  df_ethereum['Opens'].values.tolist(), 'type': 'scatter' , "name" :'Open'},
                    
                    ],
                    'layout': {
                            'title': '2015.08.09 to 2021.01.04',
                            'yaxis' : dict(
                                title='Dolar',
                                color='#7f7f7f'
                            ),
                            'xaxis' : dict(
                                title='Time',
                                color='#7f7f7f'
                            ),

                            }
                
                }    
        return  figure 
 else: 
        val = int(df_ethereum.shape[0] / selected)
        figure={
                        'data': [
                                {'x':  df_ethereum['Date'].iloc[ -val : ].tolist() , 'y':  df_ethereum['Closing_price'].iloc[  -val:  ].tolist() , 'type': 'scatter' , "name":"Close"},
                                {'x':  df_ethereum['Date'].iloc[ -val : ].tolist() , 'y':  df_ethereum['Opens'].iloc[  -val : ].tolist(), 'type': 'scatter' , "name" :'Open'},
                        
                        ],
                        'layout': {
                                'title': '2015.08.09 to 2021.01.04',
                                'yaxis' : dict(
                                    title='Dolar',
                                    color='#7f7f7f'
                                ),
                                'xaxis' : dict(
                                    title='Time',
                                    color='#7f7f7f'
                                ),

                    }
                    
                    }   
        return figure     


