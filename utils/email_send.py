# encoding:utf-8
import random

from django.core.mail import send_mail

from apps.users.models import EmailVerifyRecord
from LxOnline.settings import EMAIL_FROM


def random_str(length=8):
    str_temp = random.sample('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789', length)
    str = ''.join(str_temp)
    return str


def my_send_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    email_record.email = email
    code = random_str(16)
    email_record.code = code
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = u'乐学在线教育网激活链接'
        email_body = u'请点击下面的链接来激活你的账号：http://127.0.0.1:5000/active/{0}/'.format(code)
    elif send_type == 'forget':
        email_title = u'乐学在线教育网密码重置链接'
        email_body = u'请点击下面的链接来重置你的密码：http://127.0.0.1:5000/reset_pwd/{0}/'.format(code)

    send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    if send_status:
        pass



































