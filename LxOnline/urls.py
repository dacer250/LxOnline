# encoding=utf-8
"""LxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static
import xadmin
import captcha

from apps.users.views import LoginView, RegisterView, ActiveUserView, \
    ForgetPwdView, ResetPwdView, ModifyPwdView, user_logout

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^captcha/', include('captcha.urls')),

    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='active'),
    url(r'^forget_pwd/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^reset_pwd/(?P<reset_code>.*)/$', ResetPwdView.as_view(), name='reset_pwd'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),

    # 课程机构相关urls
    url(r'^org/', include('apps.organization.urls', namespace='org')),

    # 课程相关urls
    url(r'^course/', include('apps.courses.urls', namespace='course')),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
