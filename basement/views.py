

import imp
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .overview import barallowQuestion, bathallowQuestion,  countertopQuestion, customerDetails, drywallQuestion, electricQuestion, finalQuestion, floorQuestion, framingQuestion,  insulationQuestion, miscallowQuestion, optionDetails, paintQuestion, plumbingQuestion , hvacQuestion,   tileQuestion, trimQuestion
from django.contrib import messages
from .Calculation import calc1, final





#page 18
def bathallow(request):
    # if request.session['Bathroom_Allowance'] == "on":
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
    # else:
    #     return HttpResponseRedirect('/19/')




#page 19
def barallow(request):
    # if request.session['Bar_Allowances'] == "on":
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
    # else:
    #     return HttpResponseRedirect('/20/')


#page 20
def miscallow(request):
    # if request.session['Misc_Materials'] == "on":
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
    # else:
    #     return HttpResponseRedirect('/21/')

#page 21
def prefinal(request):
    # if request.session['Final_Install_Punch_List'] == "on":
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
    # else:
    #     return HttpResponseRedirect('/22/')

def final1(request):
        
        # custID = request.session['customerID']
        # name = request.session['customerName']
        # address = request.session['customerAddress']
        # contact = request.session['customerContact']
        # Email = request.session['customerEmail']
        # xyz = Customer()
        # xyz.projectManager_id = request.user.id
        # xyz.customerID= custID
        # xyz.customerName = name
        # xyz.customerAddress = address
        # xyz.customerContact = contact
        # xyz.customerEmail = Email
        # xyz.save()
        
        
        q = request.session['No_of_doors']
        # q = Unitprice.objects.get(  pk = 1)
        print(q)
        return HttpResponse(q)




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



# #page 2
# def framing(request):
#     # if request.session['Framing'] == "on":
#         if request.method == "POST":
#             request.session['Framing_LF_of_Walls'] = request.POST.get('Framing_LF_of_Walls')
#             request.session['Framing_LF_of_Bulkheads'] = request.POST.get('Framing_LF_of_Bulkheads')
            
#             fm2 = framingQuestion(request.POST)
#             if fm2.is_valid():
#                 messages.success(request,'Framing Details added successfully')
#         #         fm2.save()
#                 return HttpResponseRedirect('/3/')
#         else:
#             fm2 = framingQuestion()
#         return render(request, 'framing.html',{'form':fm2})
#     # else:
#     #     return HttpResponseRedirect('/3/')



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
# def plumbing2(request):
#     # if request.session['Plumbing_Final'] == "on":
#         if request.method == "POST":
#             request.session['Set_Toilet']                = request.POST.get('Set_Toilet')
#             request.session['Trim_Out_Fixtures']         = request.POST.get('Trim_Out_Fixtures')
#             request.session['Vanity_Faucet']           = request.POST.get('Vanity_Faucet')
#             request.session['Dishwater']                 = request.POST.get('Dishwater')
#             request.session['Sink']                      =    request.POST.get('Sink')
#             request.session['Refigerator_Water_Line']   = request.POST.get('Refigerator_Water_Line')

#             fm6 = plumbingQuestion2(request.POST)
#             if fm6.is_valid():
#                 messages.success(request,'Plumbing2 details added successfully')
#         #         fm6.save()
#                 return HttpResponseRedirect('/7/')
#         else:
#             fm6 = plumbingQuestion2()
#         return render(request, 'plumbing2.html',{'form':fm6})
    # else:
    #     return HttpResponseRedirect('/7/')


# #page 17
# def carpet(request):
#     # if request.session['Carpet'] == "on":
#         if request.method == "POST":
#             request.session['Carpet_sqft'] = request.POST.get('Carpet_sqft')
                   
#             fm17 = carpetQuestion(request.POST)
#             if fm17.is_valid():
#                 messages.success(request,'Floor details added successfully')
#         #         fm17.save()
#                 return HttpResponseRedirect('/18/')
#         else:
#             fm17 = carpetQuestion()
#         return render(request, 'carpet.html',{'form':fm17})
#     # else:
#     #     return HttpResponseRedirect('/18/')


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
   
#page 3
# def hvac(request):
#     # if request.session['HVAC'] == "on":
#         if request.method == "POST":
#             request.session['HVAC_RSE_Vents'] = request.POST.get('HVAC_RSE_Vents')
            
#             fm3 = hvacQuestion(request.POST)
#             if fm3.is_valid():
#                 messages.success(request,'hvac Details added successfully')
#         #         fm3.save()
#                 return HttpResponseRedirect('/4/')
#         else:
#             fm3 = hvacQuestion()
#         return render(request, 'hvac.html',{'form':fm3})
#     # else:
#     #     return HttpResponseRedirect('/4/')


#page 4
# def plumbing(request):
#     # if request.session['Plumbing_Rough'] == "on":
#         if request.method == "POST":
#             request.session['Cast_Iron_Pipe_Connection'] = request.POST.get('Cast_Iron_Pipe_Connection')
#             request.session['No_of_connections']         = request.POST.get('No_of_connections')
#             request.session['ConcreteRemoval']           = request.POST.get('ConcreteRemoval')
#             request.session['Concrete_to_be_Broken']    = request.POST.get('Concrete_to_be_Broken')
#             request.session['Plumbing_Correct_Location'] = request.POST.get('Plumbing_Correct_Location')
#             request.session['LF_of_Underground']        = request.POST.get('LF_of_Underground')
#             request.session['Rough_In_Water_Lines']     = request.POST.get('Rough_In_Water_Lines')
#             request.session['Set_Toilet']                = request.POST.get('Set_Toilet')
#             request.session['Trim_Out_Fixtures']         = request.POST.get('Trim_Out_Fixtures')
#             request.session['Vanity_Faucet']           = request.POST.get('Vanity_Faucet')
#             request.session['Dishwater']                 = request.POST.get('Dishwater')
#             request.session['Sink']                      =    request.POST.get('Sink')
#             request.session['Refigerator_Water_Line']   = request.POST.get('Refigerator_Water_Line')
            
#             fm4 = plumbingQuestion(request.POST)
            
#             if fm4.is_valid():
#                 messages.success(request,'Plumbing details added successfully')
#         #         fm4.save()
#                 return HttpResponseRedirect('/6/')
#         else:
#             fm4 = plumbingQuestion()
#         return render(request, 'plumbing.html',{'form':fm4})
#     # else:
#     #     return HttpResponseRedirect('/6/')





# #page 7
# def electric(request):
#     # if request.session['Electrical_Rough'] == "on":
#         if request.method == "POST":
#             request.session['Electrical_sqft'] = request.POST.get('Electrical_sqft')
#             request.session['Panel_Location'] = request.POST.get('Panel_Location')
#             request.session['Dimmer_Switches']       = request.POST.get('Dimmer_Switches')
#             request.session['Undercabinet_Lighting'] = request.POST.get('Undercabinet_Lighting')
#             request.session['SubPanel']               = request.POST.get('SubPanel')
#             request.session['Fan_Install']           = request.POST.get('Fan_Install')

#             fm7 = electricQuestion(request.POST)
#             if fm7.is_valid():
#                 messages.success(request,'Electrical details added successfully')
#         #         fm7.save()
#                 return HttpResponseRedirect('/8/')
#         else:
#             fm7 = electricQuestion()
#         return render(request, 'electric.html',{'form':fm7})
#     # else:
#     #     return HttpResponseRedirect('/8/')



# #page 8
# def electric1(request):
#     # if request.session['Electrical_Final'] == "on":
#         if request.method == "POST":
#             request.session['Dimmer_Switches']       = request.POST.get('Dimmer_Switches')
#             request.session['Undercabinet_Lighting'] = request.POST.get('Undercabinet_Lighting')
#             request.session['SubPanel']               = request.POST.get('SubPanel')
#             request.session['Fan_Install']           = request.POST.get('Fan_Install')

#             fm8 = electricQuestion1(request.POST)
#             if fm8.is_valid():
#                 messages.success(request,'Electrical1 details added successfully')
#         #         fm8.save()
#                 return HttpResponseRedirect('/9/')
#         else:
#             fm8 = electricQuestion1()
#         return render(request, 'electric1.html',{'form':fm8})
#     # else:
#     #     return HttpResponseRedirect('/9/')



# #page 9
# def insulation(request):
#     # if request.session['Insulation'] == "on":
#         if request.method == "POST":
#             request.session['Insulation_sqft'] = request.POST.get('Insulation_sqft')
        
#             fm9 = insulationQuestion(request.POST)
#             if fm9.is_valid():
#                 messages.success(request,'Insulation details added successfully')
#         #         fm9.save()
#                 return HttpResponseRedirect('/10/')
#         else:
#             fm9 = insulationQuestion()
#         return render(request, 'insulation.html',{'form':fm9})
#     # else:
#     #     return HttpResponseRedirect('/10/')


# #page 10
# def drywall(request):
#     # if request.session['Drywall'] == "on":
#         if request.method == "POST":
#             request.session['Drywall_sqft'] = request.POST.get('Drywall_sqft')
#             request.session['Wall_Texture'] = request.POST.get('Wall_Texture')
#             request.session['Ceiling_Texture'] = request.POST.get('Ceiling_Texture')
           
#             fm10 = drywallQuestion(request.POST)
#             if fm10.is_valid():
#                 messages.success(request,'Drywall details added successfully')
#         #         fm10.save()
#                 return HttpResponseRedirect('/11/')
#         else:
#             fm10 = drywallQuestion()
#         return render(request, 'drywall.html',{'form':fm10})
#     # else:
#     #     return HttpResponseRedirect('/11/')




# #page 11
# def trim(request):
#     # if request.session['Trim'] == "on":
#         if request.method == "POST":

#             request.session['No_of_doors'] = request.POST.get('No_of_doors')
#             request.session['LF_of_Cabinetry'] = request.POST.get('LF_of_Cabinetry')
#             request.session['LF_of_baseboard'] = request.POST.get('LF_of_baseboard')
#             request.session['Casing_LF'] = request.POST.get('Casing_LF')
#             request.session['Stairs_skirting'] = request.POST.get('Stairs_skirting')
#             request.session['Solid_core_doors'] = request.POST.get('Solid_core_doors')
            

#             fm11 = trimQuestion(request.POST)
#             if fm11.is_valid():
#                 messages.success(request,'Trim details added successfully')
#         #         fm11.save()
                
#                 return HttpResponseRedirect('/12/')
#         else:
#             fm11 = trimQuestion()
#         return render(request, 'trim.html',{'form':fm11})
#     # else:
#     #     return HttpResponseRedirect('/12/')



# #page 12
# def paint(request):
#     # if request.session['Painting'] == "on":
#         if request.method == "POST":
#             request.session['Paint_sqft'] = request.POST.get('Paint_sqft')
#             request.session['add_colors'] = request.POST.get('add_colors')
       
           
#             fm12 = paintQuestion(request.POST)
#             if fm12.is_valid():
#                 messages.success(request,'Paint details added successfully')
#         #         fm12.save()
#                 return HttpResponseRedirect('/13/')
#         else:
#             fm12 = paintQuestion()
#         return render(request, 'paint.html',{'form':fm12})
#     # else:
#     #     return HttpResponseRedirect('/13/')





# #page 13
# def countertop(request):
#     # if request.session['Countertops'] == "on":
#         if request.method == "POST":
#             request.session['Countertop_type'] = request.POST.get('Countertop_type')
#             request.session['Countertop_sqft'] = request.POST.get('Countertop_sqft')
       
           
#             fm13 = countertopQuestion(request.POST)
#             if fm13.is_valid():
#                 messages.success(request,'Paint details added successfully')
#         #         fm13.save()
#                 return HttpResponseRedirect('/14/')
#         else:
#             fm13 = countertopQuestion()
#         return render(request, 'countertop.html',{'form':fm13})
#     # else:
#     #     return HttpResponseRedirect('/14/')



# #page 14
# def tile(request):
#     # if request.session['Tile'] == "on":
#         if request.method == "POST":
#             request.session['Tile_Backsplash_sqft']       =     request.POST.get('Tile_Backsplash_sqft')
#             request.session['BathType']                     = request.POST.get('BathType')
#             request.session['Shower_Pan_sqft']           = request.POST.get('Shower_Pan_sqft')
#             request.session['Wall_Tile_sqft']           = request.POST.get('Wall_Tile_sqft')
#             request.session['Niches']                   = request.POST.get('Niches')

       
            
#             fm14 = tileQuestion(request.POST)
#             if fm14.is_valid():
#                 messages.success(request,'Paint details added successfully')
#         #         fm14.save()
#                 return HttpResponseRedirect('/16/')
#         else:
#             fm14 = tileQuestion()
#         return render(request, 'tile.html',{'form':fm14})
#     # else:
#     #     return HttpResponseRedirect('/16/')


# #page 16
# def floor(request):
#     # if request.session['Flooring'] == "on":
#         if request.method == "POST":
#             request.session['Floor_sqft'] = request.POST.get('Floor_sqft')
#             request.session['Floor_Tile_sqft'] = request.POST.get('Floor_Tile_sqft')
#             request.session['Carpet_sqft'] = request.POST.get('Carpet_sqft')
                   
#             fm16 = floorQuestion(request.POST)
#             if fm16.is_valid():
#                 messages.success(request,'Tile details added successfully')
#         #         fm16.save()
#                 return HttpResponseRedirect('/17/')
#         else:
#             fm16 = floorQuestion()
#         return render(request, 'floor.html',{'form':fm16})
#     # else:
#     #     return HttpResponseRedirect('/17/')

