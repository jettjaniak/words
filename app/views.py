from django import forms
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, FormView, View
from app.models import Translation, Word, Language


def get_languages(kwargs):
    return \
        [get_object_or_404(Language, code=kwargs['lang1']), get_object_or_404(Language, code=kwargs['lang2'])]


class TranslationListView(ListView):
    model = Translation
    template_name = 'translation_list.html'


class TranslationCreateForm(forms.Form):
    # TODO: validator
    lang1_words = forms.CharField()
    lang2_words = forms.CharField()


class TranslationCreateView(View):
    form_class = TranslationCreateForm

    def get(self, request, *args, **kwargs):
        lang1, lang2 = get_languages(self.kwargs)
        return render(request, 'translation_create.html', {'lang1': lang1, 'lang2': lang2})

    def post(self, request, **kwargs):
        lang1, lang2 = get_languages(self.kwargs)
        form = self.form_class(request.POST)
        if form.is_valid():
            lang1_words = form.cleaned_data['lang1_words'].split(',')
            lang2_words = form.cleaned_data['lang2_words'].split(',')

            word_objects = []
            for w in lang1_words:
                word_objects += [Word.objects.get_or_create(language=lang1, word=w)[0]]
            for w in lang2_words:
                word_objects += [Word.objects.get_or_create(language=lang2, word=w)[0]]

            same_translations = Translation.objects.all()
            for w in word_objects:
                same_translations = same_translations.filter(words=w)

            if not same_translations:
                t = Translation()
                t.save()
                t.words.add(*word_objects)

            return self.get(request)
