import xadmin

from .models import Course, Chapter, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'degree', 'learn_time',
                    'student_num', 'fav_num', 'click_num', 'create_time']
    search_fields = ['name', 'desc', 'degree', 'learn_time',
                     'student_num', 'fav_num', 'click_num']
    list_filter = ['name', 'desc', 'degree', 'learn_time',
                   'student_num', 'fav_num', 'click_num', 'create_time']


class ChapterAdmin(object):
    list_display = ['name', 'course', 'create_time']
    search_fields = ['name', 'course']
    list_filter = ['name', 'course__name', 'create_time']


class VideoAdmin(object):
    list_display = ['name', 'chapter', 'create_time']
    search_fields = ['name', 'chapter']
    list_filter = ['name', 'chapter__name', 'create_time']


class CourseResourceAdmin(object):
    list_display = ['name', 'course', 'download_url', 'create_time']
    search_fields = ['name', 'course', 'download_url']
    list_filter = ['name', 'course__name', 'download_url', 'create_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Chapter, ChapterAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
