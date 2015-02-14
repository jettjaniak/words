from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from app.views import TranslationListView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^translations/$', TranslationListView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
