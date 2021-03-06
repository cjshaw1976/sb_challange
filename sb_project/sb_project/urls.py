"""sb_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from rest_framework import routers
from account.views import CustomerViewSet, AccessLogViewSet

# Routes for API views
router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'accesslog', AccessLogViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls, namespace="api")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$', auth_views.login, name='staff_login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='staff_logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^backend/', include('backend.urls')),
    url(r'', include('portal.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
