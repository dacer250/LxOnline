# encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'城市名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'机构名')
    desc = models.TextField(verbose_name=u'描述')
    image = models.ImageField(max_length=100, upload_to='organization/%Y/%m',
                              verbose_name=u'封面')
    city = models.ForeignKey(City, verbose_name=u'所在城市')
    address = models.CharField(max_length=200, verbose_name=u'地址')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏数')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程机构'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    organization = models.ForeignKey(CourseOrg, verbose_name=u'所属机构')
    name = models.CharField(max_length=50, verbose_name=u'教师名')
    image = models.ImageField(max_length=100, upload_to='organization/%Y/%m',
                              verbose_name=u'封面')
    work_years = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.CharField(max_length=50, verbose_name=u'就职公司')
    work_position = models.CharField(max_length=50, verbose_name=u'公司职位')
    points = models.CharField(max_length=200, verbose_name=u'教学特点')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏数')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'教师'
        verbose_name_plural = verbose_name













