from asyncio import events
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from events.models import *

# create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"
        #fields = ('name', 'address'..)
        labels = {
            'name':'',
            'address': '',
            'zip_code':'',
            'phone':'',
            'web':'',
            'email_address':'',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Venue Name'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address'}),
            'zip_code':forms.TextInput(attrs={'class':'form-control','placeholder':'Enther Zip Code'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone Number'}),
            'web':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Web Address'}),
            'email_address':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}),
        }

# Create an event form
class EventForm(ModelForm):
    class Meta:
        model = Event
        #fields = "__all__"
        fields = ('name', 'event_date','venue','manager','attendees','description')
        labels = {
            'name':'',
            'event_date': '',
            'venue':'',
            'manager':'',
            'attendees':'',
            'description':'',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Event Name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Event Date'}),
            'venue':forms.Select(attrs={'class':'form-select','placeholder':'Enther Venue'}),
            'manager':forms.Select(attrs={'class':'form-select','placeholder':'Enter Manager'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-select','placeholder':'Enter attendees'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Description'}),
        }