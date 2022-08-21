from django import forms
from .models import product

class ProductForm(forms.modelform):
    class Meta:
        model=product
        fields='__all__'