import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import pandas as pd
from bit.models import values
import plotly.express as px

app = DjangoDash('xrp')

qs = values.objects.get( name = "XRP")

obj = qs.data.all()
date = [ _.date for _ in obj]
close = [ _.close for _ in obj]
opens = [ _.opens for _ in obj]

xrp = {"Date" : date , "Closing_price" : close , "Opens" : opens}
df_xrp = pd.DataFrame( data = xrp)


app.layout = html.Div(
    html.Div([
        html.H1(children='XRP' , style = dict( color='#448D9B')),

      
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
        ),
       
])

)

@app.callback(  
    Output('graph', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected):
   
 if selected == 1:
        figure={
                    'data': [
                            {'x': df_xrp['Date'].values.tolist() , 'y': df_xrp['Closing_price'].values.tolist(), 'type': 'scatter' , "name":"Close"  },
                            {'x': df_xrp['Date'].values.tolist() , 'y': df_xrp['Opens'].values.tolist(), 'type': 'scatter' , "name" :'Open'},
                    
                    ],
                    'layout': {
                            'title': '2020.01.06 to 2021.01.05',
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
        val = int(df_xrp.shape[0] / selected)
        figure={
                        'data': [
                                {'x': df_xrp['Date'].iloc[ -val : ].tolist() , 'y': df_xrp['Closing_price'].iloc[  -val :  ].tolist() , 'type': 'scatter' , "name":"Close"},
                                {'x': df_xrp['Date'].iloc[ -val  :  ].tolist() , 'y': df_xrp['Opens'].iloc[  -val  : ].tolist(), 'type': 'scatter' , "name" :'Open'},
                        
                        ],
                           
                        'layout': {
                                'title': '2020.01.06 to 2021.01.05',
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





