from urllib import request
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.http import HttpResponseServerError,HttpResponseForbidden
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect

#HttpResponseBadRequest - 400
#HttpResponseForbidden - 403
#HttpResponseNotFound - 404
#HttpResponseServerError - 500

data_db = [
    {'id': 1, 'FIO': 'none', 'interesting': 'what'},
    {'id': 2, 'FIO': 'of', 'interesting': 'me'},
    {'id': 3, 'FIO': 'me', 'interesting': 'date'},
]

def index(request):
    if (request.GET):
        print(request.GET)
    data = {'Title': 'Главная стр.'}
    return render(request, 'women/index.html', context=data)
    return HttpResponse('Главная страница women')


def categories(request):
    return HttpResponse('<h1>Привет!</h1>')


def categories_id(request, catid):
    if int(catid) > 30:
        raise Http404()
    return HttpResponse(f'<h1>Статьи по номерам {catid} </h1>')


def categories_sl(request, catid):
    return HttpResponse(f'<h1>Статьи по номерам и названию {catid} </h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ошибка 404() - Статья не найдена!</h1>')


def pageForbidden(request, exception):
    return HttpResponseForbidden('<h1>Ошибка 403() - Доступ запрещён!</h1>')


def pageBadRequest(request, exception):
    return HttpResponseBadRequest('<h1>Ошибка 400() - Неверный запрос!</h1>')


def pageServerError(exception):
    return HttpResponseServerError('<h1>Ошибка 500() - Ошибка сервера!</h1>')


def redirect_view(request):
    responce = redirect('/women/cat')
    return responce
