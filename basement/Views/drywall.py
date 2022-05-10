from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ..models import Unitprice, Markup
from ..overview import  drywallQuestion
from django.contrib import messages



#page 10
def drywall(request):
  
    if request.method == "POST":
        request.session['Drywall_sqft'] = request.POST.get('Drywall_sqft')
        request.session['Wall_Texture'] = request.POST.get('Wall_Texture')
        request.session['Ceiling_Texture'] = request.POST.get('Ceiling_Texture')
        
        fm10 = drywallQuestion(request.POST)
        if fm10.is_valid():
            messages.success(request,'Drywall details added successfully')


            try:
                request.session['Drywall_sqft']         
            except:
                request.session['Drywall_sqft'] = "0"


            drywallAreaKey          = request.session['Drywall_sqft']
    

    #Drywall

            drywallAreaValue = drywallAreaKey

            drywallAreaMarkup = Markup.objects.only('Drywall_sqft').get(pk=1).Drywall_sqft

            drywallAreaPrice = Unitprice.objects.only('Drywall_sqft').get(pk=1).Drywall_sqft

            drywallAreaEstimate = float(drywallAreaValue)*float(drywallAreaPrice)*(1+float(drywallAreaMarkup)/100)

    ### TOTAL DRYWALL ESTIMATE 

            totalDrywallEstimate = drywallAreaEstimate

    #         fm10.save()
            return render(request, 'drywall.html',{'form':fm10,'estimate':totalDrywallEstimate})
    else:
        fm10 = drywallQuestion()
    return render(request, 'drywall.html',{'form':fm10})

