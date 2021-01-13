"""coin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from django.urls import path , include
from bit import views
from bit.plot import bitcoin , litecoin , xrp , ethereum , chainlink , oil , gold, silver
from django.conf.urls import url, include
urlpatterns = [
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('admin/', admin.site.urls),
    url(r'^bitcoin/$' ,views.bitcoin, name ='Bitcoin'),
    url(r"^main/$" , views.main , name = 'main'),
    url(r"^ethereum/$" , views.ethereum , name = 'Ethereum'),
    url(r"^litecoin/$" , views.litecoin , name = 'Litecoin'),
    url(r"^xrp/$" , views.xrp , name = 'XRP'),
    url(r"^chainlink/$" , views.chainlink , name = 'chainlink'),
    url(r"^silver/$" , views.silver , name = 'silver'),
    url(r"^gold/$" , views.gold , name = 'gold'),
    url(r"^oil/$" , views.oil , name = 'oil'),
  
   
 
    

]
