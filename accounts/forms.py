from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Indirizzo e-mail')
    email_confirmation = forms.EmailField(label='Conferma e-mail')
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
 
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'email_confirmation',
            'password',
            'first_name',
            'last_name',
        ]
 
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email_confirmation = self.cleaned_data.get('email_confirmation')
        if email != email_confirmation:
            raise forms.ValidationError('Sono stati inseriti due indirizzi e-mail differenti')
        email_qs = CustomUser.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('Indirizzo e-mail utilizzato')
        return super(UserRegisterForm, self).clean(*args, **kwargs)