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
        exclude = ['adhaar_linked','Password','username']



class staff_form(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['city'].queryset = City.objects.none()

class register_form(forms.Form):
    Adhaar = forms.IntegerField(label='adhaar_no')
    username = forms.CharField(max_length=200,label = 'user-name')
    password = forms.CharField(max_length=200,label = 'password')


class login_form(forms.Form):
    username = forms.CharField(max_length=200,label = 'user-name')
    password = forms.CharField(max_length=200,label = 'password')
