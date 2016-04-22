"""
Changes URL module
"""
from django.conf.urls import patterns, url

from board import views


urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),

)
