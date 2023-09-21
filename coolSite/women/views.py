from django.http import HttpResponse
from django.shortcuts import render


def index(requests):
    return HttpResponse('Главная страница women')


def categories(requests):
    return HttpResponse('<h1>Привет!</h1>')