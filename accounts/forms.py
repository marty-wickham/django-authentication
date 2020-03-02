from django import forms

class UserLoginForm(forms.Form):

    username = forms.CharField()
    # We want to render a normal text input box but we want it to be of type password 
    password = forms.CharField(widget=forms.PasswordInput)