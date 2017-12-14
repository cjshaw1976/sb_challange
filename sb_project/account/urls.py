from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.listAccounts, name='list_accounts'),
    url(r'^new/$', views.newAccount, name='new_account'),
    url(r'^(?P<user_name>\w+)/$', views.viewAccount, name='view_account'),
    url(r'^(?P<user_name>\w+)/edit/$', views.editAccount, name='edit_account'),
]
