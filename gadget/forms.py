from django import forms 
from gadget.models import Gadgets

class GadgetsForm(forms.ModelForm):
    class Meta:
        model = Gadgets
        fields = '__all__'
        
