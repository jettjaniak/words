from django.shortcuts import get_object_or_404

from app.models import Language


def get_languages(kwargs):
    return \
        [get_object_or_404(Language, code=kwargs['lang1']), get_object_or_404(Language, code=kwargs['lang2'])]
