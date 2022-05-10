
import imp
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ..overview import insulationQuestion
from ..models import Unitprice, Markup
from django.contrib import messages




#page 9
def insulation(request):
    
    if request.method == "POST":
        request.session['Insulation_sqft'] = request.POST.get('Insulation_sqft')

        try:
            request.session['Insulation_sqft']         
        except:
            request.session['Insulation_sqft'] = "0"


        InsulationAreaKey       = request.session['Insulation_sqft']

        fm9 = insulationQuestion(request.POST)
        if fm9.is_valid():
            messages.success(request,'Insulation details added successfully')
    #         fm9.save()

        #Insulation
 
        insulationAreaValue = InsulationAreaKey

        insulationAreaMarkup = Markup.objects.only('Insulation_sqft').get(pk=1).Insulation_sqft

        insulationAreaPrice = Unitprice.objects.only('Insulation_sqft').get(pk=1).Insulation_sqft

        insulationAreaEstimate = float(insulationAreaValue)*float(insulationAreaPrice)*(1+float(insulationAreaMarkup)/100)



### TOTAL INSULATION ESTIMATE 

        totalInsulationEstimate = insulationAreaEstimate


    
        
        return render(request, 'insulation.html',{'form':fm9,'estimate':totalInsulationEstimate}),totalInsulationEstimate
    else:
        fm9 = insulationQuestion()
    return render(request, 'insulation.html',{'form':fm9})
    