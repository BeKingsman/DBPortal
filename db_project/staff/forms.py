from .models import *
from django import forms
from django.contrib.auth.models import User


class excel_form(forms.ModelForm):
   class Meta:
       model = user_excel
       fields = ['sheet']


class user_form(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = '__all__'
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['city'].queryset = City.objects.none()
