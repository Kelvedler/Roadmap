from django import forms
from app_two import models


class UserInput(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'
