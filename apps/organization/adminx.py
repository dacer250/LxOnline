import xadmin

from .models import City, CourseOrg, Teacher


class CityAdmin(object):
    list_display = ['name', 'create_time']
    search_fields = ['name', 'url', 'index']
    list_filter = ['name', 'create_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'city', 'address', 'fav_num', 'click_num', 'create_time']
    search_fields = ['name', 'city', 'address', 'fav_num', 'click_num']
    list_filter = ['name', 'city', 'address', 'fav_num', 'click_num', 'create_time']


class TeacherAdmin(object):
    list_display = ['name', 'organization', 'work_years', 'work_company', 'work_position',
                    'points', 'fav_num', 'click_num', 'create_time']
    search_fields = ['name', 'organization', 'work_years', 'work_company', 'work_position',
                     'points', 'fav_num', 'click_num']
    list_filter = ['name', 'organization', 'work_years', 'work_company', 'work_position',
                   'points', 'fav_num', 'click_num', 'create_time']


xadmin.site.register(City, CityAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)


