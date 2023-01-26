from captcha.fields import CaptchaField
from django import forms

class MyForm(forms.Form):

    captcha = CaptchaField()
