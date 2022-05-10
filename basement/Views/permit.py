
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ..models import  BooleansTable, Markup,  Unitprice
from ..overview import  optionDetails
from django.contrib import messages
from ..Calculation import calc1, final





# Overview Tick All Data Required


def addData(request):
    if request.method == "POST":

        request.session['Permit']                   = request.POST.get('Permit')
        request.session['Dumpster']                 = request.POST.get('Dumpster')
        request.session['Year_old']                 = request.POST.get('Year_old')
        request.session['Customer_Ease']            = request.POST.get('Customer_Ease')

        fm0 = optionDetails(request.POST)
        fm0.instance.projectManager_id = request.user.id
        if fm0.is_valid():
     
            messages.success(request,'Overview added successfully')
            # fm0.save()
        
        try:
            request.session['Permit']
            if request.session['Permit'] == 'on':
                a = True
            else:
                a= False
        except: 
            a = False

        try:
            request.session['Dumpster']
            if request.session['Dumpster'] == 'on':
                b = True
            else:
                b= False
        except: 
            b = False

        bools = BooleansTable()

        bools.Permit = a               
        bools.Dumpster = b    

#permit

        permitPrice =0
        if a == True:
            permitPrice = Unitprice.objects.only('Permit').get(pk =1).Permit
        else:
            permitPrice = 0
        
        permitMarkup = Markup.objects.only('Permit').get(pk=1).Permit

        permitEstimate = permitPrice*(1+permitMarkup/100)

        
# TOTAL PERMIT ESTIMATE 

        totalPermitEstimate = permitEstimate

#Dumpster Calculations

        dumpsterPrice =0
        if b == True:
            dumpsterPrice = Unitprice.objects.only('Dumpster').get(pk =1).Dumpster
        else:
            dumpsterPrice = 0
        # return HttpResponse(dumpsterPrice)

        dumpsterMarkup = Markup.objects.only('Dumpster').get(pk=1).Dumpster

        dumpsterEstimate = dumpsterPrice*(1+dumpsterMarkup/100)

# TOTAL DUMPSTER ESTIMATE 

        totalDumpsterEstimate = dumpsterEstimate

        Page1Estimate = totalPermitEstimate + totalDumpsterEstimate


        return render(request, 'addData.html',{'form':fm0,'estimate':Page1Estimate})
    else:
     fm0 = optionDetails()
    return render(request, 'addData.html',{'form':fm0})















    # request.session['Framing']                 = request.POST.get('Framing')
        # request.session['HVAC']                    = request.POST.get('HVAC')
        # request.session['Plumbing_Rough']          = request.POST.get('Plumbing_Rough')
        # request.session['Plumbing_Final']          = request.POST.get('Plumbing_Final')
        # request.session['Electrical_Rough']        = request.POST.get('Electrical_Rough')
        # request.session['Electrical_Final']        = request.POST.get('Electrical_Final')
        # request.session['Insulation']              = request.POST.get('Insulation')
        # request.session['Drywall']                 = request.POST.get('Drywall')
        # request.session['Trim']                    = request.POST.get('Trim')
        # request.session['Painting']                = request.POST.get('Painting')
        # request.session['Cabinetry']               = request.POST.get('Cabinetry')
        # request.session['Countertops']             = request.POST.get('Countertops')
        # request.session['Tile']                    = request.POST.get('Tile')
        # request.session['Flooring']                = request.POST.get('Flooring')
        # request.session['Carpet']                  = request.POST.get('Carpet')
        # request.session['Bathroom_Allowance']      = request.POST.get('Bathroom_Allowance')
        # request.session['Bar_Allowances']          = request.POST.get('Bar_Allowances')
        # request.session['Final_Install_Punch_List']= request.POST.get('Final_Install_Punch_List')
        # request.session['Misc_Materials']          = request.POST.get('Misc_Materials')
        