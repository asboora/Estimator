"""Estimator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import imp
from django.contrib import admin
from django.urls import path, include
from basement.Views import addCustomer,permit,framing, hvac, plumbing, electric, insulation , drywall, trim, paint,countertop,tile, floor

from basement import views as basement
from authentication import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
       
    path('admin/', admin.site.urls),
    # path('api/user/', include('account.urls')),
    path('signup/', views.sign_up, name ='signup'),
    path('', views.user_login, name ='login'),
    path('profile/', addCustomer.addCustomer, name='profile'),
   path('logout/', views.user_logout, name='logout'),
   path('get/', basement.getsession, ),
     path('addData/', permit.addData ,name= 'Customer'),
   
    path('2/', framing.framing,name= 'framing' ),
    path('3/', hvac.hvac,name= 'hvac'),
    path('4/', plumbing.plumbing,name= 'plumbing' ),
    # path('5/', basement.plumbing1 ),
    # path('6/', basement.plumbing2,name= 'plumbing2' ),
    path('7/', electric.electric,name= 'electric' ),
    # path('8/', basement.electric1,name= 'electric1' ),
    path('9/', insulation.insulation,name= 'insulation' ),
    path('10/', drywall.drywall,name= 'drywall' ),
    path('11/', trim.trim,name= 'trim' ),
    path('12/', paint.paint,name= 'paint' ),
    path('13/', countertop.countertop,name= 'countertop'),
    path('14/', tile.tile,name= 'tile' ),
    # path('15/', basement.tile1 ),
    path('16/', floor.floor,name= 'floor' ),
    # path('17/', basement.carpet,name= 'carpet' ),
    path('18/', basement.bathallow,name= 'bathallow' ),
    path('19/', basement.barallow,name= 'barallow' ),
    path('20/', basement.miscallow,name= 'miscallow' ),
    path('21/', basement.prefinal,name= 'prefinal' ),
    path('22/', basement.final,name= 'final' ),
    # path('obtain/', basement.obtain ),
    
]
urlpatterns += staticfiles_urlpatterns()