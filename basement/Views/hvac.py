

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ..models import Markup, Unitprice
from ..overview import  hvacQuestion
from django.contrib import messages



#page 3
def hvac(request):

        if request.method == "POST":
            request.session['HVAC_RSE_Vents'] = request.POST.get('HVAC_RSE_Vents')
            
            fm3 = hvacQuestion(request.POST)
            if fm3.is_valid():
                messages.success(request,'hvac Details added successfully')
        #         fm3.save()
            #HVAC

            try:
                request.session['HVAC_RSE_Vents']         
            except:
                request.session['HVAC_RSE_Vents'] = "0"

            HVACVentsKey            = request.session['HVAC_RSE_Vents']

            hvacValue = HVACVentsKey

            hvacMarkup = Markup.objects.only('HVAC_RSE_Vents').get(pk=1).HVAC_RSE_Vents

            hvacUnitPrice = Unitprice.objects.only('HVAC_RSE_Vents').get(pk=1).HVAC_RSE_Vents

            hvacEstimate = float(hvacValue)*float(hvacUnitPrice)*(1+float(hvacMarkup)/100)


    # TOTAL HVAC ESTIMATE 

            totalHvacEstimate = hvacEstimate
        

        
            return render(request, 'hvac.html',{'form':fm3,'estimate':totalHvacEstimate})
        else:
                fm3 = hvacQuestion()
        return render(request, 'hvac.html',{'form':fm3})
    