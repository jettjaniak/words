from django import forms
from django.views.generic import ListView, FormView
from app.models import Translation, Word, Language


class TranslationListView(ListView):
    model = Translation
    template_name = 'translation_list.html'


class TranslationCreateForm(forms.Form):
    # TODO: validator
    english = forms.CharField()
    polish = forms.CharField()


class TranslationCreateView(FormView):
    template_name = 'translation_create.html'
    form_class = TranslationCreateForm
    success_url = '/translation-create/'

    def form_valid(self, form):
        polish_words = form.cleaned_data['polish'].split(',')
        english_words = form.cleaned_data['english'].split(',')
        polish = Language.objects.get(code='pl')
        english = Language.objects.get(code='en')
        words_ids = []
        for p in polish_words:
            w = Word.objects.get_or_create(language=polish, word=p)[0]
            words_ids += [w.id]
        for e in english_words:
            w = Word.objects.get_or_create(language=english, word=e)[0]
            words_ids += [w.id]
        t = Translation()
        t.save()
        t.words.add(*words_ids)
        return super(TranslationCreateView, self).form_valid(form)
