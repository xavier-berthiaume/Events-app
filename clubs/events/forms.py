from django import forms
from django.forms import ModelForm
from .models import Venue, Event

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address') # "__all__"

        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
            'web': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Website'}),
            'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),
        }


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'manager', 'description', 'attendees')

        labels = {
            'name':'',
            'event_date':'Date of the event (YYYY-MM-DD HH:MM:SS)',
            'venue':'Select a venue',
            'manager':'Select an event manager',
            'description':'',
            'attendees':'Select attendees',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
            'event_date': forms.DateTimeInput(attrs={'class':'form-control'}),
            'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'Venue'}),
            'manager':forms.Select(attrs={'class':'form-select', 'placeholder':'Manager'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Event Description'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Attendees'}),
        }
