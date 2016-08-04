from django.contrib import admin
from .models import *
from treebeard.forms import movenodeform_factory
from treebeard.admin import TreeAdmin


class AdminMenu(TreeAdmin):
    form = movenodeform_factory(Menyu)
admin.site.register(Menyu, AdminMenu)


class RegionAdmin(admin.ModelAdmin):
    list_display = ['region_name', 'region_photo']
admin.site.register(Regions, RegionAdmin)


class NationalInfoAdmin(admin.ModelAdmin):
    list_display = ['menu', 'author']
admin.site.register(GeneralInfo, NationalInfoAdmin)


class WriterAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'period']
admin.site.register(Writer, WriterAdmin)


class MainArticleAdmin(admin.ModelAdmin):
    list_display = ['b_tild', 'b_box']
admin.site.register(MainArticle, MainArticleAdmin)


class SlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo', 'description']
admin.site.register(Slide, SlideAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['news_title', 'news_photo', 'news_created']
admin.site.register(News, NewsAdmin)


class OtherInfoAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone_1', 'email', 'website']
admin.site.register(OtherInfo, OtherInfoAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['category', 'photo', 'created']
admin.site.register(Gallery, GalleryAdmin)


class LibraryAdmin(admin.ModelAdmin):
    list_display = ['lib_name', 'lib_photo', 'lib_file', 'lib_created']
admin.site.register(Library, LibraryAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
admin.site.register(Feedback, FeedbackAdmin)


class PromoAdmin(admin.ModelAdmin):
    list_display = ['promo_text', 'promo_photo']
admin.site.register(Promo, PromoAdmin)


class SubArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo', 'body', 'created']
admin.site.register(SubArticle, SubArticleAdmin)


class MostVisitedAdmin(admin.ModelAdmin):
    list_display = ['title', 'region']
admin.site.register(MostVisited, MostVisitedAdmin)


class MaqolAdmin(admin.ModelAdmin):
    list_display = ['title', 'body']
admin.site.register(Maqollar, MaqolAdmin)


class TurismAdmin(admin.ModelAdmin):
    list_display = ['name', 'region', 'created']
admin.site.register(Tourism, TurismAdmin)


class KechaBugunAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
admin.site.register(KechaBugun, KechaBugunAdmin)


class FirstAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
admin.site.register(First, FirstAdmin)


class SecondAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
admin.site.register(Second, FirstAdmin)


class SanatAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
admin.site.register(Sanat, SanatAdmin)
