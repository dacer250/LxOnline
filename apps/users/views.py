# encoding:utf-8
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.backends import ModelBackend
from django.views.generic.base import View
from django.db.models import Q

from .models import UserProfile, EmailVerifyRecord
from .forms import RegisterForm, ForgetPwdForm, ModifyPwdForm
from utils.email_send import my_send_email

# Create your views here.


class MyCustomBackend(ModelBackend):
    def authenticate(self, user=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=user) | Q(email=user))
        except Exception as e:
            return None
        else:
            if user.check_password(password):
                return user
            else:
                return None

    def get_user(self, user_id):
        try:
            user = UserProfile.objects.get(id=user_id)
        except Exception as e:
            return None
        else:
            return user


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = request.POST.get('user', '')
        password = request.POST.get('password', '')
        user = authenticate(user=user, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'msg': u'用户未激活'})
        else:
            return render(request, 'login.html', {'msg': u'用户名或密码错误'})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')

            try:
                UserProfile.objects.get(email=email)
            except Exception as e:
                user = UserProfile()
                user.username = email
                user.email = email
                user.set_password(password)
                user.is_active = False
                user.save()

                my_send_email(email, 'register')
                return render(request, 'index.html')
            else:
                return render(request, 'register.html',
                              {'register_form': register_form, 'msg': u'Email已注册'})

        else:
            return render(request, 'register.html', {'register_form': register_form})


class ActiveUserView(View):
    def get(self, request, active_code):
        try:
            record = EmailVerifyRecord.objects.get(code=active_code)
        except Exception as e:
            return render(request, 'index.html')
        else:
            email = record.email
            user = UserProfile.objects.get(email=email)
            user.is_active = True
            user.save()
            return render(request, 'index.html')


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetPwdForm()
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetPwdForm(request.POST)
        if forget_form.is_valid():
            my_send_email(request.POST.get('email'), send_type='forget')
            return render(request, 'index.html')
        else:
            return render(request, 'forgetpwd.html')


class ResetPwdView(View):
    def get(self, request, reset_code):
        try:
            record = EmailVerifyRecord.objects.get(code=reset_code)
        except Exception as e:
            return render(request, 'index.html')
        else:
            email = record.email
            return render(request, 'password_reset.html', {'email': email})


class ModifyPwdView(View):
    def post(self, request):
        modify_pwd_form = ModifyPwdForm(request.POST)
        if modify_pwd_form.is_valid():
            email = modify_pwd_form.cleaned_data.get('email')
            pwd1 = modify_pwd_form.cleaned_data.get('password1')
            pwd2 = modify_pwd_form.cleaned_data.get('password2')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'msg': u'密码不一致'})
            user = UserProfile.objects.get(email=email)
            user.set_password(pwd1)
            user.save()
            return render(request, 'login.html')
        else:
            return render(request, 'password_reset.html', {'modify_pwd_form': modify_pwd_form})


def user_logout(request):
    logout(request)
    return render(request, 'index.html')
