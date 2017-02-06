# encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'课程名')
    desc = models.CharField(max_length=300, verbose_name=u'描述')
    detail = models.TextField(verbose_name=u'详情')
    degree = models.CharField(max_length=2, verbose_name=u'等级',
                              choices=(('cj', u'初级'), ('zj', u'中级'), ('gj', u'高级')))
    image = models.ImageField(max_length=100, upload_to='course/image/%Y/%m', verbose_name=u'封面')
    learn_time = models.IntegerField(default=0, verbose_name=u'学习时长（分钟）')
    student_num = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏人数')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name


class Chapter(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=50, verbose_name=u'章节名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name


class Video(models.Model):
    chapter = models.ForeignKey(Chapter, verbose_name=u'章节')
    name = models.CharField(max_length=50, verbose_name=u'视频名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=50, verbose_name=u'资源名')
    download_url = models.FileField(max_length=100, upload_to='course/resource/%Y/%m',
                                    verbose_name=u'资源文件')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name






















































































