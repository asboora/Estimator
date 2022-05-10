
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

BathTypeChoice =(
    ("1", "No Tiles"),
    ("2", "FiberGlass Tub"),
    ("3", "Shower Pan"),   
)
class Customer(models.Model):
    #Customer Details
    
    projectManager = models.ForeignKey(User, on_delete=models.CASCADE)
    customerID = models.AutoField(primary_key= True)
    customerName = models.CharField(max_length=100,null=True)
    customerAddress = models.CharField(max_length=100,null=True)
    customerContact = models.CharField(max_length=100,null=True)
    customerEmail = models.EmailField(null=True)
    def __str__(self):
                return self.customerName
    class Meta:
                ordering = ['customerName']
    #Boolean Fields
class BooleansTable(models.Model):
    customerID = models.OneToOneField(Customer,to_field='customerID', on_delete=models.CASCADE, primary_key= True)
    Permit = models.BooleanField(default=False, null= True)
    Dumpster = models.BooleanField(default=False)
    Year_old = models.BooleanField(default=False)
    Customer_Ease = models.BooleanField(default=False)
    # Framing = models.BooleanField(default=False)
    # HVAC = models.BooleanField(default=False)
    # Plumbing_Rough = models.BooleanField(default=False)
    # Plumbing_Final = models.BooleanField(default=False)
    # Electrical_Rough = models.BooleanField(default=False)
    # Electrical_Final = models.BooleanField(default=False)
    # Insulation = models.BooleanField(default=False)
    # Drywall = models.BooleanField(default=False)
    # Trim = models.BooleanField(default=False)
    # Painting = models.BooleanField(default=False)
    # Cabinetry = models.BooleanField(default=False)
    # Countertops = models.BooleanField(default=False)
    # Tile = models.BooleanField(default=False)
    # Flooring = models.BooleanField(default=False)
    # Carpet = models.BooleanField(default=False)
    # Bathroom_Allowance = models.BooleanField(default=False)
    # Bar_Allowances = models.BooleanField(default=False)
    # Final_Install_Punch_List = models.BooleanField(default=False)
    # Misc_Materials = models.BooleanField(default=False)
     


    #Framing
class FramingTable(models.Model):
    customerID = models.OneToOneField(Customer,to_field='customerID', on_delete=models.CASCADE, primary_key= True)
    Framing_LF_of_Walls = models.IntegerField(default=0)
    Framing_LF_of_Bulkheads = models.IntegerField(default=0)

class HVACTable(models.Model):
    customerID = models.OneToOneField(Customer,to_field='customerID', on_delete=models.CASCADE, primary_key= True)
    HVAC_RSE_Vents = models.IntegerField(default=0)
  


 

    
    
    #Electrical
class ElectricalTable(models.Model):
    customerID = models.OneToOneField(Customer,to_field='customerID', on_delete=models.CASCADE, primary_key= True)
    Electrical_sqft =   models.IntegerField(default=0)
    Panel_Location =  models.CharField(choices = PanelChoice,default= 1, max_length=100,null=True)
    Dimmer_Switches =   models.IntegerField(default=0)
    Undercabinet_Lighting =  models.BooleanField(default=False)
    SubPanel =  models.BooleanField(default=False)
    Fan_Install =   models.IntegerField(default=0)
    #Insulation
class InsulationTable(models.Model):
    customerID = models.OneToOneField(Customer,to_field='customerID', on_delete=models.CASCADE, primary_key= True)
    Insulation_sqft =  models.IntegerField(default=0)
    #Drywall
class DrywallTable(models.Model):
    customerID = models.OneToOneField(Customer,to_field='customerID', on_delete=models.CASCADE, primary_key= True)
    Drywall_sqft =  models.IntegerField(default=0)
    Wall_Texture = models.CharField(choices = WallTextureChoice, default= 3, max_length=20)
    Ceiling_Texture = models.CharField(choices = CeilTextureChoice, default= 3, max_length=20)
    #Trim
class TrimTable(models.Model):
    customerID = models.OneToOneField(Customer,to_field='customerID', on_delete=models.CASCADE, primary_key= True)
    No_of_doors =  models.FloatField(default=0)
    LF_of_Cabinetry =  models.IntegerField(default=0)
    LF_of_baseboard =  models.IntegerField(default=0)
    Casing_LF =  models.IntegerField(default=0)
    Stairs_skirting = models.BooleanField(default=False)
    Solid_core_doors = models.BooleanField(default=False)
    #Painting
class PaintTable(models.Model):
    customerID = models.OneToOneField(Customer,to_field='customerID', on_delete=models.CASCADE, primary_key= True)
    Paint_sqft =  models.IntegerField(default=0)
    add_colors =  models.IntegerField(default=0)
    #Countertops 

class CountertopTable(models.Model):  
    customerID = models.OneToOneField(Customer,to_field='customerID', on_delete=models.CASCADE, primary_key= True)
    Countertop_type =  models.CharField(choices = countertopChoice, default= 1, max_length=20)
    Countertop_sqft =  models.PositiveIntegerField(default=0)

class TileTable(models.Model):
    #Tile
    customerID = models.OneToOneField(Customer,to_field='customerID', on_delete=models.CASCADE, primary_key= True)
    Tile_Backsplash_sqft = models.PositiveIntegerField(default=0)
    BathType =  models.CharField(choices = BathTypeChoice, default= 1, max_length=20)     
    Shower_Pan_sqft =models.PositiveIntegerField(default=0)
    Wall_Tile_sqft =models.PositiveIntegerField(default=0)
    Niches = models.PositiveIntegerField(default=0)
  
    
    
    #Flooring
class FloorTable(models.Model):
    customerID = models.OneToOneField(Customer,to_field='customerID', on_delete=models.CASCADE, primary_key= True)
    Floor_sqft = models.PositiveIntegerField(default=0)
    Floor_Tile_sqft = models.PositiveIntegerField(default=0)
    #Carpet
    Carpet_sqft = models.PositiveIntegerField(default=0)
    #Bathroom_Allowance_items 
class BathAllowanceTable(models.Model):
    customerID = models.OneToOneField(Customer,to_field='customerID', on_delete=models.CASCADE, primary_key= True)
    Bathroom_Allowance_items_type = models.CharField(choices = TIER_CHOICES, default= 4, max_length=20)
    Bathroom_Allowance_item1 = models.BooleanField(default=False)
    Bathroom_Allowance_item2 = models.BooleanField(default=False)
    Bathroom_Allowance_item3 = models.BooleanField(default=False)
    Bathroom_Allowance_item4 = models.BooleanField(default=False)
    Bathroom_Allowance_item5 = models.BooleanField(default=False)
    #Bar_Allowance_items 

class BarAllowanceTable(models.Model):
    customerID = models.OneToOneField(Customer,to_field='customerID', on_delete=models.CASCADE, primary_key= True)
    Bar_Allowance_items_type =  models.CharField(choices = TIER_CHOICES, default= 4, max_length=20)
    Bar_Allowance_item1 = models.BooleanField(default=False)
    Bar_Allowance_item2 = models.BooleanField(default=False)
    Bar_Allowance_item3 = models.BooleanField(default=False)
    Bar_Allowance_item4 = models.BooleanField(default=False)
    Bar_Allowance_item5 = models.BooleanField(default=False)
    #Misc_Allowance_items 
class MiscAllowanceTable(models.Model):
    customerID = models.OneToOneField(Customer,to_field='customerID', on_delete=models.CASCADE, primary_key= True)
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
class FinalTable(models.Model):
    customerID = models.OneToOneField(Customer,to_field='customerID', on_delete=models.CASCADE, primary_key= True)
    Final_install =  models.PositiveIntegerField(default=0)
    Misc_Materials_val = models.PositiveIntegerField(default=0)



    # def __str__(self):
    #         return self.customerID
    # class Meta:
    #         ordering = ['customerID']

class PlumbingTable(models.Model):
    #Plumbing   
    customerID = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key= True)
    Cast_Iron_Pipe_Connection = models.BooleanField(default=False)
    No_of_connections = models.IntegerField(default=0)
    ConcreteRemoval = models.BooleanField(default=False)
    Plumbing_Correct_Location = models.BooleanField(default=False)
    LF_of_Underground = models.IntegerField(default=0)    
    Concrete_to_be_Broken =  models.IntegerField(default=0)
    Rough_In_Water_Lines = models.IntegerField(default=0)
    Set_Toilet =  models.BooleanField(default=False)
    Trim_Out_Fixtures =  models.BooleanField(default=False)
    Vanity_Faucet = models.BooleanField(default=False)
    #Bar Addition
    Dishwater =  models.BooleanField(default=False)
    Sink =  models.BooleanField(default=False)
    Refigerator_Water_Line =  models.BooleanField(default=False)
    

class Markup(models.Model):
    Permit                           = models.PositiveIntegerField(default=0)                    
    Dumpster                         = models.PositiveIntegerField(default=0)                  
    Framing                          = models.PositiveIntegerField(default=0)                   
    HVAC                             = models.PositiveIntegerField(default=0)                  
    Plumbing_Rough                   = models.PositiveIntegerField(default=0)                    
    Plumbing_Final                   = models.PositiveIntegerField(default=0)                    
    Electrical_Rough                 = models.PositiveIntegerField(default=0)                  
    Electrical_Final                 = models.PositiveIntegerField(default=0)                  
    Insulation                       = models.PositiveIntegerField(default=0)                    
    Drywall                          = models.PositiveIntegerField(default=0)                   
    Trim                             = models.PositiveIntegerField(default=0)                  
    Painting                         = models.PositiveIntegerField(default=0)                  
    Cabinetry                        = models.PositiveIntegerField(default=0)                 
    Countertops                      = models.PositiveIntegerField(default=0)                   
    Tile                             = models.PositiveIntegerField(default=0)                  
    Flooring                         = models.PositiveIntegerField(default=0)                  
    Carpet                           = models.PositiveIntegerField(default=0)                    
    Bathroom_Allowance               = models.PositiveIntegerField(default=0)                    
    Bar_Allowances                   = models.PositiveIntegerField(default=0)                    
    Final_Install_Punch_List         = models.PositiveIntegerField(default=0)                  
    Misc_Materials                   = models.PositiveIntegerField(default=0)                    
    Year_old                         = models.PositiveIntegerField(default=0)                  
    Customer_Ease                    = models.PositiveIntegerField(default=0)                 
    Framing_LF_of_Walls              = models.PositiveIntegerField(default=0)                   
    Framing_LF_of_Bulkheads          = models.PositiveIntegerField(default=0)                   
    HVAC_RSE_Vents                   = models.PositiveIntegerField(default=0)                    
    Cast_Iron_Pipe_Connection        = models.PositiveIntegerField(default=0)
    No_of_connections                = models.PositiveIntegerField(default=0)                 
    ConcreteRemoval                  = models.PositiveIntegerField(default=0)                   
    Plumbing_Correct_Location        = models.PositiveIntegerField(default=0)                 
    LF_of_Underground                = models.PositiveIntegerField(default=0)                           
    Concrete_to_be_Broken            = models.PositiveIntegerField(default=0)                  
    Rough_In_Water_Lines             = models.PositiveIntegerField(default=0)                  
    Set_Toilet                       = models.PositiveIntegerField(default=0)                    
    Trim_Out_Fixtures                = models.PositiveIntegerField(default=0)                 
    Vanity_Faucet                    = models.PositiveIntegerField(default=0)                 
    Dishwater                        = models.PositiveIntegerField(default=0)                 
    Sink                             = models.PositiveIntegerField(default=0)                  
    Refigerator_Water_Line           = models.PositiveIntegerField(default=0)                      
    Electrical_sqft                  = models.PositiveIntegerField(default=0)                   
    Panel_Location                   = models.PositiveIntegerField(default=0)                    
    Dimmer_Switches                  = models.PositiveIntegerField(default=0)                   
    Undercabinet_Lighting            = models.PositiveIntegerField(default=0)                 
    SubPanel                         = models.PositiveIntegerField(default=0)                  
    Fan_Install                      = models.PositiveIntegerField(default=0)                   
    Insulation_sqft                  = models.PositiveIntegerField(default=0)                   
    Drywall_sqft                     = models.PositiveIntegerField(default=0)                  
    Wall_Texture                     = models.PositiveIntegerField(default=0)                  
    Ceiling_Texture                  = models.PositiveIntegerField(default=0)                   
    No_of_doors                      = models.PositiveIntegerField(default=0)
    LF_of_Cabinetry                  = models.PositiveIntegerField(default=0)                   
    LF_of_baseboard                  = models.PositiveIntegerField(default=0)                   
    Casing_LF                        = models.PositiveIntegerField(default=0)                 
    Stairs_skirting                  = models.PositiveIntegerField(default=0)
    Solid_core_doors                 = models.PositiveIntegerField(default=0)                  
    Paint_sqft                       = models.PositiveIntegerField(default=0)                    
    add_colors                       = models.PositiveIntegerField(default=0)                    
    Countertop_type                  = models.PositiveIntegerField(default=0)                   
    Countertop_sqft                  = models.PositiveIntegerField(default=0)                   
    Tile_Backsplash_sqft             = models.PositiveIntegerField(default=0)                    
    Shower_Pan_sqft                  = models.PositiveIntegerField(default=0)                   
    Wall_Tile_sqft                   = models.PositiveIntegerField(default=0)
    Niches                           = models.PositiveIntegerField(default=0)
    FiberglassTub                    = models.PositiveIntegerField(default=0)                    
    Floor_sqft                       = models.PositiveIntegerField(default=0)                    
    Floor_Tile_sqft                  = models.PositiveIntegerField(default=0) 
    Carpet_sqft                      = models.PositiveIntegerField(default=0)                   
    Bathroom_Allowance_items_type    = models.PositiveIntegerField(default=0)                 
    Bathroom_Allowance_item1         = models.PositiveIntegerField(default=0)                    
    Bathroom_Allowance_item2         = models.PositiveIntegerField(default=0)                   
    Bathroom_Allowance_item3         = models.PositiveIntegerField(default=0)                    
    Bathroom_Allowance_item4         = models.PositiveIntegerField(default=0)                    
    Bathroom_Allowance_item5         = models.PositiveIntegerField(default=0)                    
    Bar_Allowance_items_type         = models.PositiveIntegerField(default=0)                    
    Bar_Allowance_item1              = models.PositiveIntegerField(default=0)                   
    Bar_Allowance_item2              = models.PositiveIntegerField(default=0)                   
    Bar_Allowance_item3              = models.PositiveIntegerField(default=0)                   
    Bar_Allowance_item4              = models.PositiveIntegerField(default=0)                   
    Bar_Allowance_item5              = models.PositiveIntegerField(default=0)                   
    Misc_Allowance_item1             = models.PositiveIntegerField(default=0)                  
    Misc_Allowance_item2             = models.PositiveIntegerField(default=0)                  
    Misc_Allowance_item3             = models.PositiveIntegerField(default=0)                  
    Misc_Allowance_item4             = models.PositiveIntegerField(default=0)                  
    Misc_Allowance_item5             = models.PositiveIntegerField(default=0)                  
    Misc_Allowance_item1_no          = models.PositiveIntegerField(default=0)                    
    Misc_Allowance_item2_no          = models.PositiveIntegerField(default=0)                     
    Misc_Allowance_item3_no          = models.PositiveIntegerField(default=0)                     
    Misc_Allowance_item4_no          = models.PositiveIntegerField(default=0)                    
    Misc_Allowance_item5_no          = models.PositiveIntegerField(default=0)                    
    Final_install                    = models.PositiveIntegerField(default=0)                 
    Misc_Materials_val               = models.PositiveIntegerField(default=0)


    



class Unitprice(models.Model):
   Permit                           = models.FloatField(default=0)                    
   Dumpster                         = models.FloatField(default=0)                  
   Framing                          = models.FloatField(default=0)                   
   HVAC                             = models.FloatField(default=0)                  
   Plumbing_Rough                   = models.FloatField(default=0)                    
   Plumbing_Final                   = models.FloatField(default=0)                    
   Electrical_Rough                 = models.FloatField(default=0)                  
   Electrical_Final                 = models.FloatField(default=0)                  
   Insulation                       = models.FloatField(default=0)                    
   Drywall                          = models.FloatField(default=0)                   
   Trim                             = models.FloatField(default=0)                  
   Painting                         = models.FloatField(default=0)                  
   Cabinetry                        = models.FloatField(default=0)                 
   Countertops                      = models.FloatField(default=0)                   
   Tile                             = models.FloatField(default=0)                  
   Flooring                         = models.FloatField(default=0)                  
   Carpet                           = models.FloatField(default=0)                    
   Bathroom_Allowance               = models.FloatField(default=0)                    
   Bar_Allowances                   = models.FloatField(default=0)                    
   Final_Install_Punch_List         = models.FloatField(default=0)                  
   Misc_Materials                   = models.FloatField(default=0)                    
   Year_old                         = models.FloatField(default=0)                  
   Customer_Ease                    = models.FloatField(default=0)                 
   Framing_LF_of_Walls              = models.FloatField(default=0)                   
   Framing_LF_of_Bulkheads          = models.FloatField(default=0)                   
   HVAC_RSE_Vents                   = models.FloatField(default=0)                    
   Cast_Iron_Pipe_Connection        = models.FloatField(default=0)
   No_of_connections                = models.FloatField(default=0)                
   ConcreteRemoval                  = models.FloatField(default=0)                   
   Plumbing_Correct_Location        = models.FloatField(default=0)                 
   LF_of_Underground                = models.FloatField(default=0)                           
   Concrete_to_be_Broken            = models.FloatField(default=0)                  
   Rough_In_Water_Lines             = models.FloatField(default=0)                  
   Set_Toilet                       = models.FloatField(default=0)                    
   Trim_Out_Fixtures                = models.FloatField(default=0)                 
   Vanity_Faucet                    = models.FloatField(default=0)                 
   Dishwater                        = models.FloatField(default=0)                 
   Sink                             = models.FloatField(default=0)                  
   Refigerator_Water_Line           = models.FloatField(default=0)                      
   Electrical_sqft                  = models.FloatField(default=0)                   
   Panel_Location                   = models.FloatField(default=0)                    
   Dimmer_Switches                  = models.FloatField(default=0)                   
   Undercabinet_Lighting            = models.FloatField(default=0)                 
   SubPanel                         = models.FloatField(default=0)                  
   Fan_Install                      = models.FloatField(default=0)                   
   Insulation_sqft                  = models.FloatField(default=0)                   
   Drywall_sqft                     = models.FloatField(default=0)                  
   Wall_Texture                     = models.FloatField(default=0)                  
   Ceiling_Texture                  = models.FloatField(default=0)                   
   No_of_doors                      = models.FloatField(default=0)
   LF_of_Cabinetry                  = models.FloatField(default=0)                   
   LF_of_baseboard                  = models.FloatField(default=0)                   
   Casing_LF                        = models.FloatField(default=0)                 
   Stairs_skirting                  = models.FloatField(default=0)
   Solid_core_doors                 = models.FloatField(default=0)                  
   Paint_sqft                       = models.FloatField(default=0)                    
   add_colors                       = models.FloatField(default=0)                    
   Countertop_type_Granite          = models.FloatField(default=0)
   Countertop_type_Quartz           = models.FloatField(default=0)
   Countertop_type_Butcherblock     = models.FloatField(default=0)                   
   Countertop_sqft                  = models.FloatField(default=0)                   
   Tile_Backsplash_sqft             = models.FloatField(default=0)                    
   Shower_Pan_sqft                  = models.FloatField(default=0)                   
   Wall_Tile_sqft                   = models.FloatField(default=0)
   Niches                           = models.FloatField(default=0)
   FiberglassTub                    = models.FloatField(default=0)                    
   Floor_sqft                       = models.FloatField(default=0)                    
   Floor_Tile_sqft                  = models.FloatField(default=0)
   Carpet_sqft                      = models.FloatField(default=0)                   
   Bathroom_Allowance_items_type    = models.FloatField(default=0)                 
   Bathroom_Allowance_item1         = models.FloatField(default=0)                    
   Bathroom_Allowance_item2         = models.FloatField(default=0)                   
   Bathroom_Allowance_item3         = models.FloatField(default=0)                    
   Bathroom_Allowance_item4         = models.FloatField(default=0)                    
   Bathroom_Allowance_item5         = models.FloatField(default=0)                    
   Bar_Allowance_items_type         = models.FloatField(default=0)                    
   Bar_Allowance_item1              = models.FloatField(default=0)                   
   Bar_Allowance_item2              = models.FloatField(default=0)                   
   Bar_Allowance_item3              = models.FloatField(default=0)                   
   Bar_Allowance_item4              = models.FloatField(default=0)                   
   Bar_Allowance_item5              = models.FloatField(default=0)                   
   Misc_Allowance_item1             = models.FloatField(default=0)                  
   Misc_Allowance_item2             = models.FloatField(default=0)                  
   Misc_Allowance_item3             = models.FloatField(default=0)                  
   Misc_Allowance_item4             = models.FloatField(default=0)                  
   Misc_Allowance_item5             = models.FloatField(default=0)                  
   Misc_Allowance_item1_no          = models.FloatField(default=0)                    
   Misc_Allowance_item2_no          = models.FloatField(default=0)                     
   Misc_Allowance_item3_no          = models.FloatField(default=0)                     
   Misc_Allowance_item4_no          = models.FloatField(default=0)                    
   Misc_Allowance_item5_no          = models.FloatField(default=0)                    
   Final_install                    = models.FloatField(default=0)                 
   Misc_Materials_val               = models.FloatField(default=0) 




def __str__(self):
        return self.Permit
class Meta:
        ordering = ['Permit']
    
# def __str__(self):
    #         return self.customerID
    # class Meta:
    #         ordering = ['customerID']



