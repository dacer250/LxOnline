# encoding:utf-8
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


def object_paginator(request, object_list, num):
    paginator = Paginator(object_list, num)
    try:
        page = paginator.page(int(request.GET.get('page', 1)))
    except (InvalidPage, EmptyPage, PageNotAnInteger):
        page = paginator.page(1)
    return page
