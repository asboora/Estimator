from django.contrib import admin
from .models import  BarAllowanceTable,  BathAllowanceTable, BooleansTable,  CountertopTable, Customer,  DrywallTable,  ElectricalTable,  FinalTable, FloorTable, FramingTable, HVACTable,  InsulationTable, Markup,  MiscAllowanceTable,  PaintTable, PlumbingTable, TileTable, TrimTable, Unitprice

# Register your models here.
@admin.register(Customer)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'projectManager',
        'customerID',
        'customerName',
        'customerAddress',
        'customerContact',
        'customerEmail',]

@admin.register(BooleansTable)
class PostAdmin(admin.ModelAdmin):
    list_display = [
    'Permit',
    'Dumpster',
    'Year_old',
    'Customer_Ease']
    # 'Framing',
    # 'HVAC',
    # 'Plumbing_Rough',
    # 'Plumbing_Final',
    # 'Electrical_Rough',
    # 'Electrical_Final',
    # 'Insulation',
    # 'Drywall',
    # 'Trim',
    # 'Painting',
    # 'Cabinetry',
    # 'Countertops',
    # 'Tile',
    # 'Flooring',
    # 'Carpet',
    # 'Bathroom_Allowance',
    # 'Bar_Allowances',
    # 'Final_Install_Punch_List',
    # 'Misc_Materials',]


    
@admin.register(FramingTable)
class PostAdmin(admin.ModelAdmin):
    list_display = [
    'Framing_LF_of_Walls',
    'Framing_LF_of_Bulkheads',]

@admin.register(HVACTable)
class PostAdmin(admin.ModelAdmin):
    list_display = [
    'HVAC_RSE_Vents',]
    # 'Cast_Iron_Pipe_Connection',
    # 'ConcreteRemoval',
    # 'Plumbing_Correct_Location',
    # 'LF_of_Underground',                 
    # 'Concrete_to_be_Broken',
    # 'Rough_In_Water_Lines',
@admin.register(ElectricalTable)
class PostAdmin(admin.ModelAdmin):
    list_display = [   
    'Electrical_sqft',
    'Panel_Location',
    'Dimmer_Switches',
    'Undercabinet_Lighting',
    'SubPanel',
    'Fan_Install',]


@admin.register(InsulationTable)
class PostAdmin(admin.ModelAdmin):
    list_display = [
    'Insulation_sqft',]

@admin.register(DrywallTable)
class PostAdmin(admin.ModelAdmin):
    list_display = [
    'Drywall_sqft',
    'Wall_Texture',
    'Ceiling_Texture',]


@admin.register(TrimTable)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'No_of_doors',
    'LF_of_Cabinetry',
    'LF_of_baseboard',
    'Casing_LF',
    'Stairs_skirting',
    'Solid_core_doors',]


@admin.register(PaintTable)
class PostAdmin(admin.ModelAdmin):
    list_display = [
    'Paint_sqft',
    'add_colors',]

@admin.register(CountertopTable)
class PostAdmin(admin.ModelAdmin):
    list_display = [
    'Countertop_type',
    'Countertop_sqft',]


@admin.register(TileTable)
class PostAdmin(admin.ModelAdmin):
    list_display = [
                    'Tile_Backsplash_sqft',
                    'BathType',
                    'Shower_Pan_sqft',
                    'Wall_Tile_sqft',
                    'Niches',
    ]


@admin.register(FloorTable)
class PostAdmin(admin.ModelAdmin):
    list_display = [
    'Floor_sqft',
    'Floor_Tile_sqft',
    'Carpet_sqft',]


@admin.register(BathAllowanceTable)
class PostAdmin(admin.ModelAdmin):
    list_display = [
    'Bathroom_Allowance_items_type',
    'Bathroom_Allowance_item1',
    'Bathroom_Allowance_item2',
    'Bathroom_Allowance_item3',
    'Bathroom_Allowance_item4',
    'Bathroom_Allowance_item5',]

@admin.register(BarAllowanceTable)
class PostAdmin(admin.ModelAdmin):
    list_display = [
    'Bar_Allowance_items_type',
    'Bar_Allowance_item1',
    'Bar_Allowance_item2',
    'Bar_Allowance_item3',
    'Bar_Allowance_item4',
    'Bar_Allowance_item5',]


@admin.register(MiscAllowanceTable)
class PostAdmin(admin.ModelAdmin):
    list_display = [
    'Misc_Allowance_item1',
    'Misc_Allowance_item2',
    'Misc_Allowance_item3',
    'Misc_Allowance_item4',
    'Misc_Allowance_item5',
    'Misc_Allowance_item1_no',
    'Misc_Allowance_item2_no',
    'Misc_Allowance_item3_no',
    'Misc_Allowance_item4_no',
    'Misc_Allowance_item5_no',]


@admin.register(FinalTable)
class PostAdmin(admin.ModelAdmin):
    list_display = [
    'Final_install',
    'Misc_Materials_val']

@admin.register(PlumbingTable)
class PostAdmin(admin.ModelAdmin):
    list_display = [

    'Cast_Iron_Pipe_Connection',
    'No_of_connections',
    'ConcreteRemoval',
    'Plumbing_Correct_Location',
    'LF_of_Underground',                 
    'Concrete_to_be_Broken',
    'Rough_In_Water_Lines',
    'Set_Toilet',
    'Trim_Out_Fixtures',
    'Vanity_Faucet',
    'Dishwater',
    'Sink',
    'Refigerator_Water_Line',]

@admin.register(Unitprice)
class PostAdmin(admin.ModelAdmin):
    list_display = [
      'Permit',
    'Dumpster',
    'Framing',
    'HVAC',
    'Plumbing_Rough',
    'Plumbing_Final',
    'Electrical_Rough',
    'Electrical_Final',
    'Insulation',
    'Drywall',
    'Trim',
    'Painting',
    'Cabinetry',
    'Countertops',
    'Tile',
    'Flooring',
    'Carpet',
    'Bathroom_Allowance',
    'Bar_Allowances',
    'Final_Install_Punch_List',
    'Misc_Materials',
    'Year_old',
    'Customer_Ease',
    'Framing_LF_of_Walls',
    'Framing_LF_of_Bulkheads',
    'HVAC_RSE_Vents',
    'Cast_Iron_Pipe_Connection',
    'No_of_connections',
    'ConcreteRemoval',
    'Plumbing_Correct_Location',
    'LF_of_Underground',                 
    'Concrete_to_be_Broken',
    'Rough_In_Water_Lines',
    'Set_Toilet',
    'Trim_Out_Fixtures',
    'Vanity_Faucet',
    'Dishwater',
    'Sink',
    'Refigerator_Water_Line',
    'Electrical_sqft',
    'Panel_Location',
    'Dimmer_Switches',
    'Undercabinet_Lighting',
    'SubPanel',
    'Fan_Install',
    'Insulation_sqft',
    'Drywall_sqft',
    'Wall_Texture',
    'Ceiling_Texture',
    'No_of_doors',
    'LF_of_Cabinetry',
    'LF_of_baseboard',
    'Casing_LF',
    'Stairs_skirting',
    'Solid_core_doors',
    'Paint_sqft',
    'add_colors',
    'Countertop_type_Granite',
    'Countertop_type_Quartz',
    'Countertop_type_Butcherblock',
    'Countertop_sqft',
    'Tile_Backsplash_sqft',
    'Shower_Pan_sqft',
    'Wall_Tile_sqft',
    'Niches',
    'FiberglassTub',
    'Floor_sqft',
    'Floor_Tile_sqft',
    'Carpet_sqft',
    'Bathroom_Allowance_items_type',
    'Bathroom_Allowance_item1',
    'Bathroom_Allowance_item2',
    'Bathroom_Allowance_item3',
    'Bathroom_Allowance_item4',
    'Bathroom_Allowance_item5',
    'Bar_Allowance_items_type',
    'Bar_Allowance_item1',
    'Bar_Allowance_item2',
    'Bar_Allowance_item3',
    'Bar_Allowance_item4',
    'Bar_Allowance_item5',
    'Misc_Allowance_item1',
    'Misc_Allowance_item2',
    'Misc_Allowance_item3',
    'Misc_Allowance_item4',
    'Misc_Allowance_item5',
    'Misc_Allowance_item1_no',
    'Misc_Allowance_item2_no',
    'Misc_Allowance_item3_no',
    'Misc_Allowance_item4_no',
    'Misc_Allowance_item5_no',
    'Final_install',
    'Misc_Materials_val']


@admin.register(Markup)
class PostAdmin(admin.ModelAdmin):
    list_display = [
       'Permit',
    'Dumpster',
    'Framing',
    'HVAC',
    'Plumbing_Rough',
    'Plumbing_Final',
    'Electrical_Rough',
    'Electrical_Final',
    'Insulation',
    'Drywall',
    'Trim',
    'Painting',
    'Cabinetry',
    'Countertops',
    'Tile',
    'Flooring',
    'Carpet',
    'Bathroom_Allowance',
    'Bar_Allowances',
    'Final_Install_Punch_List',
    'Misc_Materials',
    'Year_old',
    'Customer_Ease',
    'Framing_LF_of_Walls',
    'Framing_LF_of_Bulkheads',
    'HVAC_RSE_Vents',
    'Cast_Iron_Pipe_Connection',
    'No_of_connections',
    'ConcreteRemoval',
    'Plumbing_Correct_Location',
    'LF_of_Underground',                 
    'Concrete_to_be_Broken',
    'Rough_In_Water_Lines',
    'Set_Toilet',
    'Trim_Out_Fixtures',
    'Vanity_Faucet',
    'Dishwater',
    'Sink',
    'Refigerator_Water_Line',
    'Electrical_sqft',
    'Panel_Location',
    'Dimmer_Switches',
    'Undercabinet_Lighting',
    'SubPanel',
    'Fan_Install',
    'Insulation_sqft',
    'Drywall_sqft',
    'Wall_Texture',
    'Ceiling_Texture',
    'No_of_doors',
    'LF_of_Cabinetry',
    'LF_of_baseboard',
    'Casing_LF',
    'Stairs_skirting',
    'Solid_core_doors',
    'Paint_sqft',
    'add_colors',
    'Countertop_type',
    'Countertop_sqft',
    'Tile_Backsplash_sqft',
    'Shower_Pan_sqft',
    'Wall_Tile_sqft',
    'Niches',
    'FiberglassTub',
    'Floor_sqft',
    'Floor_Tile_sqft',
    'Carpet_sqft',
    'Bathroom_Allowance_items_type',
    'Bathroom_Allowance_item1',
    'Bathroom_Allowance_item2',
    'Bathroom_Allowance_item3',
    'Bathroom_Allowance_item4',
    'Bathroom_Allowance_item5',
    'Bar_Allowance_items_type',
    'Bar_Allowance_item1',
    'Bar_Allowance_item2',
    'Bar_Allowance_item3',
    'Bar_Allowance_item4',
    'Bar_Allowance_item5',
    'Misc_Allowance_item1',
    'Misc_Allowance_item2',
    'Misc_Allowance_item3',
    'Misc_Allowance_item4',
    'Misc_Allowance_item5',
    'Misc_Allowance_item1_no',
    'Misc_Allowance_item2_no',
    'Misc_Allowance_item3_no',
    'Misc_Allowance_item4_no',
    'Misc_Allowance_item5_no',
    'Final_install',
    'Misc_Materials_val']