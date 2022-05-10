
import imp
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ..models import Unitprice, Markup
from ..overview import  tileQuestion
from django.contrib import messages



#page 14
def tile(request):
   
    if request.method == "POST":
        request.session['Tile_Backsplash_sqft']     = request.POST.get('Tile_Backsplash_sqft')
        request.session['BathType']                 = request.POST.get('BathType')
        request.session['Shower_Pan_sqft']          = request.POST.get('Shower_Pan_sqft')
        request.session['Wall_Tile_sqft']           = request.POST.get('Wall_Tile_sqft')
        request.session['Niches']                   = request.POST.get('Niches')

    
        
        fm14 = tileQuestion(request.POST)
        if fm14.is_valid():
            messages.success(request,'Paint details added successfully')
    #         fm14.save()
            try:
                request.session['Tile_Backsplash_sqft']         
            except:
                request.session['Tile_Backsplash_sqft'] = "0"

            try:
                request.session['BathType']         
            except:
                request.session['BathType'] = "1"
     
            try:
                request.session['Shower_Pan_sqft']         
            except:
                request.session['Shower_Pan_sqft'] = "0"

            try:
                request.session['Wall_Tile_sqft']         
            except:
                request.session['Wall_Tile_sqft'] = "0"

            try:
                request.session['Niches']         
            except:
                request.session['Niches'] = "0"


            BacksplashAreaKey       = request.session['Tile_Backsplash_sqft']
            BathTypeKey             = request.session['BathType']
            ShowerPanAreaKey        = request.session['Shower_Pan_sqft']
            WallTileAreaKey         = request.session['Wall_Tile_sqft']
            NichesKey               = request.session['Niches']

    ##TILES
    # BackSplash Tile Area 

            backsplashAreaValue = BacksplashAreaKey
    
            backsplashAreaMarkup = Markup.objects.only('Tile_Backsplash_sqft').get(pk=1).Tile_Backsplash_sqft

            backsplashAreaPrice = Unitprice.objects.only('Tile_Backsplash_sqft').get(pk=1).Tile_Backsplash_sqft

            backsplashAreaEstimate = float(backsplashAreaValue)*float(backsplashAreaPrice)*(1+float(backsplashAreaMarkup)/100)


    #Shower Pan Area

            showerPanAreaValue = ShowerPanAreaKey
    
            showerPanAreaMarkup = Markup.objects.only('Shower_Pan_sqft').get(pk=1).Shower_Pan_sqft

            showerPanAreaPrice = Unitprice.objects.only('Shower_Pan_sqft').get(pk=1).Shower_Pan_sqft

            showerPanAreaEstimate = float(showerPanAreaValue)*float(showerPanAreaPrice)*(1+float(showerPanAreaMarkup)/100)

    #Wall Tile Area

            wallTileAreaValue = WallTileAreaKey
    
            wallTileAreaMarkup = Markup.objects.only('Wall_Tile_sqft').get(pk=1).Wall_Tile_sqft

            wallTileAreaPrice = Unitprice.objects.only('Wall_Tile_sqft').get(pk=1).Wall_Tile_sqft

            wallTileAreaEstimate = float(wallTileAreaValue)*float(wallTileAreaPrice)*(1+float(wallTileAreaMarkup)/100)

    #Niches

            nichesValue = NichesKey
    
            nichesMarkup = Markup.objects.only('Niches').get(pk=1).Niches

            nichesPrice = Unitprice.objects.only('Niches').get(pk=1).Niches

            nichesEstimate = float(nichesValue)*float(nichesPrice)*(1+float(nichesMarkup)/100)

    #Fiberglass Tub Cost

            fiberglassTubPrice = Unitprice.objects.only('FiberglassTub').get(pk=1).FiberglassTub

            fiberglassTubMarkup = Markup.objects.only('FiberglassTub').get(pk=1).FiberglassTub

            fiberglassTubEstimate = float(fiberglassTubPrice)*(1+float(fiberglassTubMarkup)/100)
    #Tile Estimate bath Type Condition

            if BathTypeKey == "1":
                showerPanAreaEstimate = 0
                wallTileAreaEstimate = 0
                nichesEstimate = 0
                fiberglassTubEstimate = 0

            elif BathTypeKey == "2":
                showerPanAreaEstimate = 0
                fiberglassTubEstimate = fiberglassTubEstimate
            else:
                fiberglassTubEstimate = 0
                showerPanAreaEstimate = showerPanAreaEstimate


    ### TOTAL TILE ESTIMATE 

            totalTileEstimate = (backsplashAreaEstimate + 
                                showerPanAreaEstimate +
                                wallTileAreaEstimate +
                                nichesEstimate +
                                fiberglassTubEstimate) 



            return render(request, 'tile.html',{'form':fm14,'estimate':totalTileEstimate})
    else:
        fm14 = tileQuestion()
    return render(request, 'tile.html',{'form':fm14})


