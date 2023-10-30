
from django.contrib import admin
from django.urls import path, include

from women.views import pageBadRequest, pageForbidden
from women.views import pageNotFound, pageServerError, redirect_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('women/', include('women.urls')),
    path('/women/cat/29', redirect_view)
]

handler400 = pageBadRequest
handler403 = pageForbidden
handler404 = pageNotFound
handler500 = pageServerError
