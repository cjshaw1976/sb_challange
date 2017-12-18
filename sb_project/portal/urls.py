from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signin/$', views.customer_login, name='customer_login'),
    url(r'^signout/$', views.customer_logout, name='customer_logout'),
]
