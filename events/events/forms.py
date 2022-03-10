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