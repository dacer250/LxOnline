# encoding=utf-8
from __future__ import absolute_import

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import View

from .models import City, CourseOrg
from apps.operation.models import UserFavorite
from utils.paginator import object_paginator

# Create your views here.


class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self, request):
        all_course_org = CourseOrg.objects.all()

        hot_course_org = all_course_org.order_by('-click_num')[:3]

        # 通过机构类别进行筛选
        category = request.GET.get('ct', '')
        if category:
            all_course_org = CourseOrg.objects.filter(category=category)

        # 通过机构所在城市进行筛选
        city_id = request.GET.get('city_id', '')
        if city_id:
            all_course_org = CourseOrg.objects.filter(city_id=int(city_id))

        # 根据学生人数或课程数进行排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_course_org = CourseOrg.objects.order_by('-student_num')
            elif sort == 'courses':
                all_course_org = CourseOrg.objects.order_by('-course_num')

        course_org_page = object_paginator(request, all_course_org, 2)

        course_org_num = all_course_org.count()

        all_city = City.objects.all()

        return render(request, 'org-list.html', {
            'course_org_page': course_org_page,
            'course_org_num': course_org_num,
            'all_city': all_city,
            'city_id': city_id,
            'category': category,
            'hot_course_org': hot_course_org,
            'sort': sort,
        })


class OrgHomeView(View):
    def get(self, request, org_id):
        current_page = 'home'
        course_org = CourseOrg.objects.get(id=int(org_id))

        has_fav = False
        if not request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=int(course_org.id), fav_type=2):
                has_fav = True

        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:2]

        return render(request, 'org-detail-home.html', {
            'course_org': course_org,
            'all_courses': all_courses,
            'all_teachers': all_teachers,
            'current_page': current_page,
            'has_fav': has_fav,
        })


class OrgCourseView(View):
    def get(self, request, org_id):
        current_page = 'courses'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()
        return render(request, 'org-detail-courses.html', {
            'course_org': course_org,
            'all_courses': all_courses,
            'current_page': current_page,
        })


class OrgTeacherView(View):
    def get(self, request, org_id):
        current_page = 'teachers'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_teachers = course_org.teacher_set.all()
        return render(request, 'org-detail-teachers.html', {
            'course_org': course_org,
            'all_teachers': all_teachers,
            'current_page': current_page,

        })


class OrgDescView(View):
    def get(self, request, org_id):
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id=int(org_id))
        return render(request, 'org-detail-desc.html', {
            'course_org': course_org,
            'current_page': current_page,

        })


class OrgFavView(View):
    '''
    用户收藏或取消收藏课程机构
    '''
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        # 判断用户是否登录
        if not request.user.is_authenticated():
            return JsonResponse({'status': 'fail', 'meg': u'用户未登录'})

        # 判断对应的收藏记录是否存在
        records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        # 若存在则表示取消收藏,若不存在则表示收藏
        if records:
            records.delete()
            return JsonResponse({'status': 'success', 'meg': u'收藏'})
        else:
            if int(fav_id) > 0 and int(fav_type) > 0:
                record = UserFavorite()
                record.user = request.user
                record.fav_id = fav_id
                record.fav_type = fav_type
                record.save()
                return JsonResponse({'status': 'success', 'meg': u'取消收藏'})
            else:
                return JsonResponse({'status': 'fail', 'meg': u'收藏失败'})







