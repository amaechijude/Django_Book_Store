from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Books, Authors

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
    
    
class AddRecordForm(forms.ModelForm):
    Title = forms.CharField(required=True)
    Authors_Name = forms.ModelChoiceField(queryset=Authors.objects.all())
    Price = forms.CharField(required=True)
    Stock = forms.CharField(required=True)
    
    class Meta:
        model = Books
        exclude = ('BookID',)


class AuthorForm(forms.ModelForm):
    Authors_Name = forms.CharField(required=True)

    class Meta:
        model = Authors
        fields = '__all__'
