from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from app.views import TranslationListView, TranslationCreateView, AjaxWordsView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^(?P<lang1>[a-z]{2})-(?P<lang2>[a-z]{2})/translations/$', TranslationListView.as_view()),
    url(r'^(?P<lang1>[a-z]{2})-(?P<lang2>[a-z]{2})/translation-create/$', TranslationCreateView.as_view()),
    url(r'^ajax/words.json$', AjaxWordsView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
