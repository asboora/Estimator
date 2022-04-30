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
from django.urls import path
from basement import views as basement
from authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('signup/', views.sign_up, name ='signup'),
    path('', views.user_login, name ='login'),
    path('profile/', basement.addCustomer,),
   path('logout/', views.user_logout, name='logout'),
   path('get/', basement.getsession, ),
    path('addData/', basement.addData ),
    path('1/', basement.addGeneral ),
    path('2/', basement.framing ),
    path('3/', basement.hvac ),
    path('4/', basement.plumbing ),
    # path('5/', basement.plumbing1 ),
    path('6/', basement.plumbing2 ),
    path('7/', basement.electric ),
    path('8/', basement.electric1 ),
    path('9/', basement.insulation ),
    path('10/', basement.drywall ),
    path('11/', basement.trim ),
    path('12/', basement.paint ),
    path('13/', basement.countertop),
    path('14/', basement.tile ),
    # path('15/', basement.tile1 ),
    path('16/', basement.floor ),
    path('17/', basement.carpet ),
    path('18/', basement.bathallow ),
    path('19/', basement.barallow ),
    path('20/', basement.miscallow ),
    path('21/', basement.prefinal ),
    path('22/', basement.final ),
    path('list/', basement.AllCustomer ),
    # path('obtain/', basement.obtain ),
    
]
