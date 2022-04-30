

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Customer
from .overview import barallowQuestion, bathallowQuestion, carpetQuestion, countertopQuestion, customerDetails, drywallQuestion, electricQuestion, electricQuestion1, finalQuestion, floorQuestion, framingQuestion, generalQuestion, insulationQuestion, miscallowQuestion, optionDetails, paintQuestion, plumbingQuestion , hvacQuestion,  plumbingQuestion2, tileQuestion, trimQuestion
from django.contrib import messages

#Customer Details form
def addCustomer(request):

    if request.method == "POST":
        request.session['customerName'] = request.POST.get('customerName')
        request.session['customerAddress'] = request.POST.get('customerAddress')
        request.session['customerContact'] = request.POST.get('customerContact')
        request.session['customerEmail'] = request.POST.get('customerEmail')

        fm = customerDetails(request.POST)
        fm.instance.projectManager_id = request.user.id
        if fm.is_valid():   
            messages.success(request,'customer added successfully')
    #         fm.save()
            return HttpResponseRedirect('/addData/')

    else:
        fm = customerDetails()
    return render(request, 'addCustomer.html',{'form':fm})



# Overview Tick All Data Required


def addData(request):
    if request.method == "POST":
        request.session['Permit']                  = request.POST.get('Permit')
        request.session['Dumpster']                = request.POST.get('Dumpster')
        request.session['Framing']                 = request.POST.get('Framing')
        request.session['HVAC']                    = request.POST.get('HVAC')
        request.session['Plumbing_Rough']          = request.POST.get('Plumbing_Rough')
        request.session['Plumbing_Final']          = request.POST.get('Plumbing_Final')
        request.session['Electrical_Rough']        = request.POST.get('Electrical_Rough')
        request.session['Electrical_Final']        = request.POST.get('Electrical_Final')
        request.session['Insulation']              = request.POST.get('Insulation')
        request.session['Drywall']                 = request.POST.get('Drywall')
        request.session['Trim']                    = request.POST.get('Trim')
        request.session['Painting']                = request.POST.get('Painting')
        request.session['Cabinetry']               = request.POST.get('Cabinetry')
        request.session['Countertops']             = request.POST.get('Countertops')
        request.session['Tile']                    = request.POST.get('Tile')
        request.session['Flooring']                = request.POST.get('Flooring')
        request.session['Carpet']                  = request.POST.get('Carpet')
        request.session['Bathroom_Allowance']      = request.POST.get('Bathroom_Allowance')
        request.session['Bar_Allowances']          = request.POST.get('Bar_Allowances')
        request.session['Final_Install_Punch_List']= request.POST.get('Final_Install_Punch_List')
        request.session['Misc_Materials']          = request.POST.get('Misc_Materials')
        

        fm0 = optionDetails(request.POST)
        fm0.instance.projectManager_id = request.user.id
        if fm0.is_valid():
            messages.success(request,'Overview added successfully')
            # fm0.save()
            return HttpResponseRedirect('/1/')
    else:
     fm0 = optionDetails()
    return render(request, 'addData.html',{'form':fm0})



#page 1
def addGeneral(request):

    if request.method == "POST":
        request.session['Year_old'] = request.POST.get('Year_old')
        request.session['Customer_Ease'] = request.POST.get('Customer_Ease')

        fm1 = generalQuestion(request.POST)
        if fm1.is_valid():
            messages.success(request,'General Details added successfully')
    #         fm1.save()
            return HttpResponseRedirect('/2/')
    else:
        fm1 = generalQuestion()
    return render(request, 'general.html',{'form':fm1})

#page 2
def framing(request):
    if request.session['Framing'] == "on":
        if request.method == "POST":
            request.session['Framing_LF_of_Walls'] = request.POST.get('Framing_LF_of_Walls')
            request.session['Framing_LF_of_Bulkheads'] = request.POST.get('Framing_LF_of_Bulkheads')
            
            fm2 = framingQuestion(request.POST)
            if fm2.is_valid():
                messages.success(request,'Framing Details added successfully')
        #         fm2.save()
                return HttpResponseRedirect('/3/')
        else:
            fm2 = framingQuestion()
        return render(request, 'framing.html',{'form':fm2})
    else:
        return HttpResponseRedirect('/3/')

        
#page 3
def hvac(request):
    if request.session['HVAC'] == "on":
        if request.method == "POST":
            request.session['HVAC_RSE_Vents'] = request.POST.get('HVAC_RSE_Vents')
            
            fm3 = hvacQuestion(request.POST)
            if fm3.is_valid():
                messages.success(request,'hvac Details added successfully')
        #         fm3.save()
                return HttpResponseRedirect('/4/')
        else:
            fm3 = hvacQuestion()
        return render(request, 'hvac.html',{'form':fm3})
    else:
        return HttpResponseRedirect('/4/')

#page 4
def plumbing(request):
    if request.session['Plumbing_Rough'] == "on":
        if request.method == "POST":
            request.session['Cast_Iron_Pipe_Connection'] = request.POST.get('Cast_Iron_Pipe_Connection')
            request.session['ConcreteRemoval'] =            request.POST.get('ConcreteRemoval')
            request.session['Concrete_to_be_Broken'] = request.POST.get('Concrete_to_be_Broken')
            request.session['Plumbing_Correct_Location'] = request.POST.get('Plumbing_Correct_Location')
            request.session['LF_of_Underground'] = request.POST.get('LF_of_Underground')
            request.session['Rough_In_Water_Lines'] = request.POST.get('Rough_In_Water_Lines')
            
            
            fm4 = plumbingQuestion(request.POST)
            if fm4.is_valid():
                messages.success(request,'Plumbing details added successfully')
        #         fm4.save()
                return HttpResponseRedirect('/6/')
        else:
            fm4 = plumbingQuestion()
        return render(request, 'plumbing.html',{'form':fm4})
    else:
        return HttpResponseRedirect('/6/')


# #page 5
# def plumbing1(request):
#     if request.session['Plumbing_Final'] == "on":
#         if request.method == "POST":
#             request.session['LF_of_Underground'] = request.POST.get('LF_of_Underground')
#             request.session['Rough_In_Water_Lines'] = request.POST.get('Rough_In_Water_Lines')

#             fm5 = plumbingQuestion1(request.POST)
#             if fm5.is_valid():
#                 messages.success(request,'Plumbing1 details added successfully')
#         #         fm5.save()
#                 return HttpResponseRedirect('/6/')
#         else:
#             fm5 = plumbingQuestion1()
#         return render(request, 'plumbing1.html',{'form':fm5})
#     else:
#         return HttpResponseRedirect('/7/')



#page 6
def plumbing2(request):
    if request.session['Plumbing_Final'] == "on":
        if request.method == "POST":
            request.session['Set_Toilet']                = request.POST.get('Set_Toilet')
            request.session['Trim_Out_Fixtures']         = request.POST.get('Trim_Out_Fixtures')
            request.session['Vanity_Faucet']           = request.POST.get('Vanity_Faucet')
            request.session['Dishwater']                 = request.POST.get('Dishwater')
            request.session['Sink']                      =    request.POST.get('Sink')
            request.session['Refigerator_Water_Line']   = request.POST.get('Refigerator_Water_Line')

            fm6 = plumbingQuestion2(request.POST)
            if fm6.is_valid():
                messages.success(request,'Plumbing2 details added successfully')
        #         fm6.save()
                return HttpResponseRedirect('/7/')
        else:
            fm6 = plumbingQuestion2()
        return render(request, 'plumbing2.html',{'form':fm6})
    else:
        return HttpResponseRedirect('/7/')



#page 7
def electric(request):
    if request.session['Electrical_Rough'] == "on":
        if request.method == "POST":
            request.session['Electrical_sqft'] = request.POST.get('Electrical_sqft')
            request.session['Panel_Location'] = request.POST.get('Panel_Location')
            

            fm7 = electricQuestion(request.POST)
            if fm7.is_valid():
                messages.success(request,'Electrical details added successfully')
        #         fm7.save()
                return HttpResponseRedirect('/8/')
        else:
            fm7 = electricQuestion()
        return render(request, 'electric.html',{'form':fm7})
    else:
        return HttpResponseRedirect('/8/')

#page 8
def electric1(request):
    if request.session['Electrical_Final'] == "on":
        if request.method == "POST":
            request.session['Dimmer_Switches']       = request.POST.get('Dimmer_Switches')
            request.session['Undercabinet_Lighting'] = request.POST.get('Undercabinet_Lighting')
            request.session['SubPanel']               = request.POST.get('SubPanel')
            request.session['Fan_Install']           = request.POST.get('Fan_Install')

            fm8 = electricQuestion1(request.POST)
            if fm8.is_valid():
                messages.success(request,'Electrical1 details added successfully')
        #         fm8.save()
                return HttpResponseRedirect('/9/')
        else:
            fm8 = electricQuestion1()
        return render(request, 'electric1.html',{'form':fm8})
    else:
        return HttpResponseRedirect('/9/')

#page 9
def insulation(request):
    if request.session['Insulation'] == "on":
        if request.method == "POST":
            request.session['Insulation_sqft'] = request.POST.get('Insulation_sqft')
        
            fm9 = insulationQuestion(request.POST)
            if fm9.is_valid():
                messages.success(request,'Insulation details added successfully')
        #         fm9.save()
                return HttpResponseRedirect('/10/')
        else:
            fm9 = insulationQuestion()
        return render(request, 'insulation.html',{'form':fm9})
    else:
        return HttpResponseRedirect('/10/')


#page 10
def drywall(request):
    if request.session['Drywall'] == "on":
        if request.method == "POST":
            request.session['Drywall_sqft'] = request.POST.get('Drywall_sqft')
            request.session['Wall_Texture'] = request.POST.get('Wall_Texture')
            request.session['Ceiling_Texture'] = request.POST.get('Ceiling_Texture')
           
            fm10 = drywallQuestion(request.POST)
            if fm10.is_valid():
                messages.success(request,'Drywall details added successfully')
        #         fm10.save()
                return HttpResponseRedirect('/11/')
        else:
            fm10 = drywallQuestion()
        return render(request, 'drywall.html',{'form':fm10})
    else:
        return HttpResponseRedirect('/11/')


#page 11
def trim(request):
    if request.session['Trim'] == "on":
        if request.method == "POST":
            request.session['LF_of_Cabinetry'] = request.POST.get('LF_of_Cabinetry')
            request.session['LF_of_baseboard'] = request.POST.get('LF_of_baseboard')
            request.session['Casing_LF'] = request.POST.get('Casing_LF')
            request.session['Solid_core_doors'] = request.POST.get('Solid_core_doors')
           
            fm11 = trimQuestion(request.POST)
            if fm11.is_valid():
                messages.success(request,'Trim details added successfully')
        #         fm11.save()
                return HttpResponseRedirect('/12/')
        else:
            fm11 = trimQuestion()
        return render(request, 'trim.html',{'form':fm11})
    else:
        return HttpResponseRedirect('/12/')


#page 12
def paint(request):
    if request.session['Painting'] == "on":
        if request.method == "POST":
            request.session['Paint_sqft'] = request.POST.get('Paint_sqft')
            request.session['add_colors'] = request.POST.get('add_colors')
       
           
            fm12 = paintQuestion(request.POST)
            if fm12.is_valid():
                messages.success(request,'Paint details added successfully')
        #         fm12.save()
                return HttpResponseRedirect('/13/')
        else:
            fm12 = paintQuestion()
        return render(request, 'paint.html',{'form':fm12})
    else:
        return HttpResponseRedirect('/13/')



#page 13
def countertop(request):
    if request.session['Countertops'] == "on":
        if request.method == "POST":
            request.session['Countertop_type'] = request.POST.get('Countertop_type')
            request.session['Countertop_sqft'] = request.POST.get('Countertop_sqft')
       
           
            fm13 = countertopQuestion(request.POST)
            if fm13.is_valid():
                messages.success(request,'Paint details added successfully')
        #         fm13.save()
                return HttpResponseRedirect('/14/')
        else:
            fm13 = countertopQuestion()
        return render(request, 'countertop.html',{'form':fm13})
    else:
        return HttpResponseRedirect('/14/')


#page 14
def tile(request):
    if request.session['Tile'] == "on":
        if request.method == "POST":
            request.session['Tile_floor']       =     request.POST.get('Tile_floor')
            request.session['Tile_Backsplash'] = request.POST.get('Tile_Backsplash')
            request.session['Tile_Shower']           = request.POST.get('Tile_Shower')
            request.session['Tile_floor_sqft'] = request.POST.get('Tile_floor_sqft')
            request.session['Tile_Backsplash_sqft'] = request.POST.get('Tile_Backsplash_sqft')
            request.session['Tile_Shower_sqft'] = request.POST.get('Tile_Shower_sqft')
       
           
            fm14 = tileQuestion(request.POST)
            if fm14.is_valid():
                messages.success(request,'Paint details added successfully')
        #         fm14.save()
                return HttpResponseRedirect('/16/')
        else:
            fm14 = tileQuestion()
        return render(request, 'tile.html',{'form':fm14})
    else:
        return HttpResponseRedirect('/16/')



# #page 15
# def tile1(request):
#         if request.method == "POST":
#             request.session['Tile_floor_sqft'] = request.POST.get('Tile_floor_sqft')
#             request.session['Tile_Backsplash_sqft'] = request.POST.get('Tile_Backsplash_sqft')
#             request.session['Tile_Shower_sqft'] = request.POST.get('Tile_Shower_sqft')
       
           
#             fm15 = tileQuestion1(request.POST)
#             if fm15.is_valid():
#                 messages.success(request,'Paint details added successfully')
#         #         fm15.save()
#                 return HttpResponseRedirect('/16/')
#         else:
#             fm15 = tileQuestion1()
#         return render(request, 'tile1.html',{'form':fm15})
   


#page 16
def floor(request):
    if request.session['Flooring'] == "on":
        if request.method == "POST":
            request.session['Floor_sqft'] = request.POST.get('Floor_sqft')
                   
            fm16 = floorQuestion(request.POST)
            if fm16.is_valid():
                messages.success(request,'Tile details added successfully')
        #         fm16.save()
                return HttpResponseRedirect('/17/')
        else:
            fm16 = floorQuestion()
        return render(request, 'floor.html',{'form':fm16})
    else:
        return HttpResponseRedirect('/17/')

#page 17
def carpet(request):
    if request.session['Carpet'] == "on":
        if request.method == "POST":
            request.session['Carpet_sqft'] = request.POST.get('Carpet_sqft')
                   
            fm17 = carpetQuestion(request.POST)
            if fm17.is_valid():
                messages.success(request,'Floor details added successfully')
        #         fm17.save()
                return HttpResponseRedirect('/18/')
        else:
            fm17 = carpetQuestion()
        return render(request, 'carpet.html',{'form':fm17})
    else:
        return HttpResponseRedirect('/18/')



#page 18
def bathallow(request):
    if request.session['Bathroom_Allowance'] == "on":
        if request.method == "POST":
            request.session['Bathroom_Allowance_items_type'] = request.POST.get('Bathroom_Allowance_items_type')
            request.session['Bathroom_Allowance_item1']    = request.POST.get('Bathroom_Allowance_item1')
            request.session['Bathroom_Allowance_item2']    = request.POST.get('Bathroom_Allowance_item2')
            request.session['Bathroom_Allowance_item3']    = request.POST.get('Bathroom_Allowance_item3')
            request.session['Bathroom_Allowance_item4']    = request.POST.get('Bathroom_Allowance_item4')
            request.session['Bathroom_Allowance_item5']    = request.POST.get('Bathroom_Allowance_item5')    
            
            fm18 = bathallowQuestion(request.POST)
            if fm18.is_valid():
                messages.success(request,'Bathallowance details added successfully')
        #         fm18.save()
                return HttpResponseRedirect('/19/')
        else:
            fm18 = bathallowQuestion()
        return render(request, 'bathallowance.html',{'form':fm18})
    else:
        return HttpResponseRedirect('/19/')




#page 19
def barallow(request):
    if request.session['Bar_Allowances'] == "on":
        if request.method == "POST":
            request.session['Bar_Allowance_items_type'] = request.POST.get('Bar_Allowance_items_type')
            request.session['Bar_Allowance_item1'] = request.POST.get('Bar_Allowance_item1')
            request.session['Bar_Allowance_item2'] = request.POST.get('Bar_Allowance_item2')
            request.session['Bar_Allowance_item3'] = request.POST.get('Bar_Allowance_item3')
            request.session['Bar_Allowance_item4'] = request.POST.get('Bar_Allowance_item4')
            request.session['Bar_Allowance_item5'] = request.POST.get('Bar_Allowance_item5')    
            
            fm19 = barallowQuestion(request.POST)
            if fm19.is_valid():
                messages.success(request,'Barallowance details added successfully')
        #         fm19.save()
                return HttpResponseRedirect('/20/')
        else:
            fm19 = barallowQuestion()
        return render(request, 'barallowance.html',{'form':fm19})
    else:
        return HttpResponseRedirect('/20/')


#page 20
def miscallow(request):
    if request.session['Misc_Materials'] == "on":
        if request.method == "POST":
            request.session['Misc_Allowance_items_type'] = request.POST.get('Misc_Allowance_items_type')
            request.session['Misc_Allowance_item1'] = request.POST.get('Misc_Allowance_item1')
            request.session['Misc_Allowance_item2'] = request.POST.get('Misc_Allowance_item2')
            request.session['Misc_Allowance_item3'] = request.POST.get('Misc_Allowance_item3')
            request.session['Misc_Allowance_item4'] = request.POST.get('Misc_Allowance_item4')
            request.session['Misc_Allowance_item5'] = request.POST.get('Misc_Allowance_item5')    
            request.session['Misc_Allowance_item1_no'] = request.POST.get('Misc_Allowance_item1_no')
            request.session['Misc_Allowance_item2_no'] = request.POST.get('Misc_Allowance_item2_no')
            request.session['Misc_Allowance_item3_no'] = request.POST.get('Misc_Allowance_item3_no')
            request.session['Misc_Allowance_item4_no'] = request.POST.get('Misc_Allowance_item4_no')
            request.session['Misc_Allowance_item5_no'] = request.POST.get('Misc_Allowance_item5_no')  
            
           
            fm20 = miscallowQuestion(request.POST)
            if fm20.is_valid():
                messages.success(request,'Barallowance details added successfully')              
               # fm20.save()
                return HttpResponseRedirect('/21/')
        else:
            fm20 = miscallowQuestion()
        return render(request, 'misc.html',{'form':fm20})
    else:
        return HttpResponseRedirect('/21/')

#page 21
def prefinal(request):
    if request.session['Final_Install_Punch_List'] == "on":
        if request.method == "POST":
            request.session['Final_install'] = request.POST.get('Final_install')
            request.session['Misc_Materials_val'] = request.POST.get('Misc_Materials_val')
            
            
           
            fm21 = finalQuestion(request.POST)
            if fm21.is_valid():
                messages.success(request,'Barallowance details added successfully')              
             #   fm21.save()
                return HttpResponseRedirect('/22/')
        else:
            fm21 = finalQuestion()
        return render(request, 'prefinal.html',{'form':fm21})
    else:
        return HttpResponseRedirect('/22/')


#page 22
def final(request):
    # if request.method == "POST":

        fm22 = request.POST.get(all) 
        fm23 = Customer()
              

        name = request.session['customerName']
        address = request.session['customerAddress']
        contact = request.session['customerContact']
        Email = request.session['customerEmail']

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

        try:
            request.session['Framing']
            if request.session['Framing'] == 'on':
                c = True
            else:
                c= False
        except: 
            c = False

        try:
            request.session['HVAC']
            if request.session['HVAC'] == 'on':
                d = True
            else:
                d= False
        except: 
            d = False

        try:
            request.session['Plumbing_Rough']
            if request.session['Plumbing_Rough'] == 'on':
                e = True
            else:
                e= False
        except: 
            e = False

        try:
            request.session['Plumbing_Final']
            if request.session['Plumbing_Final'] == 'on':
                f = True
            else:
                f= False
        except: 
            f = False

        try:
            request.session['Electrical_Rough']
            if request.session['Electrical_Rough'] == 'on':
                g = True
            else:
                g= False
        except: 
            g = False

        try:
            request.session['Electrical_Final']
            if request.session['Electrical_Final'] == 'on':
                h = True
            else:
                h= False
        except: 
            h = False

        try:
            request.session['Insulation']
            if request.session['Insulation'] == 'on':
                i = True
            else:
                i= False
        except: 
            i = False

        try:
            request.session['Drywall']
            if request.session['Drywall'] == 'on':
                j = True
            else:
                j= False
        except: 
            j = False

        try:
            request.session['Trim']
            if request.session['Trim'] == 'on':
                k = True
            else:
                k= False
        except: 
            k = False

        try:
            request.session['Painting']
            if request.session['Painting'] == 'on':
                l = True
            else:
                l= False
        except: 
            l = False

        try:
            request.session['Cabinetry']
            if request.session['Cabinetry'] == 'on':
                m = True
            else:
                m= False
        except: 
            m = False

        try:
            request.session['Countertops']
            if request.session['Countertops'] == 'on':
                n = True
            else:
                n= False
        except: 
            n = False

        try:
            request.session['Tile']
            if request.session['Tile'] == 'on':
                o = True
            else:
                o= False
        except: 
            o = False

        try:
            request.session['Flooring']
            if request.session['Flooring'] == 'on':
                p = True
            else:
                p= False
        except: 
            p = False

        try:
            request.session['Carpet']
            if request.session['Carpet'] == 'on':
                q = True
            else:
                q= False
        except: 
            q = False

        try:
            request.session['Bathroom_Allowance']
            if request.session['Bathroom_Allowance'] == 'on':
                r = True
            else:
                r= False
        except: 
            r = False

        try:
            request.session['Bar_Allowances']
            if request.session['Bar_Allowances'] == 'on':
                s = True
            else:
                s= False
        except: 
            s = False

        try:
            request.session['Final_Install_Punch_List']
            if request.session['Final_Install_Punch_List'] == 'on':
                t = True
            else:
                t= False
        except: 
            t = False

        try:
            request.session['Misc_Materials']
            if request.session['Misc_Materials'] == 'on':
                u = True
            else:
                u= False
        except: 
            u = False

        try:
            request.session['Cast_Iron_Pipe_Connection']
            if request.session['Cast_Iron_Pipe_Connection'] == 'on':
                v = True
            else:
                v= False
        except: 
            v = False

        try:
            request.session['ConcreteRemoval']
            if request.session['ConcreteRemoval'] == 'on':
                w = True
            else:
                w= False
        except: 
            w = False

        try:
            request.session['Plumbing_Correct_Location']
            if request.session['Plumbing_Correct_Location'] == 'on':
                x = True
            else:
                x= False
        except: 
            x = False

        try:
            request.session['Set_Toilet']
            if request.session['Set_Toilet'] == 'on':
                y = True
            else:
                y= False
        except: 
            y = False

        try:
            request.session['Trim_Out_Fixtures']
            if request.session['Trim_Out_Fixtures'] == 'on':
                z = True
            else:
                z= False
        except: 
            z = False

        try:
            request.session['Vanity_Faucet']
            if request.session['Vanity_Faucet'] == 'on':
                aa = True
            else:
                aa = False
        except: 
            aa = False

        try:
            request.session['Dishwater']
            if request.session['Dishwater'] == 'on':
                bb = True
            else:
                bb = False
        except: 
            bb = False


        try:
            request.session['Sink']
            if request.session['Sink'] == 'on':
                cc = True
            else:
                cc= False
        except: 
            cc = False


        try:
            request.session['Refigerator_Water_Line']
            if request.session['Refigerator_Water_Line'] == 'on':
                dd = True
            else:
                dd= False
        except: 
            dd = False

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
            request.session['Solid_core_doors']
            if request.session['Solid_core_doors'] == 'on':
                gg = True
            else:
                gg= False
        except: 
            gg = False


        try:
            request.session['Tile_floor']
            if request.session['Tile_floor'] == 'on':
                hh = True
            else:
                hh= False
        except: 
            hh = False


        try:
            request.session['Tile_Backsplash']
            if request.session['Tile_Backsplash'] == 'on':
                ii = True
            else:
                ii = False
        except: 
            ii = False

        try:
            request.session['Tile_Shower']
            if request.session['Tile_Shower'] == 'on':
                jj = True
            else:
                jj= False
        except: 
            jj = False

        try:
            request.session['Bathroom_Allowance_item1']
            if request.session['Bathroom_Allowance_item1'] == 'on':
                kk = True
            else:
                kk= False
        except: 
            kk = False

        try:
            request.session['Bathroom_Allowance_item2']
            if request.session['Bathroom_Allowance_item2'] == 'on':
                ll = True
            else:
                ll= False
        except: 
            ll = False

        try:
            request.session['Bathroom_Allowance_item3']
            if request.session['Bathroom_Allowance_item3'] == 'on':
                mm = True
            else:
                mm= False
        except: 
            mm = False

        try:
            request.session['Bathroom_Allowance_item4']
            if request.session['Bathroom_Allowance_item4'] == 'on':
                nn = True
            else:
                nn= False
        except: 
            nn = False

        try:
            request.session['Bathroom_Allowance_item5']
            if request.session['Bathroom_Allowance_item5'] == 'on':
                oo = True
            else:
                oo= False
        except: 
            oo = False

        try:
            request.session['Bar_Allowance_item1']
            if request.session['Bar_Allowance_item1'] == 'on':
                pp = True
            else:
                pp= False
        except: 
            pp = False

        try:
            request.session['Bar_Allowance_item2']
            if request.session['Bar_Allowance_item2'] == 'on':
                qq = True
            else:
                qq= False
        except: 
            qq = False

        try:
            request.session['Bar_Allowance_item3']
            if request.session['Bar_Allowance_item3'] == 'on':
                rr = True
            else:
                rr= False
        except: 
            rr = False

        try:
            request.session['Bar_Allowance_item4']
            if request.session['Bar_Allowance_item4'] == 'on':
                ss = True
            else:
                ss= False
        except: 
            ss = False

        try:
            request.session['Bar_Allowance_item5']
            if request.session['Bar_Allowance_item5'] == 'on':
                tt = True
            else:
                tt= False
        except: 
            tt = False

        try:
            request.session['Misc_Allowance_item1']
            if request.session['Misc_Allowance_item1'] == 'on':
                uu = True
            else:
                uu= False
        except: 
            uu = False


        try:
            request.session['Misc_Allowance_item2']
            if request.session['Misc_Allowance_item2'] == 'on':
                vv = True
            else:
                vv= False
        except: 
            vv = False


        try:
            request.session['Misc_Allowance_item3']
            if request.session['Misc_Allowance_item3'] == 'on':
                ww = True
            else:
                ww= False
        except: 
            ww = False


        try:
            request.session['Misc_Allowance_item4']
            if request.session['Misc_Allowance_item4'] == 'on':
                xx = True
            else:
                xx= False
        except: 
            xx = False


        try:
            request.session['Misc_Allowance_item5']
            if request.session['Misc_Allowance_item5'] == 'on':
                yy = True
            else:
                yy= False
        except: 
            yy = False


#Real Values

        
        try:
            request.session['Drywall_sqft']         
        except:
            request.session['Drywall_sqft'] = "0"

        try:
            request.session['Framing_LF_of_Walls']         
        except:
            request.session['Framing_LF_of_Walls'] = "0"

        try:
            request.session['Framing_LF_of_Bulkheads']         
        except:
            request.session['Framing_LF_of_Bulkheads'] = "0"   

        try:
            request.session['HVAC_RSE_Vents']         
        except:
            request.session['HVAC_RSE_Vents'] = "0"

        try:
            request.session['LF_of_Underground']         
        except:
            request.session['LF_of_Underground'] = "0"

        try:
            request.session['Concrete_to_be_Broken']         
        except:
            request.session['Concrete_to_be_Broken'] = "0"

        try:
            request.session['Rough_In_Water_Lines']         
        except:
            request.session['Rough_In_Water_Lines'] = "0"

        try:
            request.session['Electrical_sqft']         
        except:
            request.session['Electrical_sqft'] = "0"
        
        try:
            request.session['Panel_Location']         
        except:
            request.session['Panel_Location'] = "0"

        try:
            request.session['Dimmer_Switches']         
        except:
            request.session['Dimmer_Switches'] = "0"

        
        try:
            request.session['Fan_Install']         
        except:
            request.session['Fan_Install'] = "0"


        try:
            request.session['Insulation_sqft']         
        except:
            request.session['Insulation_sqft'] = "0"

        try:
            request.session['Drywall_sqft']         
        except:
            request.session['Drywall_sqft'] = "0"

        try:
            request.session['Wall_Texture']         
        except:
            request.session['Wall_Texture'] = "0"

        try:
            request.session['Ceiling_Texture']         
        except:
            request.session['Ceiling_Texture'] = "0"

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
            request.session['Paint_sqft']         
        except:
            request.session['Paint_sqft'] = "0"

        try:
            request.session['add_colors']         
        except:
            request.session['add_colors'] = "0"

        try:
            request.session['Countertop_type']         
        except:
            request.session['Countertop_type'] = "0"

        try:
            request.session['Countertop_sqft']         
        except:
            request.session['Countertop_sqft'] = "0"

        try:
            request.session['Tile_floor_sqft']         
        except:
            request.session['Tile_floor_sqft'] = "0"

        try:
            request.session['Tile_Backsplash_sqft']         
        except:
            request.session['Tile_Backsplash_sqft'] = "0"

        try:
            request.session['Tile_Shower_sqft']         
        except:
            request.session['Tile_Shower_sqft'] = "0"

        try:
            request.session['Floor_sqft']         
        except:
            request.session['Floor_sqft'] = "0"

        try:
            request.session['Carpet_sqft']         
        except:
            request.session['Carpet_sqft'] = "0"

        try:
            request.session['Bathroom_Allowance_items_type']         
        except:
            request.session['Bathroom_Allowance_items_type'] = "0"

        try:
            request.session['Bar_Allowance_items_type']         
        except:
            request.session['Bar_Allowance_items_type'] = "0"

        try:
            request.session['Final_install']         
        except:
            request.session['Final_install'] = "0"

        try:
            request.session['Misc_Materials_val']         
        except:
            request.session['Misc_Materials_val'] = "0"


        HouseOld             = request.session['Year_old']
        CustomerEase         = request.session['Customer_Ease']
        FramingLFofWalls     = request.session['Framing_LF_of_Walls']
        FramingLFofBulkheads = request.session['Framing_LF_of_Bulkheads']
        HVACVents            = request.session['HVAC_RSE_Vents']
        UndergroundFeet      = request.session['LF_of_Underground']
        ConcreteBreak        = request.session['Concrete_to_be_Broken']
        RoughWaterLines      = request.session['Rough_In_Water_Lines']
        ElectricalArea       = request.session['Electrical_sqft']
        PanelLocation        = request.session['Panel_Location']
        DimmerSwitches       = request.session['Dimmer_Switches']
        FanInstall           = request.session['Fan_Install']
        InsulationArea       = request.session['Insulation_sqft']
        drywallArea          = request.session['Drywall_sqft']
        WallTexture          = request.session['Wall_Texture']
        CeilTexture          = request.session['Ceiling_Texture']
        Doors                = request.session['No_of_doors']
        CabinetryArea        = request.session['LF_of_Cabinetry']
        BaseboardArea        = request.session['LF_of_baseboard']
        CasingLength         = request.session['Casing_LF']
        PaintArea            = request.session['Paint_sqft']
        NumberOfColors       = request.session['add_colors']
        CountertopType       = request.session['Countertop_type']
        CountertopArea       = request.session['Countertop_sqft']
        FloorTileArea        = request.session['Tile_floor_sqft']
        BacksplashArea       = request.session['Tile_Backsplash_sqft']
        ShowerArea           = request.session['Tile_Shower_sqft']
        FloorArea            = request.session['Floor_sqft']
        CarpetArea           = request.session['Carpet_sqft']
        BathAllowanceType    = request.session['Bathroom_Allowance_items_type']
        BarAllowanceType     = request.session['Bar_Allowance_items_type']
        FinalInstall         = request.session['Final_install']
        MiscMatrialValue     = request.session['Misc_Materials_val']










       
        fm23.projectManager_id = request.user.id
        fm23.customerName = request.session['customerName']
        fm23.customerContact = request.session['customerContact']
        fm23.customerEmail = request.session['customerEmail']
        fm23.customerAddress = request.session['customerAddress']
        fm23.Permit = a               
        fm23.Dumpster = b               
        fm23.Framing = c                 
        fm23.HVAC =  d                  
        fm23.Plumbing_Rough = e         
        fm23.Plumbing_Final = f         
        fm23.Electrical_Rough = g       
        fm23.Electrical_Final = h       
        fm23.Insulation = i            
        fm23.Drywall =  j               
        fm23.Trim =  k                  
        fm23.Painting =   l             
        fm23.Cabinetry =  m             
        fm23.Countertops =  n           
        fm23.Tile =  o                  
        fm23.Flooring = p                
        fm23.Carpet =   q               
        fm23.Bathroom_Allowance = r     
        fm23.Bar_Allowances =  s        
        fm23.Final_Install_Punch_List = t
        fm23.Misc_Materials = u
        fm23.Cast_Iron_Pipe_Connection = v
        fm23.ConcreteRemoval = w
        fm23.Plumbing_Correct_Location =x
        fm23.Set_Toilet = y
        fm23.Trim_Out_Fixtures= z
        fm23.Vanity_Faucet = aa
        fm23.Dishwater = bb
        fm23.Sink = cc     
        fm23.Refigerator_Water_Line = dd
        fm23.Undercabinet_Lighting =ee
        fm23.SubPanel = ff
        fm23.Solid_core_doors = gg
        fm23.Tile_floor = hh
        fm23.Tile_Backsplash = ii
        fm23.Tile_Shower = jj
        fm23.Bathroom_Allowance_item1 = kk
        fm23.Bathroom_Allowance_item2 = ll
        fm23.Bathroom_Allowance_item3 = mm
        fm23.Bathroom_Allowance_item4 = nn
        fm23.Bathroom_Allowance_item5 = oo
        fm23.Bar_Allowance_item1 = pp
        fm23.Bar_Allowance_item2 = qq
        fm23.Bar_Allowance_item3 = rr
        fm23.Bar_Allowance_item4 = ss
        fm23.Bar_Allowance_item5 = tt
        fm23.Misc_Allowance_item1 = uu
        fm23.Misc_Allowance_item2 = vv
        fm23.Misc_Allowance_item3 = ww
        fm23.Misc_Allowance_item4 = xx
        fm23.Misc_Allowance_item5 = yy
        fm23.Year_old                   = HouseOld
        fm23.Customer_Ease              = CustomerEase
        fm23.Framing_LF_of_Walls        = FramingLFofWalls
        fm23.Framing_LF_of_Bulkheads    = FramingLFofBulkheads
        fm23.HVAC_RSE_Vents             = HVACVents
        fm23.LF_of_Underground          = UndergroundFeet
        fm23.Concrete_to_be_Broken      = ConcreteBreak
        fm23.Rough_In_Water_Lines       = RoughWaterLines
        fm23.Electrical_sqft            = ElectricalArea
        fm23.Panel_Location             = PanelLocation
        fm23.Dimmer_Switches            = DimmerSwitches
        fm23.Fan_Install                = FanInstall
        fm23.Insulation_sqft            = InsulationArea
        fm23.Drywall_sqft               = drywallArea
        fm23.Wall_Texture               = WallTexture
        fm23.Ceiling_Texture            = CeilTexture
        fm23.No_of_doors                = Doors
        fm23.LF_of_Cabinetry            = CabinetryArea
        fm23.LF_of_baseboard            = BaseboardArea
        fm23.Casing_LF                  = CasingLength
        fm23.Paint_sqft                 = PaintArea
        fm23.add_colors                 = NumberOfColors
        fm23.Countertop_type            = CountertopType
        fm23.Countertop_sqft            = CountertopArea
        fm23.Tile_floor_sqft            = FloorTileArea
        fm23.Tile_Backsplash_sqft       = BacksplashArea
        fm23.Tile_Shower_sqft           = ShowerArea
        fm23.Floor_sqft                 = FloorArea
        fm23.Carpet_sqft                = CarpetArea
        fm23.Bathroom_Allowance_items_type= BathAllowanceType
        fm23.Bar_Allowance_items_type   = BarAllowanceType
        fm23.Final_install              = FinalInstall
        fm23.Misc_Materials_val         = MiscMatrialValue

        
        
            

        messages.success(request,'Data added successfully')              
        fm23.save()
        return render(request, 'getsession.html',
    {'name':name,
    'address':address,
    'contact': contact,
    'Email':Email,
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
        'f': f,
        'g': g,
        'h': h,
        'i': i,
        'j': j,
        'k': k,
        'l': l,
        'm': m,
        'n': n,
        'o': o,
        'p': p,
        'q': q,
        'r': r,
        's': s,
        't': t,
        'u': u,
        'v': v,
        'w': w,
        'x': x,
        'y': y,
        'z': z,
        'aa' : aa,
        'bb' : bb,
        'cc' : cc,
        'dd' : dd,
        'ee' : ee,
        'ff' : ff,
        'gg' : gg,
        'hh' : hh,
        'ii' : ii,
        'jj' : jj,
        'kk' : kk,
        'll' : ll,
        'mm' : mm,
        'nn' : nn,
        'oo' : oo,
        'pp' : pp,
        'qq' : qq,
        'rr' : rr,
        'ss' : ss,
        'tt' : tt,
        'uu' : uu,
        'vv' : vv,
        'ww' : ww,
        'xx' : xx,
        'yy' : yy,})
    # else:
    #     fm22 = miscallowQuestion()
    #     return render(request, 'misc.html',{'form':fm22})
   

# def obtain(request):
#     if request.session['dumpster'] == "on":
#         if request.method == "POST":                       
#                 fm3 = questionDetails(request.POST)
#                 if fm3.is_valid():'LF_of_Underground',                 
                      
#                     messages.success(request,'you are going goog')
#                     # fm3.save()
#                 return HttpResponseRedirect('/obtain/')
#         else:
#             fm3 = questionDetails()
#         return render(request, 'addCustomer.html',{'form':fm3})
#     else:
#         fm3 = questionDetails()
# #     return render(request, 'obtain.html',{'form':fm3})
# def AllCustomer(request):
#     AllCustomers = Customer.objects.all()
#     return render(request, 'list.html', locals())

def getsession(request):
    name = request.session['customerName']
    address = request.session['customerAddress']
    contact = request.session['customerContact']
    Email = request.session['customerEmail']
    a = a         
    b = b        
    c = c         
    d = d         
    e = e         
    f = f         
    g = g       
    h = h      
    i = i         
    j = j         
    k = k         
    l = l         
    m = m         
    n = n         
    o = o         
    p = p         
    q = q         
    r = r      
    s = s         
    t = t
    u = u         
    v   = v
    w   = w         
    x   = x
    y   = y       
    z   = z     
    aa = aa       
    bb = bb       
    cc = cc       
    dd = dd
    ee = ee
    ff = ff
    gg = gg
    hh = hh
    ii = ii
    jj = jj
    kk = kk    
    ll = ll    
    mm = mm    
    nn = nn    
    oo = oo    
    pp = pp
    qq = qq
    rr = rr
    ss = ss
    tt = tt
    uu = uu
    vv = vv
    ww = ww
    xx = xx
    yy = yy

    return render(request, 'getsession.html',
    {'name':name,
    'address':address,
    'contact': contact,
    'Email':Email,
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
        'f': f,
        'g': g,
        'h': h,
        'i': i,
        'j': j,
        'k': k,
        'l': l,
        'm': m,
        'n': n,
        'o': o,
        'p': p,
        'q': q,
        'r': r,
        's': s,
        't': t,
        'u': u,
        'v': v,
        'w': w,
        'x': x,
        'y': y,
        'z': z,
        'aa' : aa,
        'bb' : bb,
        'cc' : cc,
        'dd' : dd,
        'ee' : ee,
        'ff' : ff,
        'gg' : gg,
        'hh' : hh,
        'ii' : ii,
        'jj' : jj,
        'kk' : kk,
        'll' : ll,
        'mm' : mm,
        'nn' : nn,
        'oo' : oo,
        'pp' : pp,
        'qq' : qq,
        'rr' : rr,
        'ss' : ss,
        'tt' : tt,
        'uu' : uu,
        'vv' : vv,
        'ww' : ww,
        'xx' : xx,
        'yy' : yy,})






# def addData(request):
#     if request.method == "POST":
        
#         fm = EstimatorData(request.POST)
        
        

#         if fm.is_valid():
#             messages.success(request,'data added successfully')
#             fm.save()
#     else:
#      fm = EstimatorData()
#     return render(request, 'addData.html',{'form':fm})