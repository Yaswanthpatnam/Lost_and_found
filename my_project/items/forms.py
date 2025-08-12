from django import forms
from .models import FoundItem,CATEGORY_CHOICES,LOCATION_CHOICES

        
class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = [ 'category','title','description','location','contact_info', 'image']
        
class LostSearchForm(forms.Form):
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'})
    )
    location = forms.ChoiceField(
        choices=LOCATION_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'})
    )
    thing_name = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
    date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type':'date','class':'form-control'})
    )
    time = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={'type': 'time','class':'form-control'})
        )
        
        