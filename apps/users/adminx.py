# encoding:utf-8
import xadmin
from xadmin import views

from .models import UserProfile, EmailVerifyRecord, Banner
# Register your models here.


# --------------------------xadmin基本配置-----------------------------------------
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '乐学后台管理系统'
    site_footer = '乐学在线教育网'
    menu_style = 'accordion'


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
# --------------------------------------------------------------------------------


class UserProfileAdmin(object):
    list_display = ['username', 'email', 'mobile', 'date_joined']
    search_fields = ['username', 'email', 'mobile', 'address']
    list_filter = ['username', 'email', 'mobile', 'birthday', 'gender',
                   'is_staff', 'is_active', 'date_joined']


class EmailVerifyRecordAdmin(object):
    list_display = ['email', 'code', 'send_type', 'send_time']
    search_fields = ['email', 'code']
    list_filter = ['email', 'code', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'create_time']
    search_fields = ['title', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'create_time']


xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)



