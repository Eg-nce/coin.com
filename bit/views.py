from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
# Create your views here.
from django.shortcuts import render
import pandas as pd 
from  .models import data_loader,values
import pandas as pd




def main(request):
   qs_list = ["bitcoin" ,"litecoin"  , "ethereum" , "XRP" , "Chainlink" ,  "gold" , "silver" , "Oil"]
   labels = ["open_btc" , "close_btc" , "change_btc" , "open_lite" , "close_lite" , "change_lite" ,
    "open_et" , "close_et" , "change_et" , "open_xrp" ,"close_xrp" , "change_xrp" , "open_chain" , "close_chain" , "change_chain" , "open_gold" , 
    "close_gold","change_gold" ,"open_silver" , "close_silver"  , "change_silver" , "open_oil" , "close_oil" , "change_oil"]
   context = dict()
   step = 0
   for val in qs_list:

        qs = values.objects.get( name = val)
        obj = qs.data.all()
        close = [ _.close for _ in obj][-1]
        opens = [ _.opens for _ in obj][-1]
        derivative =  ((close*100) / opens) - 100
        derivative =  round(derivative ,3)
        if close > 1000 and opens > 1000:
            close = '{:,.2f}'.format(close)
            opens = '{:,.2f}'.format(opens)
        else:
            close = round(close, 3)
            opens = round(opens ,3) 
        
        context[labels[step]] = opens
        context[labels[step+1]] = close
        context[labels[step+2]] = derivative
        step += 3
    
   return render(request , "main.html" , context)

def bitcoin(request):
    qs = values.objects.get( name = "bitcoin")
    obj = qs.data.all()
    close = [ _.close for _ in obj][-1]
    opens = [ _.opens for _ in obj][-1]
    derivative =  ((close*100) / opens) - 100
    derivative =  round(derivative ,3)
    if close > 1000 and opens > 1000:
        close = '{:,.2f}'.format(close)
        opens = '{:,.2f}'.format(opens)
    else:
        close = round(close, 3)
        opens = round(opens ,3)  
    context =   {"opens": opens , "close" : close ,  "derivative" : derivative}
    return render( request , "plots/bitcoin.html" ,  context)    


def litecoin(request):
    qs = values.objects.get( name = "litecoin")
    obj = qs.data.all()
    close = [ _.close for _ in obj][-1]
    opens = [ _.opens for _ in obj][-1]
    derivative =  ((close*100) / opens) - 100
    derivative =  round(derivative ,3)
    if close > 1000 and opens > 1000:
        close = '{:,.2f}'.format(close)
        opens = '{:,.2f}'.format(opens)
    else:
        close = round(close, 3)
        opens = round(opens ,3)   
    context = {"opens": opens , "close" : close ,  "derivative" : derivative}
    
    return render(request , "plots/litecoin.html" ,   context )


def ethereum(request):
    qs = values.objects.get( name = "ethereum")
    obj = qs.data.all()
    close = [ _.close for _ in obj][-1]
    opens = [ _.opens for _ in obj][-1]
    derivative =  ((close*100) / opens) - 100
    derivative =  round(derivative ,3)
    if close > 1000 and opens > 1000:
        close = '{:,.2f}'.format(close)
        opens = '{:,.2f}'.format(opens)
    else:
        close = round(close, 3)
        opens = round(opens ,3) 

    context =  {"opens": opens , "close" : close ,  "derivative" : derivative}
    return render(request , "plots/ethereum.html" , context)

def xrp(request):
    qs = values.objects.get( name = "XRP")
    obj = qs.data.all()
    close = [ _.close for _ in obj][-1]
    opens = [ _.opens for _ in obj][-1]
    derivative =  ((close*100) / opens) - 100
    derivative =  round(derivative ,3)
    if close > 1000 and opens > 1000:
        close = '{:,.2f}'.format(close)
        opens = '{:,.2f}'.format(opens)
    else:
        close = round(close, 3)
        opens = round(opens ,3) 
     
    context = {"opens": opens , "close" : close ,  "derivative" : derivative} 
    return render(request , "plots/XRP.html" ,    context  )    

def chainlink(request ):
    qs = values.objects.get( name = "Chainlink")
    obj = qs.data.all()
    close = [ _.close for _ in obj][-1]
    opens = [ _.opens for _ in obj][-1]
    derivative =  ((close*100) / opens) - 100
    derivative =  round(derivative ,3)

    if close > 1000 and opens > 1000:
        close = '{:,.2f}'.format(close)
        opens = '{:,.2f}'.format(opens)
    else:
        close = round(close, 3)
        opens = round(opens ,3) 
    
    context = {"opens": opens , "close" : close , "derivative" : derivative}
    return render( request , "plots/chainlink.html", context )    

def gold(request ):
    qs = values.objects.get( name = "gold")
    obj = qs.data.all()
    close = [ _.close for _ in obj][-1]
    opens = [ _.opens for _ in obj][-1]
    derivative =  ((close*100) / opens) - 100
    derivative =  round(derivative ,3)

    if close > 1000 and opens > 1000:
        close = '{:,.2f}'.format(close)
        opens = '{:,.2f}'.format(opens)
    else:
        close = round(close, 3)
        opens = round(opens ,3) 
    
    context =  {"opens": opens , "close" : close , "derivative" : derivative}
    return render( request , "plots/gold.html",     context )    



def silver(request ):
    qs = values.objects.get( name = "silver")
    obj = qs.data.all()
    close = [ _.close for _ in obj][-1]
    opens = [ _.opens for _ in obj][-1]
    derivative =  ((close*100) / opens) - 100
    derivative =  round(derivative ,3)

    if close > 1000 and opens > 1000:
        close = '{:,.2f}'.format(close)
        opens = '{:,.2f}'.format(opens)
    else:
        close = round(close, 3)
        opens = round(opens ,3) 
    
    context = {"opens": opens , "close" : close , "derivative" : derivative}
    return render( request , "plots/silver.html",  context )    




def oil(request ):
    qs = values.objects.get( name = "Oil")
    obj = qs.data.all()
    close = [ _.close for _ in obj][-1]
    opens = [ _.opens for _ in obj][-1]
    derivative =  ((close*100) / opens) - 100
    derivative =  round(derivative ,3)

    if close > 1000 and opens > 1000:
        close = '{:,.2f}'.format(close)
        opens = '{:,.2f}'.format(opens)
    else:
        close = round(close, 3)
        opens = round(opens ,3) 
    
    context = {"opens": opens , "close" : close , "derivative" : derivative}
    return render( request , "plots/oil.html",  context)            