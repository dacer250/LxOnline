# encoding=utf-8
from django.conf.urls import url

from .views import CourseListView, CourseDetailView, CourseInfoView, CourseCommentView

urlpatterns = [
    # 课程列表页
    url(r'list/$', CourseListView.as_view(), name='course_list'),
    # 课程详情页、信息页、评论页
    url(r'detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),
    url(r'info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course_info'),
    url(r'comment/(?P<course_id>\d+)/$', CourseCommentView.as_view(), name='course_comment'),

    # url(r'courses/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='org_courses'),
    # url(r'teachers/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='org_teachers'),
    # url(r'desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name='org_desc'),
    # # 收藏课程机构
    # url(r'fav_course_org/$', OrgFavView.as_view(), name='org_fav'),


]

