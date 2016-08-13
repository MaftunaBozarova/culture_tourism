from modeltranslation.translator import translator, TranslationOptions
from .models import *


class SubArticleTranslation(TranslationOptions):
    fields = ('title', 'body',)


class MainArticleTranslation(TranslationOptions):
    fields = ('b_tild', 'b_box')


class RegionTranslation(TranslationOptions):
    fields = ('title', 'body',)


class WriterTranslation(TranslationOptions):
    fields = ('name', 'description',)


class SliderTranslation(TranslationOptions):
    fields = ('title', 'description',)


class OtherInfoTranslation(TranslationOptions):
    fields = ('description', 'address',)


class NewsTranslation(TranslationOptions):
    fields = ('news_title', 'news_body',)


class GalleryTranslation(TranslationOptions):
    fields = ('description',)


class LibraryTranslation(TranslationOptions):
    fields = ('lib_name', 'lib_description',)


class MostVisitedTranslation(TranslationOptions):
    fields = ('title', 'body',)


class MaqolTranslation(TranslationOptions):
    fields = ('title', 'body')


class MenuTranslation(TranslationOptions):
    fields = ('name',)


translator.register(Menyu, MenuTranslation)
translator.register(SubArticle, SubArticleTranslation)
translator.register(MainArticle, MainArticleTranslation)
translator.register(Regions, RegionTranslation)
translator.register(Writer, WriterTranslation)
translator.register(Slide, SliderTranslation)
translator.register(OtherInfo, OtherInfoTranslation)
translator.register(News, NewsTranslation)
translator.register(Gallery, GalleryTranslation)
translator.register(Library, LibraryTranslation)
translator.register(MostVisited, MostVisitedTranslation)
translator.register(Maqollar, MaqolTranslation)
