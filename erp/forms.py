from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(max_length = 60, label="Email")
    password = forms.CharField(max_length = 30, label='Password', widget = forms.PasswordInput)
