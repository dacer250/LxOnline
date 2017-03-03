# encoding=utf-8
from __future__ import absolute_import

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic.base import View

from .models import Course, CourseResource
from apps.operation.models import UserFavorite, UserCourse, CourseComment
from utils.paginator import object_paginator
from utils.mixin import LoginRequiredMixin

# Create your views here.


class CourseListView(View):
    """
    课程列表功能
    """
    def get(self, request):
        all_courses = Course.objects.all().order_by('-create_time')

        hot_courses = all_courses.order_by('-click_num')[:3]

        # 排序，默认根据课程添加时间，还可根据学生人数、热门程度进行排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'hot':
                all_courses = all_courses.order_by('-click_num')
            elif sort == 'student_num':
                all_courses = all_courses.order_by('-student_num')

        # 分页
        courses_page = object_paginator(request, all_courses, 2)

        return render(request, 'course-list.html', {
            'courses_page': courses_page,
            'hot_courses': hot_courses,
            'sort': sort
        })


class CourseDetailView(View):
    """
    课程详情功能
    """
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=int(course_id))

        # 课程的点击数需加一
        course.click_num += 1
        course.save()

        # 获取相关课程(根据是否有相同的标签来判断)
        tag = course.tag
        if tag:
            relate_course = Course.objects.filter(tag=tag)[:3]
        else:
            relate_course = []

        return render(request, 'course-detail.html', {
            'course': course,
            'relate_course': relate_course,
        })


class CourseInfoView(LoginRequiredMixin, View):
    """
    课程信息功能
    """
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=int(course_id))
        # 查询用户是否已经关联了该课程
        user_course = UserCourse.objects.filter(user=request.user, course=course)
        if not user_course:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()

        course_resource = CourseResource.objects.filter(course=course)
        return render(request, 'course-video.html', {
            'course': course,
            'course_resource': course_resource,
        })


class CourseCommentView(View):
    """
    课程评论功能
    """
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=int(course_id))
        course_comments = CourseComment.objects.filter(course=course)
        course_resource = CourseResource.objects.filter(course=course)
        return render(request, 'course-comment.html', {
            'course': course,
            'course_comments': course_comments,
            'course_resource': course_resource,
        })
