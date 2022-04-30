from django.core import validators
from django import forms
from .models import Customer
from .models import Customer

class EstimatorData(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['permit','dumpster','framing','electrical','framingSqft','framingBulkhead','electricalSqft']