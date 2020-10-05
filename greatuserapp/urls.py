from django.urls import path

from . import views

urlpatterns = [
    path ('', views.redirection, name="redirect"),
    path ('index', views.index, name='index'),
]
