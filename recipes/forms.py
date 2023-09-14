from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList


from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Recipe name"}), help_text='This is your help  ')
    # description = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # django-crispy-forms
        for field in self.fields:
            print(field)
            new_data = {
                "placeholder": f'Recipe {str(field)}',
                "class": 'form-control',
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )
        # self.fields['name'].label = ''
        self.fields['description'].widget.attrs.update({'rows': '2'})
        self.fields['directions'].widget.attrs.update({'rows': '4'})


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity', 'unit']
