from django import forms
from . models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields= ['title', 'destination','start_date','end_date','description', 'is_public']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }