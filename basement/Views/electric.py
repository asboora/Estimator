

import imp
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ..overview import   electricQuestion
from ..models import Unitprice , Markup
from django.contrib import messages




#page 7
def electric(request):

    if request.method == "POST":
        request.session['Electrical_sqft'] = request.POST.get('Electrical_sqft')
        request.session['Panel_Location'] = request.POST.get('Panel_Location')
        request.session['Dimmer_Switches']       = request.POST.get('Dimmer_Switches')
        request.session['Undercabinet_Lighting'] = request.POST.get('Undercabinet_Lighting')
        request.session['SubPanel']               = request.POST.get('SubPanel')
        request.session['Fan_Install']           = request.POST.get('Fan_Install')

        fm7 = electricQuestion(request.POST)
        if fm7.is_valid():
            messages.success(request,'Electrical details added successfully')
    #         fm7.save()
            try:
                request.session['Undercabinet_Lighting']
                if request.session['Undercabinet_Lighting'] == 'on':
                    ee = True
                else:
                    ee= False
            except: 
                ee = False

            
            try:
                request.session['SubPanel']
                if request.session['SubPanel'] == 'on':
                    ff = True
                else:
                    ff= False
            except: 
                ff = False

            try:
                request.session['Electrical_sqft']         
            except:
                request.session['Electrical_sqft'] = "0"
            
            try:
                request.session['Panel_Location']         
            except:
                request.session['Panel_Location'] = "1"

            try:
                request.session['Dimmer_Switches']         
            except:
                request.session['Dimmer_Switches'] = "0"

            
            try:
                request.session['Fan_Install']         
            except:
                request.session['Fan_Install'] = "0"



        ElectricalAreaKey       = request.session['Electrical_sqft']
        PanelLocationKey        = request.session['Panel_Location']
        DimmerSwitchesKey       = request.session['Dimmer_Switches']
        FanInstallKey           = request.session['Fan_Install']

#Electrical 

#Electrical sq ft
        electricalSqftValue = ElectricalAreaKey

        panelLocationPrice = Unitprice.objects.only('Panel_Location').get(pk =1).Panel_Location
       
        panelLocationMarkup = Markup.objects.only('Panel_Location').get(pk =1).Panel_Location

        electricalSqftPrice = Unitprice.objects.only('Electrical_sqft').get(pk =1).Electrical_sqft
    
        electricalSqftMarkup = Markup.objects.only('Electrical_sqft').get(pk=1).Electrical_sqft

        electricalSqftEstimate = float(electricalSqftValue)*float(electricalSqftPrice)*float((1+electricalSqftMarkup/100))
        

        if PanelLocationKey == "2":

            electricalSqftEstimate = electricalSqftEstimate + panelLocationPrice*float((1+panelLocationMarkup/100))
        else:
            electricalSqftEstimate = electricalSqftEstimate
        


#DimmerSwitch 
        dimmerSwitchValue = DimmerSwitchesKey

        dimmerSwitchMarkup = Markup.objects.only('Dimmer_Switches').get(pk=1).Dimmer_Switches

        dimmerSwitchPrice = Unitprice.objects.only('Dimmer_Switches').get(pk=1).Dimmer_Switches

        dimmerSwitchEstimate = float(dimmerSwitchValue)*float(dimmerSwitchPrice)*(1+float(dimmerSwitchMarkup)/100)



#UnderCabinetLighting

        underCabinetLightingPrice = 0
        if ee == True:
            underCabinetLightingPrice = Unitprice.objects.only('Undercabinet_Lighting').get(pk =1).Undercabinet_Lighting
        else:
            underCabinetLightingPrice = 0
        

        underCabinetLightingMarkup = Markup.objects.only('Undercabinet_Lighting').get(pk=1).Undercabinet_Lighting

        underCabinetLightingEstimate = float(underCabinetLightingPrice)*(1+float(underCabinetLightingMarkup)/100)
        
        
#subpanel

        subpanelPrice = 0
        if ff == True:
            subpanelPrice = Unitprice.objects.only('SubPanel').get(pk =1).SubPanel
        else:
            subpanelPrice = 0
        

        subpanelMarkup = Markup.objects.only('SubPanel').get(pk=1).SubPanel

        subpanelEstimate = subpanelPrice*(1+subpanelMarkup/100)
        
#Fans 
        fanInstallValue = FanInstallKey

        fanInstallMarkup = Markup.objects.only('Fan_Install').get(pk=1).Fan_Install

        fanInstallPrice = Unitprice.objects.only('Fan_Install').get(pk=1).Fan_Install

        fanInstallEstimate = float(fanInstallValue)*float(fanInstallPrice)*(1+float(fanInstallMarkup)/100)
       
### TOTAL ELECTRICAL ESTIMATE 

        totalElectricalEstimate = (electricalSqftEstimate+
                                    dimmerSwitchEstimate +
                                    underCabinetLightingEstimate +
                                    subpanelEstimate + 
                                    fanInstallEstimate)        




        return render(request, 'electric.html',{'form':fm7,'estimate':totalElectricalEstimate})
    else:
        fm7 = electricQuestion()
    return render(request, 'electric.html',{'form':fm7})
   