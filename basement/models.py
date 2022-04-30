from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TIER_CHOICES =(
    ("1", "Tier 1"),
    ("2", "Tier 2"),
    ("3", "Tier 3"),
    ("4", "None"),
)

countertopChoice =(
    ("1", "Granite"),
    ("2", "Quartz"),
    ("3", "ButcherBlock"),
    
)
WallTextureChoice =(
    ("1", "Orange Peel"),
    ("2", "Others"),
    ("3", "None"),
      
)
CeilTextureChoice =(
    ("1", "Knockdown"),
    ("2", "Others"),
    ("3", "None"),   
)

PanelChoice =(
    ("1", "Basement"),
    ("2", "Garage"),
)

class Customer(models.Model):
    #Customer Details
    projectManager = models.ForeignKey(User, on_delete=models.CASCADE)
    customerName = models.CharField(max_length=100,null=True)
    customerAddress = models.CharField(max_length=100,null=True)
    customerContact = models.CharField(max_length=100,null=True)
    customerEmail = models.EmailField(null=True)
    #Boolean Fields
    Permit = models.BooleanField(default=False)
    Dumpster = models.BooleanField(default=False)
    Framing = models.BooleanField(default=False)
    HVAC = models.BooleanField(default=False)
    Plumbing_Rough = models.BooleanField(default=False)
    Plumbing_Final = models.BooleanField(default=False)
    Electrical_Rough = models.BooleanField(default=False)
    Electrical_Final = models.BooleanField(default=False)
    Insulation = models.BooleanField(default=False)
    Drywall = models.BooleanField(default=False)
    Trim = models.BooleanField(default=False)
    Painting = models.BooleanField(default=False)
    Cabinetry = models.BooleanField(default=False)
    Countertops = models.BooleanField(default=False)
    Tile = models.BooleanField(default=False)
    Flooring = models.BooleanField(default=False)
    Carpet = models.BooleanField(default=False)
    Bathroom_Allowance = models.BooleanField(default=False)
    Bar_Allowances = models.BooleanField(default=False)
    Final_Install_Punch_List = models.BooleanField(default=False)
    Misc_Materials = models.BooleanField(default=False)
    #General Question
    Year_old = models.IntegerField(default=0)
    Customer_Ease = models.IntegerField(default=0)
    #Framing
    Framing_LF_of_Walls = models.IntegerField(default=0)
    Framing_LF_of_Bulkheads = models.IntegerField(default=0)
    HVAC_RSE_Vents = models.IntegerField(default=0)
    #Plumbing   
    Cast_Iron_Pipe_Connection = models.BooleanField(default=False)
    ConcreteRemoval = models.BooleanField(default=False)
    Plumbing_Correct_Location = models.BooleanField(default=False)
    LF_of_Underground = models.IntegerField(default=0)    
    Concrete_to_be_Broken =  models.IntegerField(default=0)
    Rough_In_Water_Lines = models.IntegerField(default=0)
    #Plumbing Option
    Set_Toilet =  models.BooleanField(default=False)
    Trim_Out_Fixtures =  models.BooleanField(default=False)
    Vanity_Faucet = models.BooleanField(default=False)
    #Bar Addition
    Dishwater =  models.BooleanField(default=False)
    Sink =  models.BooleanField(default=False)
    Refigerator_Water_Line =  models.BooleanField(default=False)
    #Electrical
    Electrical_sqft =   models.IntegerField(default=0)
    Panel_Location =  models.CharField(choices = PanelChoice,default= 1, max_length=100,null=True)
    Dimmer_Switches =   models.IntegerField(default=0)
    Undercabinet_Lighting =  models.BooleanField(default=False)
    SubPanel =  models.BooleanField(default=False)
    Fan_Install =   models.IntegerField(default=0)
    #Insulation
    Insulation_sqft =  models.IntegerField(default=0)
    #Drywall
    Drywall_sqft =  models.IntegerField(default=0)
    Wall_Texture = models.CharField(choices = WallTextureChoice, default= 3, max_length=20)
    Ceiling_Texture = models.CharField(choices = CeilTextureChoice, default= 3, max_length=20)
    #Trim
    No_of_doors =  models.IntegerField(default=0)
    LF_of_Cabinetry =  models.IntegerField(default=0)
    LF_of_baseboard =  models.IntegerField(default=0)
    Casing_LF =  models.IntegerField(default=0)
    Solid_core_doors = models.BooleanField(default=False)
    #Painting
    Paint_sqft =  models.IntegerField(default=0)
    add_colors =  models.IntegerField(default=0)
    #Countertops   
    Countertop_type =  models.CharField(choices = countertopChoice, default= 1, max_length=20)
    Countertop_sqft =  models.PositiveIntegerField(default=0)
    #Tile
    Tile_floor =  models.BooleanField(default=False)
    Tile_Backsplash =  models.BooleanField(default=False)
    Tile_Shower =  models.BooleanField(default=False)
    #Tile Area
    Tile_floor_sqft = models.PositiveIntegerField(default=0)
    Tile_Backsplash_sqft = models.PositiveIntegerField(default=0)
    Tile_Shower_sqft =models.PositiveIntegerField(default=0)
    #Flooring
    Floor_sqft = models.PositiveIntegerField(default=0)
    #Carpet
    Carpet_sqft = models.PositiveIntegerField(default=0)
    #Bathroom_Allowance_items 
    Bathroom_Allowance_items_type = models.CharField(choices = TIER_CHOICES, default= 4, max_length=20)
    Bathroom_Allowance_item1 = models.BooleanField(default=False)
    Bathroom_Allowance_item2 = models.BooleanField(default=False)
    Bathroom_Allowance_item3 = models.BooleanField(default=False)
    Bathroom_Allowance_item4 = models.BooleanField(default=False)
    Bathroom_Allowance_item5 = models.BooleanField(default=False)
    #Bar_Allowance_items 
    Bar_Allowance_items_type =  models.CharField(choices = TIER_CHOICES, default= 4, max_length=20)
    Bar_Allowance_item1 = models.BooleanField(default=False)
    Bar_Allowance_item2 = models.BooleanField(default=False)
    Bar_Allowance_item3 = models.BooleanField(default=False)
    Bar_Allowance_item4 = models.BooleanField(default=False)
    Bar_Allowance_item5 = models.BooleanField(default=False)
    #Misc_Allowance_items 
    Misc_Allowance_item1 = models.BooleanField(default=False)
    Misc_Allowance_item2 = models.BooleanField(default=False)
    Misc_Allowance_item3 = models.BooleanField(default=False)
    Misc_Allowance_item4 = models.BooleanField(default=False)
    Misc_Allowance_item5 = models.BooleanField(default=False)
    Misc_Allowance_item1_no = models.PositiveIntegerField(default=0)
    Misc_Allowance_item2_no = models.PositiveIntegerField(default=0)
    Misc_Allowance_item3_no = models.PositiveIntegerField(default=0)
    Misc_Allowance_item4_no = models.PositiveIntegerField(default=0)
    Misc_Allowance_item5_no = models.PositiveIntegerField(default=0)
    #Final Install
    Final_install =  models.PositiveIntegerField(default=0)
    Misc_Materials_val = models.PositiveIntegerField(default=0)



    def __str__(self):
            return self.customerName
    class Meta:
            ordering = ['customerName']


    

class Markup(models.Model):
    Permit = models.PositiveIntegerField(default=50)
    Dumpster = models.PositiveIntegerField(default=50)
    Framing = models.PositiveIntegerField(default=50)
    HVAC = models.PositiveIntegerField(default=50)
    Plumbing_Rough = models.PositiveIntegerField(default=50)
    Plumbing_Final = models.PositiveIntegerField(default=50)
    Electrical_Rough = models.PositiveIntegerField(default=50)
    Electrical_Final = models.PositiveIntegerField(default=50)
    Insulation = models.PositiveIntegerField(default=50)
    Drywall = models.PositiveIntegerField(default=50)
    Trim = models.PositiveIntegerField(default=50)
    Painting = models.PositiveIntegerField(default=50)
    Cabinetry = models.PositiveIntegerField(default=50)
    Countertops = models.PositiveIntegerField(default=50)
    Tile = models.PositiveIntegerField(default=50)
    Flooring = models.PositiveIntegerField(default=50)
    Carpet = models.PositiveIntegerField(default=50)
    Bathroom_Allowance = models.PositiveIntegerField(default=50)
    Bar_Allowances = models.PositiveIntegerField(default=50)
    Final_Install_Punch_List = models.PositiveIntegerField(default=50)
    Misc_Materials = models.PositiveIntegerField(default=50)

    def __str__(self):
            return self.Permit
    class Meta:
            ordering = ['Permit']



class Unitprice(models.Model):
    Permit = models.PositiveIntegerField(default=50)
    Dumpster = models.PositiveIntegerField(default=50)
    Framing = models.PositiveIntegerField(default=50)
    HVAC = models.PositiveIntegerField(default=50)
    Plumbing_Rough = models.PositiveIntegerField(default=50)
    Plumbing_Final = models.PositiveIntegerField(default=50)
    Electrical_Rough = models.PositiveIntegerField(default=50)
    Electrical_Final = models.PositiveIntegerField(default=50)
    Insulation = models.PositiveIntegerField(default=50)
    Drywall = models.PositiveIntegerField(default=50)
    Trim = models.PositiveIntegerField(default=50)
    Painting = models.PositiveIntegerField(default=50)
    Cabinetry = models.PositiveIntegerField(default=50)
    Countertops = models.PositiveIntegerField(default=50)
    Tile = models.PositiveIntegerField(default=50)
    Flooring = models.PositiveIntegerField(default=50)
    Carpet = models.PositiveIntegerField(default=50)
    Bathroom_Allowance = models.PositiveIntegerField(default=50)
    Bar_Allowances = models.PositiveIntegerField(default=50)
    Final_Install_Punch_List = models.PositiveIntegerField(default=50)
    Misc_Materials = models.PositiveIntegerField(default=50)

    def __str__(self):
            return self.Permit
    class Meta:
            ordering = ['Permit']
