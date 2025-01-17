from django import forms
from .models import Route

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['name', 'cities', 'description', 'estado']
        widgets = {
            'cities': forms.Textarea(attrs={'rows': 3}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class FormRecommendationList(forms.Form):
    list = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ex: city1, city2, city3, ...'}))

class FormRecommendationOriginCity(forms.Form):
    city = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}))
    time = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 20 dias, 1 mes, 3 semanas, ...'}))

class FormRecommendationDescription(forms.Form):
    description = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': ''}))