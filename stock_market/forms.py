from django import forms
from stock_market import models

class StockForm(forms.ModelForm):
    
    class Meta:
        model = models.Stock
        fields = '__all__'