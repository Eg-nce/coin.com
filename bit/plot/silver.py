import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import pandas as pd
from bit.models import values


app = DjangoDash('silver')

qs = values.objects.get( name = "silver")

obj = qs.data.all()
date = [ _.date for _ in obj]
close = [ _.close for _ in obj]
opens = [ _.opens for _ in obj]

silver = {"Date" : date , "Closing_price" : close , "Opens" : opens}
df_silver = pd.DataFrame( data = silver )



app.layout = html.Div(
    html.Div([
        html.H1(children='Silver'  ,style = dict( color='#448D9B')),

      
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
                            {'x': df_silver['Date'].values.tolist() , 'y': df_silver['Closing_price'].values.tolist(), 'type': 'scatter' , "name":"Close"},
                            {'x': df_silver['Date'].values.tolist() , 'y': df_silver['Opens'].values.tolist(), 'type': 'scatter' , "name" :'Open'},
                    
                    ],
                    'layout': {
                        'title': '2016.01.11 to 2021.01.08',
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
        val = int( df_silver.shape[0] / selected)
        figure={
                        'data': [
                                {'x':  df_silver['Date'].iloc[ -val : ].tolist() , 'y':  df_silver['Closing_price'].iloc[  -val :  ].tolist() , 'type': 'scatter' , "name":"Close"},
                                {'x':  df_silver['Date'].iloc[ -val  :  ].tolist() ,'y': df_silver['Opens'].iloc[  -val  : ].tolist(), 'type': 'scatter' , "name" :'Open'},
                        
                        ],

                        'layout': {
                            'title': '2016.01.11 to 2021.01.08',
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


