from django import forms
from django.contrib import admin
from .models import SetProduct

class SetProductForm(forms.ModelForm):
    class Meta:
        model = SetProduct
        fields = '__all__'

class SetProductInline(admin.TabularInline):
    model = SetProduct
    form = SetProductForm