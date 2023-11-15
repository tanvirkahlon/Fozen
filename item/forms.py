from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:  # Fix: Use 'Meta' with a capital 'M'
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)