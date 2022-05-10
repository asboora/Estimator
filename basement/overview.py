


from xmlrpc.client import Boolean
from django.core import validators
from django import forms
from .models import  BarAllowanceTable,  BathAllowanceTable, BooleansTable,  CountertopTable, Customer, DrywallTable,  ElectricalTable,  FinalTable, FloorTable,  FramingTable,  HVACTable, InsulationTable,  MiscAllowanceTable,  PaintTable,  PlumbingTable, TileTable,  TrimTable
from django.utils.datastructures import MultiValueDict


     
class customerDetails(forms.ModelForm):
    
    # Varia = Customer.objects.only('customerName').get(pk=176).customerName
    customerName = forms.CharField(widget=forms.TextInput(attrs={'class':'auto-save','placeholder':'Your Name'}))
    customerAddress = forms.CharField(widget=forms.TextInput(attrs={'class':'auto-save','placeholder':'Your Address'}))
    customerContact = forms.CharField(widget=forms.TextInput(attrs={'class':'auto-save','placeholder':'Your Contact'}))
    customerEmail = forms.CharField(widget=forms.TextInput(attrs={'class':'auto-save','placeholder':'Your Email'}))
    class Meta:
        model = Customer
        fields = ['customerName','customerAddress','customerContact','customerEmail']
    # def __init__(self, data, **kwargs):
    #     initial = kwargs.get('initial', {})
    #     data = {**initial, **data}
    #     super().__init__(data, **kwargs)


class optionDetails(forms.ModelForm):
    Permit = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'auto-save'}))
    Dumpster = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'auto-save'}))
    Year_old = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'auto-save'}))
    Customer_Ease = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'auto-save'}))
    class Meta:
        model = BooleansTable
        fields = ['Permit',
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





class framingQuestion(forms.ModelForm):
    class Meta:
        model = FramingTable
        fields = [  
                    'Framing_LF_of_Walls',
                    'Framing_LF_of_Bulkheads',
                    ]

class hvacQuestion(forms.ModelForm):
    class Meta:
        model = HVACTable
        fields = [  'HVAC_RSE_Vents']


class plumbingQuestion(forms.ModelForm):
    class Meta:
        model = PlumbingTable
        fields = [     
                        'Cast_Iron_Pipe_Connection',
                        'No_of_connections',
                        'ConcreteRemoval',
                        'Concrete_to_be_Broken',
                        'Plumbing_Correct_Location',
                        'LF_of_Underground',                 
                        'Rough_In_Water_Lines',
                        'Set_Toilet',
                        'Trim_Out_Fixtures',
                        'Vanity_Faucet',
                        'Dishwater',
                        'Sink',
                        'Refigerator_Water_Line',
                        
        ]


# class plumbingQuestion1(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = [   'LF_of_Underground',                 
#                      'Rough_In_Water_Lines']

# class plumbingQuestion2(forms.ModelForm):
#     class Meta:
#         model = PlumbingTable
#         fields = [   'Set_Toilet',
#                     'Trim_Out_Fixtures',
#                     'Vanity_Faucet',
#                     'Dishwater',
#                      'Sink',
#                     'Refigerator_Water_Line',]

# class barQuestion(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = [     'Dishwater',
#                         'Sink',
#                         'Refigerator_Water_Line',]


class electricQuestion(forms.ModelForm):
    class Meta:
        model = ElectricalTable
        fields = [     'Electrical_sqft',
                        'Panel_Location',
                        'Dimmer_Switches',
                        'Undercabinet_Lighting',
                        'SubPanel',
                        'Fan_Install',
                        ]


# class electricQuestion1(forms.ModelForm):
#     class Meta:
#         model = ElectricalTable
#         fields = [      'Dimmer_Switches',
#                         'Undercabinet_Lighting',
#                         'SubPanel',
#                         'Fan_Install',]


class insulationQuestion(forms.ModelForm):
    class Meta:
        model = InsulationTable
        fields = [     'Insulation_sqft'
                      ]


class drywallQuestion(forms.ModelForm):
    class Meta:
        model = DrywallTable
        fields = ['Drywall_sqft',
    'Wall_Texture',
    'Ceiling_Texture',]

class trimQuestion(forms.ModelForm):
    class Meta:
        model = TrimTable
        fields = [ 'No_of_doors',
                    'LF_of_Cabinetry',
                    'LF_of_baseboard',
                    'Casing_LF',
                    'Stairs_skirting',
                    'Solid_core_doors']

class paintQuestion(forms.ModelForm):
    class Meta:
        model = PaintTable
        fields = ['Paint_sqft','add_colors']

class countertopQuestion(forms.ModelForm):
    class Meta:
        model = CountertopTable
        fields = [ 'Countertop_type','Countertop_sqft']

class tileQuestion(forms.ModelForm):
    class Meta:
        model = TileTable
        fields = ['Tile_Backsplash_sqft',
                    'BathType',
                    'Shower_Pan_sqft',
                    'Wall_Tile_sqft',
                    'Niches',
                    ]


# class tileQuestion1(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ['Tile_floor_sqft',
#                     'Tile_Backsplash_sqft',
#                     'Tile_Shower_sqft']



class floorQuestion(forms.ModelForm):
    class Meta:
        model = FloorTable
        fields = ['Floor_sqft','Floor_Tile_sqft','Carpet_sqft',]

# class carpetQuestion(forms.ModelForm):
#     class Meta:
#         model = FloorTable
#         fields = ['Carpet_sqft']



class bathallowQuestion(forms.ModelForm):
    class Meta:
        model = BathAllowanceTable
        
        fields = ['Bathroom_Allowance_items_type',
                'Bathroom_Allowance_item1',
                'Bathroom_Allowance_item2',
                'Bathroom_Allowance_item3',
                'Bathroom_Allowance_item4',
                'Bathroom_Allowance_item5',]


class barallowQuestion(forms.ModelForm):
    class Meta:
        model = BarAllowanceTable
        fields = ['Bar_Allowance_items_type',
                'Bar_Allowance_item1',
                'Bar_Allowance_item2',
                'Bar_Allowance_item3',
                'Bar_Allowance_item4',
                'Bar_Allowance_item5',]

class miscallowQuestion(forms.ModelForm):
    class Meta:
        model = MiscAllowanceTable
        fields = ['Misc_Allowance_item1',
                'Misc_Allowance_item2',
                'Misc_Allowance_item3',
                'Misc_Allowance_item4',
                'Misc_Allowance_item5',
                'Misc_Allowance_item1_no',
                'Misc_Allowance_item2_no',
                'Misc_Allowance_item3_no',
                'Misc_Allowance_item4_no',
                'Misc_Allowance_item5_no',]


class finalQuestion(forms.ModelForm):
    class Meta:
        model = FinalTable
        fields = [    'Final_install',
                      'Misc_Materials_val',]






