# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView, DetailView

from .views import HomeView, SpeakersView, SpeakersDetailView, ActivitiesView, AttendeeDetailView, AttendeeBadgeView, AttendeePNGView, AttendeePDFView, AttendeeReceiptView, ContentView, event

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<slug>[\w-]+)/confirmation/$', ContentView.as_view(page='confirmation'), name='confirmation'),
    url(r'^confirmation/$', ContentView.as_view(page='confirmation'), name='confirmationmail'),
    url(r'^(?P<slug>[\w-]+)/about/$', ContentView.as_view(page='about'), name='about'),
    url(r'^(?P<slug>[\w-]+)/services/$', ContentView.as_view(page='services'), name='services'),
    url(r'^(?P<slug>[\w-]+)/contact/$', ContentView.as_view(page='contact'), name='contact'),
    url(r'^(?P<slug>[\w-]+)/activities/$', ActivitiesView.as_view(), name='activities'),
    url(r'^(?P<slug>[\w-]+)/speakers/$', SpeakersView.as_view(), name='speakers'),
    url(r'^(?P<eventslug>[\w-]+)/speakers/(?P<slug>[\w-]+)/$', SpeakersDetailView.as_view(), name='speakers-detail'),
    url(r'^attendee/(?P<username>[\w.@+-]+)/$',AttendeeDetailView.as_view(), name='detail'),
    url(r'^attendee/(?P<username>[\w.@+-]+)/badge/$',AttendeeBadgeView.as_view(), name='badge'),
    url(r'^attendee/(?P<username>[\w.@+-]+)/png/$',AttendeePNGView.as_view(), name='png'),
    url(r'^attendee/(?P<username>[\w.@+-]+)/pdf/$',AttendeePDFView.as_view(), name='pdf'),
    url(r'^attendee/(?P<username>[\w.@+-]+)/receipt/$',AttendeeReceiptView.as_view(), name='receipt'),

    url(r'^(?P<slug>[\w-]+)/$', HomeView.as_view(), name='event'),
]
