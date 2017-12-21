from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.totals, name='backend'),
    url(r'^logs/$', views.logs, name='backend_logs'),
]
