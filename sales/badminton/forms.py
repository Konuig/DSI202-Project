from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class RegisterForm(UserCreationForm) :
    class Meta(UserCreationForm.Meta) :
        fields = UserCreationForm.Meta.fields + ('email',)


class ProductTitleFilter(forms.Form) :
    title = forms.CharField()
 
class Address(forms.ModelForm) :
    class Meta :
        model = Profile
        fields = "__all__"

class Payment(forms.ModelForm) :
    class Meta :
        model = Order
        fields = ['profile','items','reciept']

