from django.urls import path, include

from . import views
import django.contrib.auth.views

app_name = 'dbapp'
urlpatterns = [
    path('', django.contrib.auth.views.LoginView.as_view(), name='login'),
    path('dbapp', views.FilteredBeanListView.as_view(), name='table'),
]
