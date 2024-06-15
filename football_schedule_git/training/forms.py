from django.forms import ModelForm
from django import forms
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'event_type', 'drills', 'date', 'start_time', 'end_time', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'event_type': forms.Select(attrs={'class': 'form-control'}),
            'drills': forms.SelectMultiple(attrs={'class': 'form-control hideScroll',}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }