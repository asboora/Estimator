from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
   
from ..overview import  customerDetails
from django.contrib import messages




def addCustomer(request):
    
    
    if request.method == "POST":
        request.session['customerID'] = request.POST.get('customerID')
        request.session['customerName'] = request.POST.get('customerName')
        request.session['customerAddress'] = request.POST.get('customerAddress')
        request.session['customerContact'] = request.POST.get('customerContact')
        request.session['customerEmail'] = request.POST.get('customerEmail')

        
        fm = customerDetails(request.POST )
        fm.instance.projectManager_id = request.user.id
        if fm.is_valid():   
            messages.success(request,'customer added successfully')
            # fm.save()
            return HttpResponseRedirect('/addData/')

    else:
        fm = customerDetails()
    return render(request, 'addCustomer.html',{'form':fm})
