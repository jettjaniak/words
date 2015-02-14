from django.views.generic import ListView
from app.models import Translation


class TranslationListView(ListView):
    model = Translation
    template_name = 'translation_list.html'