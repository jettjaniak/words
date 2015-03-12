import json
import re
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView, View

from app import get_languages
from app.models import Translation, Word


class TranslationListView(ListView):
    model = Translation
    template_name = 'translation_list.html'


class TranslationCreateView(View):
    def get(self, request, *args, **kwargs):
        lang1, lang2 = get_languages(self.kwargs)
        return render(request, 'translation_create.html', {'lang1': lang1, 'lang2': lang2})

    def post(self, request, **kwargs):
        if all(k in request.POST for k in ('lang1_words', 'lang2_words')):
            word_objects = []
            unallowed_characters = False
            for i, lang in enumerate(get_languages(self.kwargs), start=1):
                for w in request.POST.getlist('lang%d_words' % i):
                    if re.match(r'^[\w, \'!?\-".]+$', w):
                        word_objects += [Word.objects.get_or_create(language=lang, word=w)[0]]
                    else:
                        unallowed_characters = True
                        messages.error(request, 'Unallowed characters in %s words' % lang.name)
                        break

            if not unallowed_characters:
                same_translations = Translation.objects.all()
                for w in word_objects:
                    same_translations = same_translations.filter(words=w)

                if not same_translations:
                    t = Translation()
                    t.save()
                    t.words.add(*word_objects)
                    messages.success(request, "Translation created.")
                else:
                    messages.warning(request, "Exactly the same translation already exists. Not added.")

        else:
            messages.error(request, "You need to enter words in both languages.")
        return self.get(request)


class AjaxWordsView(View):
    def get(self, request, *args, **kwargs):
        words = Word.objects.filter(word__contains=request.GET['q'], language__code=request.GET['l'])
        words_list = [{'id': w.word, 'text': w.word} for w in words]
        return HttpResponse(json.dumps(words_list), content_type="application/json")