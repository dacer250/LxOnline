# encoding:utf-8
from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models

from apps.organization.models import CourseOrg, Teacher

# Create your models here.


class Course(models.Model):
    organization = models.ForeignKey(CourseOrg, verbose_name=u'所属机构')
    teacher = models.ForeignKey(Teacher, null=True, blank=True, verbose_name=u'授课讲师')
    name = models.CharField(max_length=50, verbose_name=u'课程名')
    desc = models.CharField(max_length=300, verbose_name=u'描述')
    detail = models.TextField(verbose_name=u'详情')
    category = models.CharField(max_length=20, default=u'开发', verbose_name=u'种类')
    tag = models.CharField(max_length=20, default='', verbose_name=u'标签')
    degree = models.CharField(max_length=2, verbose_name=u'等级',
                              choices=(('cj', u'初级'), ('zj', u'中级'), ('gj', u'高级')))
    image = models.ImageField(max_length=100, upload_to='course/image/%Y/%m', verbose_name=u'封面')
    learn_time = models.IntegerField(default=0, verbose_name=u'学习时长（分钟）')
    student_num = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏人数')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    need_kown = models.CharField(max_length=1000, default='', verbose_name=u'课程需知')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_chapte_num(self):
        return self.chapter_set.all().count()

    def get_chaptes(self):
        return self.chapter_set.all()

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]


class Chapter(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=50, verbose_name=u'章节名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_vedios(self):
        return self.video_set.all()


class Video(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'视频名')
    url = models.CharField(max_length=100, default='', verbose_name=u'访问地址')
    learn_time = models.IntegerField(default=0, verbose_name=u'学习时长（分钟）')
    chapter = models.ForeignKey(Chapter, verbose_name=u'章节')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=50, verbose_name=u'资源名')
    download_url = models.FileField(max_length=100, upload_to='course/resource/%Y/%m',
                                    verbose_name=u'资源文件')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
