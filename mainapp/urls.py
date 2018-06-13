from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'delete/(?P<id>[-\w]+)', views.delete,name='delete'),
    url(r'add', views.add,name='add'),
    url(r'update/(?P<id>[-\w]+)', views.update,name='update'),
    url(r'(?P<isbn>[-\w]+)', views.isbn,name='isbn'),
]