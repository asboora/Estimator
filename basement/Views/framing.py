from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ..models import  FramingTable, Markup, Unitprice
from ..overview import  framingQuestion
from django.contrib import messages


def framing(request):
    
        if request.method == "POST":
            request.session['Framing_LF_of_Walls'] = request.POST.get('Framing_LF_of_Walls')
            request.session['Framing_LF_of_Bulkheads'] = request.POST.get('Framing_LF_of_Bulkheads')
            
            fm2 = framingQuestion(request.POST)
            if fm2.is_valid():
                
        #         fm2.save()
    #Framing Calculations

                try:
                    request.session['Framing_LF_of_Walls']         
                except:
                    request.session['Framing_LF_of_Walls'] = "0"

                try:
                    request.session['Framing_LF_of_Bulkheads']         
                except:
                    request.session['Framing_LF_of_Bulkheads'] = "0"  

            FramingLFofWallsKey     = request.session['Framing_LF_of_Walls']
            FramingLFofBulkheadsKey = request.session['Framing_LF_of_Bulkheads']

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
        




            return render(request, 'framing.html',{'form':fm2,'estimate':totalFramingEstimate})
        else:
            fm2 = framingQuestion()
        return render(request, 'framing.html',{'form':fm2})