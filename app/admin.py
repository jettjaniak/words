from django.contrib import admin
from app.models import Language, Word, Category, Translation

admin.site.register(Language)
admin.site.register(Word)
admin.site.register(Category)
admin.site.register(Translation)