from django.conf.urls import url
from . import views
from .models import models

urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$', views.authors),
    url(r'^authors/(?P<id>\d+)$', views.authors_num),
    url(r'^books/(?P<id>\d+)$', views.books),
    url(r'^add_book$', views.add_book),
    url(r'^add_author$', views.add_author)
    url(r'^add_here$', views.add_here)
]   