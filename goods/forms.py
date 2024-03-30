from django import forms
from django.contrib import admin
from .models import Categories, SetProduct

class SetProductForm(forms.ModelForm):
    class Meta:
        model = SetProduct
        fields = '__all__'
class SetProductInline(admin.TabularInline):
    model = SetProduct
    form = SetProductForm



class CategoriesForm(forms.ModelForm):
    class Meta:
        model = SetProduct
        fields = '__all__'
class CategoriesInline(admin.TabularInline):
    model = Categories
    form = CategoriesForm