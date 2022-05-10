from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ..models import Unitprice, Markup
from ..overview import  paintQuestion
from django.contrib import messages



#page 12
def paint(request):

    if request.method == "POST":
        request.session['Paint_sqft'] = request.POST.get('Paint_sqft')
        request.session['add_colors'] = request.POST.get('add_colors')
    
        
        fm12 = paintQuestion(request.POST)
        if fm12.is_valid():
            messages.success(request,'Paint details added successfully')
    #         fm12.save()

            try:
                request.session['Paint_sqft']         
            except:
                request.session['Paint_sqft'] = "0"

            try:
                request.session['add_colors']         
            except:
                request.session['add_colors'] = "0"

            PaintAreaKey            = request.session['Paint_sqft']
            NumberOfColorsKey       = request.session['add_colors']

    #Paint
        # Paint Area 

            paintAreaValue = PaintAreaKey
    
            paintAreaMarkup = Markup.objects.only('Paint_sqft').get(pk=1).Paint_sqft

            paintAreaPrice = Unitprice.objects.only('Paint_sqft').get(pk=1).Paint_sqft

            paintAreaEstimate = float(paintAreaValue)*float(paintAreaPrice)*(1+float(paintAreaMarkup)/100)
        
        
        # Paint Addition 

            noOfPaintValue = NumberOfColorsKey
    
            noOfPaintMarkup = Markup.objects.only('add_colors').get(pk=1).add_colors

            noOfPaintPrice = Unitprice.objects.only('add_colors').get(pk=1).add_colors

            noOfPaintEstimate = float(noOfPaintValue)*float(noOfPaintPrice)*(1+float(noOfPaintMarkup)/100)
        
        
    ### TOTAL PAINT ESTIMATE 

            totalPaintEstimate = paintAreaEstimate + noOfPaintEstimate

            return render(request, 'paint.html',{'form':fm12,'estimate':totalPaintEstimate})
    else:
        fm12 = paintQuestion()
    return render(request, 'paint.html',{'form':fm12})
