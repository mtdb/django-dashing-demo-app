# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

from dashing.utils import router

from django.views.generic.base import RedirectView

from .widgets import NewClientsWidget

router.register(NewClientsWidget, 'new_users_widget')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^dashboard/', include(router.urls), name='dashboard'),
    url(r'^$', RedirectView.as_view(url='dashboard/'), name='index')
]
