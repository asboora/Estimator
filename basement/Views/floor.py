
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ..models import Unitprice, Markup
from ..overview import  floorQuestion
from django.contrib import messages



#page 16
def floor(request):

    if request.method == "POST":
        request.session['Floor_sqft'] = request.POST.get('Floor_sqft')
        request.session['Floor_Tile_sqft'] = request.POST.get('Floor_Tile_sqft')
        request.session['Carpet_sqft'] = request.POST.get('Carpet_sqft')
                
        fm16 = floorQuestion(request.POST)
        if fm16.is_valid():
            messages.success(request,'Tile details added successfully')
    #         fm16.save()

            try:
                request.session['Floor_sqft']         
            except:
                request.session['Floor_sqft'] = "0"

            try:
                request.session['Floor_Tile_sqft']         
            except:
                request.session['Floor_Tile_sqft'] = "0"

            try:
                request.session['Carpet_sqft']         
            except:
                request.session['Carpet_sqft'] = "0"

            FloorAreaKey            = request.session['Floor_sqft']
            FloorTileAreaKey        = request.session['Floor_Tile_sqft']
            CarpetAreaKey           = request.session['Carpet_sqft']

    #Flooring Estimate
    # Floor Area 

            flooringAreaValue = FloorAreaKey
    
            flooringAreaMarkup = Markup.objects.only('Floor_sqft').get(pk=1).Floor_sqft

            flooringAreaPrice = Unitprice.objects.only('Floor_sqft').get(pk=1).Floor_sqft

            flooringAreaEstimate = float(flooringAreaValue)*float(flooringAreaPrice)*(1+float(flooringAreaMarkup)/100)

    # Tile Floor Area 

            floorTileAreaValue = FloorTileAreaKey
    
            floorTileAreaMarkup = Markup.objects.only('Floor_Tile_sqft').get(pk=1).Floor_Tile_sqft

            floorTileAreaPrice = Unitprice.objects.only('Floor_Tile_sqft').get(pk=1).Floor_Tile_sqft

            floorTileAreaEstimate = float(floorTileAreaValue)*float(floorTileAreaPrice)*(1+float(floorTileAreaMarkup)/100)



    # Carpet Area 

            carpetAreaValue = CarpetAreaKey
    
            carpetAreaMarkup = Markup.objects.only('Carpet_sqft').get(pk=1).Carpet_sqft

            carpetAreaPrice = Unitprice.objects.only('Carpet_sqft').get(pk=1).Carpet_sqft

            carpetAreaEstimate = float(carpetAreaValue)*float(carpetAreaPrice)*(1+float(carpetAreaMarkup)/100)

    ### TOTAL FLOORING ESTIMATE 

            totalFloorEstimate = (flooringAreaEstimate+
                                    floorTileAreaEstimate +
                                    carpetAreaEstimate)

            return render(request, 'floor.html',{'form':fm16,'estimate':totalFloorEstimate})
    else:
        fm16 = floorQuestion()
    return render(request, 'floor.html',{'form':fm16})

