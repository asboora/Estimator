from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ..models import Unitprice, Markup
from ..overview import  trimQuestion
from django.contrib import messages


#page 11
def trim(request):
   
    if request.method == "POST":

        request.session['No_of_doors'] = request.POST.get('No_of_doors')
        request.session['LF_of_Cabinetry'] = request.POST.get('LF_of_Cabinetry')
        request.session['LF_of_baseboard'] = request.POST.get('LF_of_baseboard')
        request.session['Casing_LF'] = request.POST.get('Casing_LF')
        request.session['Stairs_skirting'] = request.POST.get('Stairs_skirting')
        request.session['Solid_core_doors'] = request.POST.get('Solid_core_doors')
        

        fm11 = trimQuestion(request.POST)
        if fm11.is_valid():
            messages.success(request,'Trim details added successfully')
    #         fm11.save()
            try:
                request.session['No_of_doors']         
            except:
                request.session['No_of_doors'] = "0"

            try:
                request.session['LF_of_Cabinetry']         
            except:
                request.session['LF_of_Cabinetry'] = "0"

            try:
                request.session['LF_of_baseboard']         
            except:
                request.session['LF_of_baseboard'] = "0"

            try:
                request.session['Casing_LF']         
            except:
                request.session['Casing_LF'] = "0"

            try:
                request.session['Solid_core_doors']
                if request.session['Solid_core_doors'] == 'on':
                    gg = True
                else:
                    gg= False
            except: 
                gg = False


            try:
                request.session['Stairs_skirting']
                if request.session['Stairs_skirting'] == 'on':
                    StairSkirtKey = True
                else:
                    StairSkirtKey= False
            except: 
                StairSkirtKey = False


            DoorsKey                = request.session['No_of_doors']
            CabinetryAreaKey        = request.session['LF_of_Cabinetry']
            BaseboardAreaKey        = request.session['LF_of_baseboard']
            CasingLengthKey         = request.session['Casing_LF']
        
            #Trim 

        #No of Doors 

            noOfDoorsValue = DoorsKey
            
            noOfDoorsMarkup = Markup.objects.only('No_of_doors').get(pk=1).No_of_doors

            noOfDoorsPrice = Unitprice.objects.only('No_of_doors').get(pk=1).No_of_doors

            noOfDoorsEstimate = float(noOfDoorsValue)*noOfDoorsPrice*(1+float(noOfDoorsMarkup)/100)

        #LF of Cabinetry 

            lfOfCabinetryValue = CabinetryAreaKey
            
            lfOfCabinetryMarkup = Markup.objects.only('LF_of_Cabinetry').get(pk=1).LF_of_Cabinetry

            lfOfCabinetryPrice = Unitprice.objects.only('LF_of_Cabinetry').get(pk=1).LF_of_Cabinetry

            lfOfCabinetryEstimate = float(lfOfCabinetryValue)*float(lfOfCabinetryPrice)*(1+float(lfOfCabinetryMarkup)/100)

            
        #LF of Baseboard 

            lfOfBaseboardValue = BaseboardAreaKey
            
            lfOfBaseboardMarkup = Markup.objects.only('LF_of_baseboard').get(pk=1).LF_of_baseboard

            lfOfBaseboardPrice = Unitprice.objects.only('LF_of_baseboard').get(pk=1).LF_of_baseboard

            lfOfBaseboardEstimate = float(lfOfBaseboardValue)*float(lfOfBaseboardPrice)*(1+float(lfOfBaseboardMarkup)/100)

        
        #LF of Casing 

            lfOfCasingValue = CasingLengthKey
    
            lfOfCasingMarkup = Markup.objects.only('Casing_LF').get(pk=1).Casing_LF

            lfOfCasingPrice = Unitprice.objects.only('Casing_LF').get(pk=1).Casing_LF

            lfOfCasingEstimate = float(lfOfCasingValue)*float(lfOfCasingPrice)*(1+float(lfOfCasingMarkup)/100)

        #Solid Core Doors

            solidCoreDoorsPrice = 0
            if gg == True:
                solidCoreDoorsPrice = Unitprice.objects.only('Solid_core_doors').get(pk =1).Solid_core_doors
            else:
                solidCoreDoorsPrice = 0
            

            solidCoreDoorsMarkup = Markup.objects.only('Solid_core_doors').get(pk=1).Solid_core_doors

            solidCoreDoorsEstimate = float(solidCoreDoorsPrice)*(1+float(solidCoreDoorsMarkup)/100)       



        #Stairs Skirting

            stairSkirtingPrice = 0
            if StairSkirtKey == True:
                stairSkirtingPrice = Unitprice.objects.only('Stairs_skirting').get(pk =1).Stairs_skirting
            else:
                stairSkirtingPrice = 0
            

            stairSkirtingMarkup = Markup.objects.only('Stairs_skirting').get(pk=1).Stairs_skirting

            stairSkirtingEstimate = float(stairSkirtingPrice)*(1+float(stairSkirtingMarkup)/100)       

    # TOTAL TRIM ESTIMATE 

            totalTrimEstimate = (noOfDoorsEstimate +
            lfOfCabinetryEstimate +
            lfOfBaseboardEstimate +
            lfOfCasingEstimate +
            solidCoreDoorsEstimate + 
            stairSkirtingEstimate )





            return render(request, 'trim.html',{'form':fm11,'estimate':totalTrimEstimate})
    else:
        fm11 = trimQuestion()
    return render(request, 'trim.html',{'form':fm11})
  