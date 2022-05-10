
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ..models import Unitprice, Markup
from ..overview import  countertopQuestion
from django.contrib import messages

#page 13
def countertop(request):

    if request.method == "POST":
        request.session['Countertop_type'] = request.POST.get('Countertop_type')
        request.session['Countertop_sqft'] = request.POST.get('Countertop_sqft')
    
        
        fm13 = countertopQuestion(request.POST)
        if fm13.is_valid():
            messages.success(request,'Paint details added successfully')

            try:
                request.session['Countertop_type']         
            except:
                request.session['Countertop_type'] = "1"

            try:
                request.session['Countertop_sqft']         
            except:
                request.session['Countertop_sqft'] = "0"



    #Countertop Estimate
            CountertopTypeKey       = request.session['Countertop_type']
            CountertopAreaKey       = request.session['Countertop_sqft']


            countertopValue = CountertopAreaKey 

            if CountertopTypeKey == "1":
                countertopPrice = Unitprice.objects.only('Countertop_type_Granite').get(pk =1).Countertop_type_Granite
            elif CountertopTypeKey == "2":
                countertopPrice = Unitprice.objects.only('Countertop_type_Quartz').get(pk =1).Countertop_type_Quartz
            else:
                countertopPrice = Unitprice.objects.only('Countertop_type_Butcherblock').get(pk =1).Countertop_type_Butcherblock

            countertopMarkup = Markup.objects.only('Countertop_sqft').get(pk=1).Countertop_sqft
            
            countertopEstimate = float(countertopValue)*float(countertopPrice)*(1+float(countertopMarkup)/100)    


    ### TOTAL COUNTERTOP ESTIMATE 

            totalCountertopEstimate = countertopEstimate

        #   fm13.save()


            return render(request, 'countertop.html',{'form':fm13,'estimate':totalCountertopEstimate})
    else:
        fm13 = countertopQuestion()
    return render(request, 'countertop.html',{'form':fm13})

