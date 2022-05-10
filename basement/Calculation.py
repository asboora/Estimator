from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import BarAllowanceTable, BathAllowanceTable, BooleansTable, CountertopTable, Customer, DrywallTable, ElectricalTable, FinalTable, FloorTable, FramingTable, HVACTable, InsulationTable, Markup, MiscAllowanceTable, PaintTable, PlumbingTable, TileTable, TrimTable, Unitprice
from django.contrib import messages

def calc1(request):
        custID = request.session['customerID']
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

        return render(request, 'addData.html',{'estimate':Page1Estimate})

#page 22
def final(request):
    # if request.method == "POST":
        custID = request.session['customerID']
        name = request.session['customerName']
        address = request.session['customerAddress']
        contact = request.session['customerContact']
        Email = request.session['customerEmail']
        


        try:
            request.session['Year_old']
            if request.session['Year_old'] == 'on':
               HouseOldKey = True
            else:
               HouseOldKey= False
        except: 
           HouseOldKey = False



        try:
            request.session['Customer_Ease']
            if request.session['Customer_Ease'] == 'on':
               CustomerEaseKey = True
            else:
               CustomerEaseKey= False
        except: 
           CustomerEaseKey = False



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





        # try:
        #     request.session['Framing']
        #     if request.session['Framing'] == 'on':
        #         c = True
        #     else:
        #         c= False
        # except: 
        #     c = False

        # try:
        #     request.session['HVAC']
        #     if request.session['HVAC'] == 'on':
        #         d = True
        #     else:
        #         d= False
        # except: 
        #     d = False

        # try:
        #     request.session['Plumbing_Rough']
        #     if request.session['Plumbing_Rough'] == 'on':
        #         e = True
        #     else:
        #         e= False
        # except: 
        #     e = False

        # try:
        #     request.session['Plumbing_Final']
        #     if request.session['Plumbing_Final'] == 'on':
        #         f = True
        #     else:
        #         f= False
        # except: 
        #     f = False

        # try:
        #     request.session['Electrical_Rough']
        #     if request.session['Electrical_Rough'] == 'on':
        #         g = True
        #     else:
        #         g= False
        # except: 
        #     g = False

        # try:
        #     request.session['Electrical_Final']
        #     if request.session['Electrical_Final'] == 'on':
        #         h = True
        #     else:
        #         h= False
        # except: 
        #     h = False

        # try:
        #     request.session['Insulation']
        #     if request.session['Insulation'] == 'on':
        #         i = True
        #     else:
        #         i= False
        # except: 
        #     i = False

        # try:
        #     request.session['Drywall']
        #     if request.session['Drywall'] == 'on':
        #         j = True
        #     else:
        #         j= False
        # except: 
        #     j = False

        # try:
        #     request.session['Trim']
        #     if request.session['Trim'] == 'on':
        #         k = True
        #     else:
        #         k= False
        # except: 
        #     k = False

        # try:
        #     request.session['Painting']
        #     if request.session['Painting'] == 'on':
        #         l = True
        #     else:
        #         l= False
        # except: 
        #     l = False

        # try:
        #     request.session['Cabinetry']
        #     if request.session['Cabinetry'] == 'on':
        #         m = True
        #     else:
        #         m= False
        # except: 
        #     m = False

        # try:
        #     request.session['Countertops']
        #     if request.session['Countertops'] == 'on':
        #         n = True
        #     else:
        #         n= False
        # except: 
        #     n = False

        # try:
        #     request.session['Tile']
        #     if request.session['Tile'] == 'on':
        #         o = True
        #     else:
        #         o= False
        # except: 
        #     o = False

        # try:
        #     request.session['Flooring']
        #     if request.session['Flooring'] == 'on':
        #         p = True
        #     else:
        #         p= False
        # except: 
        #     p = False

        # try:
        #     request.session['Carpet']
        #     if request.session['Carpet'] == 'on':
        #         q = True
        #     else:
        #         q= False
        # except: 
        #     q = False

        # try:
        #     request.session['Bathroom_Allowance']
        #     if request.session['Bathroom_Allowance'] == 'on':
        #         r = True
        #     else:
        #         r= False
        # except: 
        #     r = False

        # try:
        #     request.session['Bar_Allowances']
        #     if request.session['Bar_Allowances'] == 'on':
        #         s = True
        #     else:
        #         s= False
        # except: 
        #     s = False

        # try:
        #     request.session['Final_Install_Punch_List']
        #     if request.session['Final_Install_Punch_List'] == 'on':
        #         t = True
        #     else:
        #         t= False
        # except: 
        #     t = False

        # try:
        #     request.session['Misc_Materials']
        #     if request.session['Misc_Materials'] == 'on':
        #         u = True
        #     else:
        #         u= False
        # except: 
        #     u = False

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
            request.session['Stairs_skirting']
            if request.session['Stairs_skirting'] == 'on':
                StairSkirtKey = True
            else:
                StairSkirtKey= False
        except: 
            StairSkirtKey = False

        # try:
        #     request.session['Tile_floor']
        #     if request.session['Tile_floor'] == 'on':
        #         hh = True
        #     else:
        #         hh= False
        # except: 
        #     hh = False


        # try:
        #     request.session['Tile_Backsplash']
        #     if request.session['Tile_Backsplash'] == 'on':
        #         ii = True
        #     else:
        #         ii = False
        # except: 
        #     ii = False

        # try:
        #     request.session['Tile_Shower']
        #     if request.session['Tile_Shower'] == 'on':
        #         jj = True
        #     else:
        #         jj= False
        # except: 
        #     jj = False

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

        try:
            request.session['Electrical_sqft']         
        except:
            request.session['Electrical_sqft'] = "0"
        
        try:
            request.session['Panel_Location']         
        except:
            request.session['Panel_Location'] = "1"

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
            request.session['Countertop_type'] = "1"

        try:
            request.session['Countertop_sqft']         
        except:
            request.session['Countertop_sqft'] = "0"


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


        



        FramingLFofWallsKey     = request.session['Framing_LF_of_Walls']
        FramingLFofBulkheadsKey = request.session['Framing_LF_of_Bulkheads']
        HVACVentsKey            = request.session['HVAC_RSE_Vents']
        CastConnections         = request.session['No_of_connections']
        UndergroundFeetKey      = request.session['LF_of_Underground']
        ConcreteBreakKey        = request.session['Concrete_to_be_Broken']
        RoughWaterLinesKey      = request.session['Rough_In_Water_Lines']
        ElectricalAreaKey       = request.session['Electrical_sqft']
        PanelLocationKey        = request.session['Panel_Location']
        DimmerSwitchesKey       = request.session['Dimmer_Switches']
        FanInstallKey           = request.session['Fan_Install']
        InsulationAreaKey       = request.session['Insulation_sqft']
        drywallAreaKey          = request.session['Drywall_sqft']
        WallTextureKey          = request.session['Wall_Texture']
        CeilTextureKey          = request.session['Ceiling_Texture']
        DoorsKey                = request.session['No_of_doors']
        CabinetryAreaKey        = request.session['LF_of_Cabinetry']
        BaseboardAreaKey        = request.session['LF_of_baseboard']
        CasingLengthKey         = request.session['Casing_LF']
        
        PaintAreaKey            = request.session['Paint_sqft']
        NumberOfColorsKey       = request.session['add_colors']
        CountertopTypeKey       = request.session['Countertop_type']
        CountertopAreaKey       = request.session['Countertop_sqft']
        BacksplashAreaKey       = request.session['Tile_Backsplash_sqft']
        BathTypeKey             = request.session['BathType']
        ShowerPanAreaKey        = request.session['Shower_Pan_sqft']
        WallTileAreaKey         = request.session['Wall_Tile_sqft']
        NichesKey               = request.session['Niches']
        
        
        FloorAreaKey            = request.session['Floor_sqft']
        FloorTileAreaKey        = request.session['Floor_Tile_sqft']
        CarpetAreaKey           = request.session['Carpet_sqft']
        BathAllowanceTypeKey    = request.session['Bathroom_Allowance_items_type']
        BarAllowanceTypeKey     = request.session['Bar_Allowance_items_type']
        FinalInstallKey         = request.session['Final_install']
        MiscMatrialValueKey     = request.session['Misc_Materials_val']

        


#save Customer Details
        cust = Customer()
       
        cust.projectManager_id = request.user.id
        cust.customerID = request.session['customerID']
        cust.customerName = request.session['customerName']
        cust.customerContact = request.session['customerContact']
        cust.customerEmail = request.session['customerEmail']
        
        cust.customerAddress = request.session['customerAddress']
        cust.save()
        abc = cust.pk
        
        
#save Boolean Values
        bools = BooleansTable()

        bools.customerID = Customer.objects.get(pk = abc)
        bools.Permit = a               
        bools.Dumpster = b   
        bools.Year_old       = HouseOldKey
        bools.Customer_Ease  = CustomerEaseKey            
        # bools.Framing = c                 
        # bools.HVAC =  d                  
        # bools.Plumbing_Rough = e         
        # bools.Plumbing_Final = f         
        # bools.Electrical_Rough = g       
        # bools.Electrical_Final = h       
        # bools.Insulation = i            
        # bools.Drywall =  j               
        # bools.Trim =  k                  
        # bools.Painting =   l             
        # bools.Cabinetry =  m             
        # bools.Countertops =  n           
        # bools.Tile =  o                  
        # bools.Flooring = p                
        # bools.Carpet =   q               
        # bools.Bathroom_Allowance = r     
        # bools.Bar_Allowances =  s        
        # bools.Final_Install_Punch_List = t
        # bools.Misc_Materials = u

        bools.save()

     
#SAve Framing Details

        Fram = FramingTable()
        Fram.customerID                 = Customer.objects.get(pk = abc)
        Fram.Framing_LF_of_Walls        = FramingLFofWallsKey
        Fram.Framing_LF_of_Bulkheads    = FramingLFofBulkheadsKey
        # fm24.customerName =request.session['customerName']
        Fram.save()

#SAve Hvac Details

        hva = HVACTable()
        hva.customerID              = Customer.objects.get(pk = abc)        
        hva.HVAC_RSE_Vents             = HVACVentsKey
        # fm24.customerName =request.session['customerName']
        hva.save()

#SAve Plumbing Details

        Plumb = PlumbingTable()
        # fm24.customerName =request.session['customerName']
        Plumb.customerID                = Customer.objects.get(pk = abc)       
        Plumb.Cast_Iron_Pipe_Connection = v
        Plumb.No_of_connections = CastConnections
        Plumb.ConcreteRemoval = w
        Plumb.LF_of_Underground      = UndergroundFeetKey
        Plumb.Concrete_to_be_Broken  = ConcreteBreakKey
        Plumb.Rough_In_Water_Lines   = RoughWaterLinesKey
        Plumb.Plumbing_Correct_Location =x
        Plumb.Set_Toilet = y
        Plumb.Trim_Out_Fixtures= z
        Plumb.Vanity_Faucet = aa
        Plumb.Dishwater = bb
        Plumb.Sink = cc     
        Plumb.Refigerator_Water_Line = dd

        Plumb.save() 

#Save Electrical Details
        Elec = ElectricalTable()

        Elec.customerID                 = Customer.objects.get(pk = abc)
        Elec.Electrical_sqft            = ElectricalAreaKey
        Elec.Panel_Location             = PanelLocationKey
        Elec.Dimmer_Switches            = DimmerSwitchesKey
        Elec.Fan_Install                = FanInstallKey
        Elec.Undercabinet_Lighting      = ee
        Elec.SubPanel                   = ff

        Elec.save()
#SAve Insulation Details

        insu = InsulationTable()
        insu.customerID                 = Customer.objects.get(pk = abc)
        insu.Insulation_sqft  = InsulationAreaKey
        # fm24.customerName =request.session['customerName']
        insu.save()

#SAve Drywall Details

        dryw = DrywallTable()
        dryw.customerID                 = Customer.objects.get(pk = abc)
        dryw.Drywall_sqft               = drywallAreaKey
        dryw.Wall_Texture               = WallTextureKey
        dryw.Ceiling_Texture            = CeilTextureKey
        # fm24.customerName =request.session['customerName']
        dryw.save()

#SAve Trim Details

        tri = TrimTable()
        tri.customerID              = Customer.objects.get(pk = abc)
        tri.No_of_doors                = DoorsKey
        tri.LF_of_Cabinetry            = CabinetryAreaKey
        tri.LF_of_baseboard            = BaseboardAreaKey
        tri.Stairs_skirting            = StairSkirtKey
        tri.Casing_LF                  = CasingLengthKey
        tri.Solid_core_doors = gg
        tri.save()

#Save Paint Details
        pain = PaintTable()
        pain.customerID                 = Customer.objects.get(pk = abc)
        pain.Paint_sqft                 = PaintAreaKey
        pain.add_colors                 = NumberOfColorsKey
        pain.save()
        
#save Countertop Details
        coun = CountertopTable()

        coun.customerID                 = Customer.objects.get(pk = abc)
        coun.Countertop_type            = CountertopTypeKey
        coun.Countertop_sqft            = CountertopAreaKey

        coun.save()

#save Tile Details
        til = TileTable()

        til.customerID                  = Customer.objects.get(pk = abc)
        til.Tile_Backsplash_sqft        = BacksplashAreaKey
        til.BathType                    = BathTypeKey
        til.Shower_Pan_sqft             = ShowerPanAreaKey
        til.Wall_Tile_sqft              = WallTileAreaKey
        til.Niches                      = NichesKey

        til.save()

#Save LVP details
        floo = FloorTable()
        floo.customerID                 = Customer.objects.get(pk = abc)
        floo.Floor_sqft                 = FloorAreaKey
        floo.Floor_Tile_sqft            = FloorTileAreaKey
        floo.Carpet_sqft                = CarpetAreaKey
        floo.save()

#Save Bathallowance details
        bathallo = BathAllowanceTable()
        bathallo.customerID                 = Customer.objects.get(pk = abc)
        bathallo.Bathroom_Allowance_items_type= BathAllowanceTypeKey
        bathallo.Bathroom_Allowance_item1 = kk
        bathallo.Bathroom_Allowance_item2 = ll
        bathallo.Bathroom_Allowance_item3 = mm
        bathallo.Bathroom_Allowance_item4 = nn
        bathallo.Bathroom_Allowance_item5 = oo

        bathallo.save()  

#Save Barallowance details
        barallo = BarAllowanceTable()
        barallo.customerID              = Customer.objects.get(pk = abc)
        barallo.Bar_Allowance_items_type   = BarAllowanceTypeKey
        barallo.Bar_Allowance_item1 = pp
        barallo.Bar_Allowance_item2 = qq
        barallo.Bar_Allowance_item3 = rr
        barallo.Bar_Allowance_item4 = ss
        barallo.Bar_Allowance_item5 = tt

        bathallo.save()    

#Save Miscallowance Details
        miscallo = MiscAllowanceTable()
        miscallo.customerID                 = Customer.objects.get(pk = abc)
        miscallo.Misc_Allowance_item1 = uu
        miscallo.Misc_Allowance_item2 = vv
        miscallo.Misc_Allowance_item3 = ww
        miscallo.Misc_Allowance_item4 = xx
        miscallo.Misc_Allowance_item5 = yy

        miscallo.save() 

#save Final Details

        fina = FinalTable()
        fina.customerID                 = Customer.objects.get(pk = abc)
        fina.Final_install              = FinalInstallKey
        fina.Misc_Materials_val         = MiscMatrialValueKey
        
        fina.save()

 


        # fm24.customerName = Customer.objects.get(customerName = name)
        # fm24.Cast_Iron_Pipe_Connection = v
        # fm24.ConcreteRemoval = w
        # fm24.Plumbing_Correct_Location =x
        # fm24.save()
        messages.success(request,'Data added successfully') 
        # fm0.instance.projectManager_id = request.user.id
        # Department.objects.get(id = yourValueHere)
        
#Calculation of Final Estimate

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

#Framing Calculations

    #Framing LF of Walls
        framingWallsValue = FramingLFofWallsKey

        framingWallsMarkup = Markup.objects.only('Framing_LF_of_Walls').get(pk=1).Framing_LF_of_Walls

        framingWallsUnitPrice = Unitprice.objects.only('Framing_LF_of_Walls').get(pk=1).Framing_LF_of_Walls

        framingWallsEstimate = float(framingWallsValue)*float(framingWallsUnitPrice)*(1+float(framingWallsMarkup)/100)


    #Framing LF of BulkHeads
        framingBulkheadValue = FramingLFofBulkheadsKey

        framingBulkheadMarkup = Markup.objects.only('Framing_LF_of_Bulkheads').get(pk=1).Framing_LF_of_Bulkheads

        framingBulkheadUnitPrice = Unitprice.objects.only('Framing_LF_of_Bulkheads').get(pk=1).Framing_LF_of_Bulkheads

        framingBulkheadEstimate = float(framingBulkheadValue)*float(framingBulkheadUnitPrice)*(1+float(framingBulkheadMarkup)/100)

# TOTAL FRAMING ESTIMATE 

        totalFramingEstimate = framingWallsEstimate + framingBulkheadEstimate
     
     
     
#HVAC

        hvacValue = HVACVentsKey

        hvacMarkup = Markup.objects.only('HVAC_RSE_Vents').get(pk=1).HVAC_RSE_Vents

        hvacUnitPrice = Unitprice.objects.only('HVAC_RSE_Vents').get(pk=1).HVAC_RSE_Vents

        hvacEstimate = float(hvacValue)*float(hvacUnitPrice)*(1+float(hvacMarkup)/100)


# TOTAL HVAC ESTIMATE 

        totalHvacEstimate = hvacEstimate



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
        
#Electrical 

#Electrical sq ft
        electricalSqftValue = ElectricalAreaKey

        panelLocationPrice = Unitprice.objects.only('Panel_Location').get(pk =1).Panel_Location
       
        panelLocationMarkup = Markup.objects.only('Panel_Location').get(pk =1).Panel_Location

        electricalSqftPrice = Unitprice.objects.only('Electrical_sqft').get(pk =1).Electrical_sqft
    
        electricalSqftMarkup = Markup.objects.only('Electrical_sqft').get(pk=1).Electrical_sqft

        electricalSqftEstimate = float(electricalSqftValue)*float(electricalSqftPrice)*float((1+electricalSqftMarkup/100))
        

        if PanelLocationKey == "2":

            electricalSqftEstimate = electricalSqftEstimate + panelLocationPrice*float((1+panelLocationMarkup/100))
        else:
            electricalSqftEstimate = electricalSqftEstimate
        


#DimmerSwitch 
        dimmerSwitchValue = DimmerSwitchesKey

        dimmerSwitchMarkup = Markup.objects.only('Dimmer_Switches').get(pk=1).Dimmer_Switches

        dimmerSwitchPrice = Unitprice.objects.only('Dimmer_Switches').get(pk=1).Dimmer_Switches

        dimmerSwitchEstimate = float(dimmerSwitchValue)*float(dimmerSwitchPrice)*(1+float(dimmerSwitchMarkup)/100)



#UnderCabinetLighting

        underCabinetLightingPrice = 0
        if ee == True:
            underCabinetLightingPrice = Unitprice.objects.only('Undercabinet_Lighting').get(pk =1).Undercabinet_Lighting
        else:
            underCabinetLightingPrice = 0
        

        underCabinetLightingMarkup = Markup.objects.only('Undercabinet_Lighting').get(pk=1).Undercabinet_Lighting

        underCabinetLightingEstimate = float(underCabinetLightingPrice)*(1+float(underCabinetLightingMarkup)/100)
        
        
#subpanel

        subpanelPrice = 0
        if ff == True:
            subpanelPrice = Unitprice.objects.only('SubPanel').get(pk =1).SubPanel
        else:
            subpanelPrice = 0
        

        subpanelMarkup = Markup.objects.only('SubPanel').get(pk=1).SubPanel

        subpanelEstimate = subpanelPrice*(1+subpanelMarkup/100)
        
#Fans 
        fanInstallValue = FanInstallKey

        fanInstallMarkup = Markup.objects.only('Fan_Install').get(pk=1).Fan_Install

        fanInstallPrice = Unitprice.objects.only('Fan_Install').get(pk=1).Fan_Install

        fanInstallEstimate = float(fanInstallValue)*float(fanInstallPrice)*(1+float(fanInstallMarkup)/100)
       
### TOTAL ELECTRICAL ESTIMATE 

        totalElectricalEstimate = (electricalSqftEstimate+
                                    dimmerSwitchEstimate +
                                    underCabinetLightingEstimate +
                                    subpanelEstimate + 
                                    fanInstallEstimate)        



#Insulation
 
        insulationAreaValue = InsulationAreaKey

        insulationAreaMarkup = Markup.objects.only('Insulation_sqft').get(pk=1).Insulation_sqft

        insulationAreaPrice = Unitprice.objects.only('Insulation_sqft').get(pk=1).Insulation_sqft

        insulationAreaEstimate = float(insulationAreaValue)*float(insulationAreaPrice)*(1+float(insulationAreaMarkup)/100)



### TOTAL INSULATION ESTIMATE 

        totalInsulationEstimate = insulationAreaEstimate


#Drywall

        drywallAreaValue = drywallAreaKey

        drywallAreaMarkup = Markup.objects.only('Drywall_sqft').get(pk=1).Drywall_sqft

        drywallAreaPrice = Unitprice.objects.only('Drywall_sqft').get(pk=1).Drywall_sqft

        drywallAreaEstimate = float(drywallAreaValue)*float(drywallAreaPrice)*(1+float(drywallAreaMarkup)/100)

### TOTAL DRYWALL ESTIMATE 

        totalDrywallEstimate = drywallAreaEstimate


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


#Countertop Estimate


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


### TOTAL ESTIMATE

        totalEstimate = (totalPermitEstimate +
        totalDumpsterEstimate +
        totalFramingEstimate +
        totalHvacEstimate +
        totalPlumbingEstimate +
        totalElectricalEstimate +
        totalInsulationEstimate +
        totalDrywallEstimate +
        totalTrimEstimate +
        totalPaintEstimate +
        totalCountertopEstimate +
        totalTileEstimate + 
        totalFloorEstimate 
        
        )

        if HouseOldKey == True:
            totalEstimate = totalEstimate*1.1
        else:
            totalEstimate = totalEstimate

        if CustomerEaseKey == True:
            totalEstimate = totalEstimate*1.05
        else:
            totalEstimate = totalEstimate



        return render(request, 'final.html',{'Estimate':totalEstimate,
        'Permit':totalPermitEstimate,
        'Dumpster':totalDumpsterEstimate,
        'Framing':totalFramingEstimate,
        'HVAC': totalHvacEstimate,
        'Plumbing': totalPlumbingEstimate,
        'Electrical': totalElectricalEstimate,
        'Insulation': totalInsulationEstimate,
        'Drywall': totalDrywallEstimate,
        'Trim': totalTrimEstimate,
        'Paint': totalPaintEstimate,
        'Countertop': totalCountertopEstimate,
        'Floor': totalFloorEstimate,
        'Carpet': totalCarpetEstimate

        })
        return HttpResponse(totalEstimate)

#Final Estimate
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

