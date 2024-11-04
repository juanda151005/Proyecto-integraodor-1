from .models import *
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = [
            'city',
            'general_review',
            'touristic_places_rate',
            'history_and_culture_rate',
            'gastronomy_rate',  
            'costs_rate',
            'safety_rate',
            'weather_rate'
        ]
        labels = {
            'city': 'City',
            'general_review': 'General Review',
            'touristic_places_rate': 'Touristic Places Rating',
            'history_and_culture_rate': 'History & Culture Rating',
            'gastronomy_rate': 'Gastronomy Rating',
            'costs_rate': 'Costs Rating',
            'safety_rate': 'Safety Rating',
            'weather_rate': 'Weather Rating'
        }
        widgets = {
            'general_review': forms.Textarea(attrs={'rows': 4}),
            'touristic_places_rate': forms.Select(),
            'history_and_culture_rate': forms.Select(),
            'gastronomy_rate': forms.Select(),
            'costs_rate': forms.Select(),
            'safety_rate': forms.Select(),
            'weather_rate': forms.Select(),
        }

class ReplyReviewForm(forms.ModelForm):
    class Meta:
        model = ReplyReview
        fields = ['text'] 
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu respuesta aquí...'}),
        }
