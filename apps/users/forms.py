# encoding:utf-8
from django import forms
from captcha.fields import CaptchaField


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True, max_length=30)
    password = forms.CharField(required=True, max_length=50)
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True, max_length=30)
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


class ModifyPwdForm(forms.Form):
    email = forms.EmailField(required=True, max_length=30)
    password1 = forms.CharField(required=True, max_length=50)
    password2 = forms.CharField(required=True, max_length=50)
