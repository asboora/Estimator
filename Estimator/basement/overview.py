from django.core import validators
from django import forms
from .models import Customer



     

class customerDetails(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customerName','customerAddress','customerContact','customerEmail']



class optionDetails(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Permit',
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
    'Misc_Materials',]



class generalQuestion(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Year_old',
                'Customer_Ease']


class framingQuestion(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [  'Framing_LF_of_Walls',
                    'Framing_LF_of_Bulkheads',
                    ]

class hvacQuestion(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [  'HVAC_RSE_Vents']


class plumbingQuestion(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [     'Cast_Iron_Pipe_Connection',
                        'ConcreteRemoval',
                        'Concrete_to_be_Broken',
                        'Plumbing_Correct_Location',
                        'LF_of_Underground',                 
                     'Rough_In_Water_Lines'
                        
        ]


# class plumbingQuestion1(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = [   'LF_of_Underground',                 
#                      'Rough_In_Water_Lines']

class plumbingQuestion2(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [   'Set_Toilet',
                    'Trim_Out_Fixtures',
                    'Vanity_Faucet',
                    'Dishwater',
                     'Sink',
                    'Refigerator_Water_Line',]

# class barQuestion(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = [     'Dishwater',
#                         'Sink',
#                         'Refigerator_Water_Line',]


class electricQuestion(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [     'Electrical_sqft',
                        'Panel_Location',
                        ]


class electricQuestion1(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [      'Dimmer_Switches',
                        'Undercabinet_Lighting',
                        'SubPanel',
                        'Fan_Install',]


class insulationQuestion(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [     'Insulation_sqft'
                      ]


class drywallQuestion(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Drywall_sqft',
    'Wall_Texture',
    'Ceiling_Texture',]

class trimQuestion(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'LF_of_Cabinetry',
                    'LF_of_baseboard',
                    'Casing_LF',
                    'Solid_core_doors']

class paintQuestion(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Paint_sqft','add_colors']

class countertopQuestion(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'Countertop_type','Countertop_sqft']

class tileQuestion(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Tile_floor',
                    'Tile_Backsplash',
                    'Tile_Shower',
                    'Tile_floor_sqft',
                    'Tile_Backsplash_sqft',
                    'Tile_Shower_sqft']


# class tileQuestion1(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ['Tile_floor_sqft',
#                     'Tile_Backsplash_sqft',
#                     'Tile_Shower_sqft']



class floorQuestion(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Floor_sqft']

class carpetQuestion(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Carpet_sqft']



class bathallowQuestion(forms.ModelForm):
    class Meta:
        model = Customer
        
        fields = ['Bathroom_Allowance_items_type',
                'Bathroom_Allowance_item1',
                'Bathroom_Allowance_item2',
                'Bathroom_Allowance_item3',
                'Bathroom_Allowance_item4',
                'Bathroom_Allowance_item5',]


class barallowQuestion(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Bar_Allowance_items_type',
                'Bar_Allowance_item1',
                'Bar_Allowance_item2',
                'Bar_Allowance_item3',
                'Bar_Allowance_item4',
                'Bar_Allowance_item5',]

class miscallowQuestion(forms.ModelForm):
    class Meta:
        model = Customer
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
        model = Customer
        fields = [    'Final_install',
                      'Misc_Materials_val',]






