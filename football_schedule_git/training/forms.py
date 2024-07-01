# from django.forms import ModelForm
# from django import forms
# from .models import Event
# import pytz

# class EventForm(ModelForm):
#     class Meta:
#         model = Event
#         fields = ['title', 'event_type', 'drills', 'date_time', 'description']
#         widgets = {
#             'calendar': forms.HiddenInput(),
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'event_type': forms.Select(attrs={'class': 'form-control'}),
#             'drills': forms.SelectMultiple(attrs={'class': 'form-control hideScroll',}),
#             'date_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
#             'description': forms.Textarea(attrs={'class': 'form-control'}),
#         }