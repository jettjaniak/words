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
            languages = get_languages(self.kwargs)
            for i, lang in enumerate(languages, start=1):
                for w in request.POST.getlist('lang%d_words' % i):
                    if re.match(r'^[\w, \'!?\-".]+$', w):
                        # TODO: exclude underscore
                        word_object = Word.objects.get_or_create(language=lang, word=w)[0]
                        elementary_words_list = w.strip(',!?".').split(' ')
                        # if first letter is entire word (not elementary) is capital,
                        # lower it (in elementary)
                        if elementary_words_list[0][0].isupper():
                            elementary_words_list[0] = elementary_words_list[0].lower()
                        elementary_words_set = set(elementary_words_list)
                        elementary_words_set.discard('-')
                        # i don't strip "-" because of words like "well-known"
                        # and discard them only if there were between spaces
                        if len(elementary_words_set) > 1:
                            for ew in elementary_words_set:
                                word_object.elementary_words.add(Word.objects.get_or_create(language=lang, word=ew)[0])
                        word_objects += [word_object]
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
                    t.languages.add(*languages)
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