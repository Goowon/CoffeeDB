from django.shortcuts import get_object_or_404, render
from django.views import generic
import django_tables2 as tables
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .models import Bean, BeanTable, BeanFilter
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class FilteredBeanListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    login_url = '/'
    redirect_field_name = ''
    table_class = BeanTable
    model = Bean
    template_name = "dbapp/bean_list.html"
    filterset_class = BeanFilter


