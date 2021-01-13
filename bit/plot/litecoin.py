import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import pandas as pd
from bit.models import values

app = DjangoDash('litecoin' )


qs = values.objects.get( name = "litecoin")

obj = qs.data.all()
date = [ _.date for _ in obj]
close = [ _.close for _ in obj]
opens = [ _.opens for _ in obj]

litecoin = {"Date" : date , "Closing_price" : close , "Opens" : opens}
df_litecoin = pd.DataFrame( data = litecoin)



app.layout = html.Div(
    html.Div([
        html.H1(children='Litecoin' ,  style = dict( color='#448D9B')),

      
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
                            {'x':  df_litecoin['Date'].values.tolist() , 'y':  df_litecoin['Closing_price'].values.tolist(), 'type': 'scatter' , "name":"Close"},
                            {'x':  df_litecoin['Date'].values.tolist() , 'y': df_litecoin['Opens'].values.tolist(), 'type': 'scatter' , "name" :'Open'},
                    
                    ],
                    'layout': {
                        'title': '2020.01.05 to 2021.01.04',
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
        val = int(df_litecoin.shape[0] / selected)
        figure={
                        'data': [
                                {'x':  df_litecoin['Date'].iloc[ -val : ].tolist() , 'y':  df_litecoin['Closing_price'].iloc[  -val :  ].tolist() , 'type': 'scatter' , "name":"Close"},
                                {'x':  df_litecoin['Date'].iloc[ -val : ].tolist() , 'y':  df_litecoin['Opens'].iloc[  -val  : ].tolist(), 'type': 'scatter' , "name" :'Open'},
                        
                        ],
                        'layout': {
                                'title': '2020.01.05 to 2021.01.04',
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

