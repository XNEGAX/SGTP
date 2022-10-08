from django import forms 
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2','required':'required','autofocus':True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-2 mr-sm-2','required':'required'})) 
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)