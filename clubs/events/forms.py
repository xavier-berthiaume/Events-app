from django import forms
from django.forms import ModelForm
from .models import Venue

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address') # "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'address': ,
            'zip_code': ,
            'phone': ,
            'web': ,
            'email_address': ,
        }
