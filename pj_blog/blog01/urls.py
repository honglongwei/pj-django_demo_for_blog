from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^acticle/(?P<title_id>[0-9]+)$', views.acticles, name='article_page'),
    url(r'^edit/(?P<title_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url(r'^edit/action$', views.edit_action, name='edit_action'),
]
