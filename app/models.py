from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.name


class Word(models.Model):
    language = models.ForeignKey(Language)
    word = models.CharField(max_length=200)
    note = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = ('language', 'word')

    def __str__(self):
        return self.word


class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', blank=True, null=True)

    def __str__(self):
        return self.name


class Translation(models.Model):
    words = models.ManyToManyField(Word, related_name='translations')
    categories = models.ManyToManyField(Category)
    note = models.CharField(max_length=400, blank=True, null=True)

    def languages(self):
        """
        Returns a list of Language objects occurring in Words
        (language field) from self.words ManyToMany field.
        """
        languages = []
        for w in self.words.all():
            if w.language not in languages:
                languages += [w.language]
        return languages

    def __str__(self):
        """ Eg. "english_word, english_word, ... (en) - polish_word, polish_word, ... (pl)". """
        lang_words_str = []
        for l in self.languages():
            lang_words_list = [w.word for w in self.words.filter(language=l)]
            lang_words_str += ["%s (%s)" % (", ".join(lang_words_list), l.code)]

        return " - ".join(lang_words_str)
