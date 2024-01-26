from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Book, Author

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    
class AddRecordForm(forms.ModelForm):
    Title = forms.CharField(required=True)
    Author_Name = forms.ModelChoiceField(queryset=Author.objects.all())
    Price = forms.CharField(required=True)
    Stock = forms.CharField(required=True)
    
    class Meta:
        model = Book
        exclude = ('BookID',)


class AuthorForm(forms.ModelForm):
    Author_Name = forms.CharField(required=True)

    class Meta:
        model = Author
        fields = '__all__'
