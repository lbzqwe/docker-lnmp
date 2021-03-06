"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.http import *
import  app.views

urlpatterns = [
    url(r'^admin/', app.views.test),
]
# handler404 = 'mysite.views.my_custom_page_not_found_view'
# HttpResponseNotFound,
# handler500 = 'mysite.views.my_custom_error_view'
# HttpResponseServerError,
# handler403 = 'mysite.views.my_custom_permission_denied_view'
# HttpResponseForbidden,
# handler400 = 'mysite.views.my_custom_bad_request_view'
# HttpResponseBadRequest