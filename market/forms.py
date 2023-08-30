from django import forms
from .models import Listing


class SellForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('category', 'name', 'description', 'amount', 'image', 'contact_number', 'location')


class UpdateSellForm(SellForm):
    class Meta:
        model = Listing
        exclude = ('created_by', 'slug', 'created_at', 'thumbnail')
