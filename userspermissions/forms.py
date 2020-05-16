from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from . models import CustomUser, Role, RoleProfile
from django.utils import timezone


class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=60, help_text='Enter a valid email address')

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',  'first_name', 'last_name', 'is_staff', 'is_active')


class RoleForm(forms.ModelForm):

    class Meta:
        model = Role
        fields = ('name', 'status', 'desk_access')
        
    '''def clean_created_by(self):
        if not self.cleaned_data['created_by']:
            return User()
        return self.cleaned_data['created_by']'''


class RoleProfileForm(forms.ModelForm):

    class Meta:
        model = RoleProfile
        fields = ('name', 'roles')
        widgets = {
            "roles": forms.CheckboxSelectMultiple,
        }
