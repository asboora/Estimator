
import imp
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ..models import Markup, Unitprice
from ..overview import plumbingQuestion
from django.contrib import messages



#page 4
def plumbing(request):
   
    if request.method == "POST":
        request.session['Cast_Iron_Pipe_Connection'] = request.POST.get('Cast_Iron_Pipe_Connection')
        request.session['No_of_connections']         = request.POST.get('No_of_connections')
        request.session['ConcreteRemoval']           = request.POST.get('ConcreteRemoval')
        request.session['Concrete_to_be_Broken']    = request.POST.get('Concrete_to_be_Broken')
        request.session['Plumbing_Correct_Location'] = request.POST.get('Plumbing_Correct_Location')
        request.session['LF_of_Underground']        = request.POST.get('LF_of_Underground')
        request.session['Rough_In_Water_Lines']     = request.POST.get('Rough_In_Water_Lines')
        request.session['Set_Toilet']                = request.POST.get('Set_Toilet')
        request.session['Trim_Out_Fixtures']         = request.POST.get('Trim_Out_Fixtures')
        request.session['Vanity_Faucet']           = request.POST.get('Vanity_Faucet')
        request.session['Dishwater']                 = request.POST.get('Dishwater')
        request.session['Sink']                      =    request.POST.get('Sink')
        request.session['Refigerator_Water_Line']   = request.POST.get('Refigerator_Water_Line')
        
        fm4 = plumbingQuestion(request.POST)
        
        if fm4.is_valid():
            messages.success(request,'Plumbing details added successfully')

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
                    request.session['No_of_connections']         
                except:
                    request.session['No_of_connections'] = "0"

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


            CastConnections         = request.session['No_of_connections']
            UndergroundFeetKey      = request.session['LF_of_Underground']
            ConcreteBreakKey        = request.session['Concrete_to_be_Broken']
            RoughWaterLinesKey      = request.session['Rough_In_Water_Lines']


            # Plumbing Details Calculation

    #CastIronConnections
        castConnectionValue = CastConnections

        castConnectionMarkup = Markup.objects.only('No_of_connections').get(pk=1).No_of_connections

        castConnectionPrice = Unitprice.objects.only('No_of_connections').get(pk=1).No_of_connections

        castConnectionEstimate = float(castConnectionValue)*float(castConnectionPrice)*(1+float(castConnectionMarkup)/100)



    #ConcreteRemoval 
        concreteValue = ConcreteBreakKey

        concreteMarkup = Markup.objects.only('Concrete_to_be_Broken').get(pk=1).Concrete_to_be_Broken

        concretePrice = Unitprice.objects.only('Concrete_to_be_Broken').get(pk=1).Concrete_to_be_Broken

        concreteEstimate = float(concreteValue)*float(concretePrice)*(1+float(concreteMarkup)/100)

    #LFofUnderground 

        LFofUndergroundValue = UndergroundFeetKey

        LFofUndergroundMarkup = Markup.objects.only('LF_of_Underground').get(pk=1).LF_of_Underground

        LFofUndergroundPrice = Unitprice.objects.only('LF_of_Underground').get(pk=1).LF_of_Underground

        LFofUndergroundEstimate = float(LFofUndergroundValue)*float(LFofUndergroundPrice)*(1+float(LFofUndergroundMarkup)/100)

    #RoughIn WaterLines 

        RoughInWaterLinesValue = RoughWaterLinesKey

        RoughInWaterLinesMarkup = Markup.objects.only('Rough_In_Water_Lines').get(pk=1).Rough_In_Water_Lines

        RoughInWaterLinesPrice = Unitprice.objects.only('Rough_In_Water_Lines').get(pk=1).Rough_In_Water_Lines

        RoughInWaterLinesEstimate = float(RoughInWaterLinesValue)*float(RoughInWaterLinesPrice)*(1+float(RoughInWaterLinesMarkup)/100)
        
        
    #Set Toilet

        setToiletPrice = 0
        if y == True:
            setToiletPrice = Unitprice.objects.only('Set_Toilet').get(pk =1).Set_Toilet
        else:
            setToiletPrice = 0
        

        setToiletMarkup = Markup.objects.only('Set_Toilet').get(pk=1).Set_Toilet

        setToiletEstimate = setToiletPrice*(1+setToiletMarkup/100)
        
    #Trim Out Fixtures

        trimOutFixturesPrice = 0
        if z == True:
            trimOutFixturesPrice = Unitprice.objects.only('Trim_Out_Fixtures').get(pk =1).Trim_Out_Fixtures
        else:
            trimOutFixturesPrice = 0
       

        trimOutFixturesMarkup = Markup.objects.only('Trim_Out_Fixtures').get(pk=1).Trim_Out_Fixtures

        trimOutFixturesEstimate = trimOutFixturesPrice*(1+trimOutFixturesMarkup/100)
        
        
  
        
    #Vanity Faucet

        vanityFaucetPrice = 0
        if aa == True:
            vanityFaucetPrice = Unitprice.objects.only('Vanity_Faucet').get(pk =1).Vanity_Faucet
        else:
            vanityFaucetPrice = 0
   

        vanityFaucetMarkup = Markup.objects.only('Vanity_Faucet').get(pk=1).Vanity_Faucet

        vanityFaucetEstimate = vanityFaucetPrice*(1+vanityFaucetMarkup/100)
        
               

    # Bar Addition
    #Dishwasher

        dishwasherPrice = 0
        if bb == True:
            dishwasherPrice = Unitprice.objects.only('Dishwater').get(pk =1).Dishwater
        else:
            dishwasherPrice = 0
        

        dishwasherMarkup = Markup.objects.only('Dishwater').get(pk=1).Dishwater

        dishwasherEstimate = dishwasherPrice*(1+dishwasherMarkup/100)
        
        
    #sink

        sinkPrice = 0
        if cc == True:
            sinkPrice = Unitprice.objects.only('Sink').get(pk =1).Sink
        else:
            sinkPrice = 0
      

        sinkMarkup = Markup.objects.only('Sink').get(pk=1).Sink

        sinkEstimate = sinkPrice*(1+sinkMarkup/100)
        
        
    #refigeratorWaterLine

        refigeratorWaterLinePrice = 0
        if dd == True:
            refigeratorWaterLinePrice = Unitprice.objects.only('Refigerator_Water_Line').get(pk =1).Refigerator_Water_Line
        else:
            refigeratorWaterLinePrice = 0
        

        refigeratorWaterLineMarkup = Markup.objects.only('Refigerator_Water_Line').get(pk=1).Refigerator_Water_Line

        refigeratorWaterLineEstimate = refigeratorWaterLinePrice*(1+refigeratorWaterLineMarkup/100)


# TOTAL PLUMBING ESTIMATE 

        totalPlumbingEstimate = (castConnectionEstimate + 
                                concreteEstimate + 
                                LFofUndergroundEstimate + 
                                RoughInWaterLinesEstimate + 
                                setToiletEstimate + 
                                trimOutFixturesEstimate + 
                                vanityFaucetEstimate + 
                                dishwasherEstimate + 
                                sinkEstimate +  
                                refigeratorWaterLineEstimate)
        


    #         fm4.save()
        return render(request, 'plumbing.html',{'form':fm4,'estimate':totalPlumbingEstimate})
    else:
        fm4 = plumbingQuestion()
    return render(request, 'plumbing.html',{'form':fm4})
   
