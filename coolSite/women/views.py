from urllib import request

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def index(requests):
    if (request.GET):
        print(request.GET)
    return HttpResponse('Главная страница women')


def categories(requests):
    return HttpResponse('<h1>Привет!</h1>')


def categories_id(requests, catid):
    if int(catid) > 30:
        raise Http404()
    return HttpResponse(f'<h1>Статьи по номерам {catid} </h1>')


def categories_sl(requests, catid):
    return HttpResponse(f'<h1>Статьи по номерам и названию {catid} </h1>')


def pageNotFound(requests, exception):
    return HttpResponseNotFound(f'<h1>Ошибка! Статья не найдена!</h1>')
