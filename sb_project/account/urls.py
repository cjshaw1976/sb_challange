from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.listAccounts, name='list_accounts'),
    url(r'^new/$', views.newAccount, name='new_account'),
    url(r'^(?P<userName>\w+)/$', views.viewAccount, name='view_account'),
    url(r'^(?P<userName>\w+)/edit/$', views.editAccount, name='edit_account'),
]
