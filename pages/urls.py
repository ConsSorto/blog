from django.urls import path
from . import views

urlpatterns = [
    path('paginas/<str:slug>', views.page, name='page'),
]

    