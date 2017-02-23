# encoding=utf-8
from django.conf.urls import url, include

from .views import OrgView, OrgHomeView, OrgCourseView, OrgTeacherView, OrgDescView, OrgFavView

urlpatterns = [
    # 课程机构列表页
    url(r'list/$', OrgView.as_view(), name='org_list'),
    # 课程机构详情页-首页、课程列表页、教师列表页、详情页
    url(r'home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
    url(r'courses/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='org_courses'),
    url(r'teachers/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='org_teachers'),
    url(r'desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name='org_desc'),
    # 收藏课程机构
    url(r'fav_course_org/$', OrgFavView.as_view(), name='org_fav'),


]

