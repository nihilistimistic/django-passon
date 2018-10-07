from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    reg = forms.CharField(max_length=8, help_text='Required. Your 8 digit MNNIT registration number')
    first_name = forms.CharField(max_length=20, help_text='Required. Your First Name')
    last_name = forms.CharField(max_length=20, help_text='Required. Your Last Name')
    email = forms.EmailField(max_length=100, help_text='Required. Your Email address')
    phone_num = forms.CharField(max_length=10, help_text='Required. Your Contact number')
    address = forms.CharField(widget=forms.widgets.Textarea, max_length=200,
                              help_text='Required. Your MNNIT Hostel and Room number')

    class Meta:
        model = User
        fields = ('username', 'reg', 'first_name', 'last_name',
                  'email', 'phone_num', 'address', 'password1', 'password2', )
