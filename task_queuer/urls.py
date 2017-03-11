from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^add_task', views.add_task, name='add_task'),
    url(r'^task_list$', views.task_list, name='task_list'),
    url(r'^task_query$', views.task_query, name='task_query'),
]
