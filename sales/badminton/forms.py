from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm) :
    class Meta(UserCreationForm.Meta) :
        fields = UserCreationForm.Meta.fields + ('email',)


class ProductTitleFilter(forms.Form) :
    title = forms.CharField()