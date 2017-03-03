# encoding:utf-8
import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin

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


class UserProfileAdmin(UserAdmin):
    pass


class EmailVerifyRecordAdmin(object):
    list_display = ['email', 'code', 'send_type', 'send_time']
    search_fields = ['email', 'code']
    list_filter = ['email', 'code', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'create_time']
    search_fields = ['title', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'create_time']


from django.contrib.auth.models import User
xadmin.site.unregister(User)
xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)



