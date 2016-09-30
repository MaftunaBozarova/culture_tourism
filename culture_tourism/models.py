from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
# from redactor.fields import RedactorField
from django.utils.translation import ugettext as _
from taggit.managers import TaggableManager
from treebeard.mp_tree import MP_Node
from ckeditor.fields import RichTextField


class Menyu(MP_Node):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=255, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Menus'
        verbose_name = 'Menu'

    def get_url(self):
        if self.url and not 'http' in self.url:
            return reverse(self.url)
        return self.url


class SubArticle(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = RichTextField(verbose_name=u'Text')
    photo = models.ImageField(upload_to='main_article/', blank=True, null=True)
    photo2 = models.ImageField(upload_to='main_article/', blank=True, null=True)
    tags = TaggableManager()
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, blank=True)

    def get_next(self):
        next = SubArticle.objects.filter(id__gt=self.id)
        if next:
            return next.first()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SubArticle, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class GeneralInfo(models.Model):
    menu = models.ForeignKey(Menyu, related_name='general_menus', null=True)
    menu_name = models.SlugField(max_length=150, blank=True)
    subarticle = models.ManyToManyField(SubArticle, related_name='generalinfo')
    author = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.menu_name = slugify(self.menu.name)
        super(GeneralInfo, self).save(*args, **kwargs)


class MainArticle(models.Model):
    b_tild = models.CharField(max_length=200, unique=True)
    b_box = models.CharField(blank=True, max_length=200, null=True)
    subarticle = models.ManyToManyField(SubArticle, related_name='mainarticle')

    def __str__(self):
        return '%s' % (self.b_tild)


class Regions(models.Model):
    title = models.CharField(max_length=70)
    photo = models.ImageField(upload_to='regions/', blank=True)
    body = RichTextField(verbose_name=u'Text')

    def __str__(self):
        return self.title


class Writer(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='writers/', blank=True)
    period = models.CharField(max_length=50, blank=True)
    description = RichTextField(verbose_name=u'Text')


class Slide(models.Model):
    title = models.TextField(blank=True)
    photo = models.ImageField(upload_to='slide/', blank=False)
    description = RichTextField(verbose_name=u'Text')
    created = models.DateTimeField(auto_now_add=True)


class OtherInfo(models.Model):
    description = RichTextField(verbose_name=u'Text')
    promo_photo = models.ImageField()
    address = models.CharField(max_length=255, blank=True)
    phone_1 = models.CharField(max_length=17, blank=True)
    phone_2 = models.CharField(max_length=17, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)


class News(models.Model):
    news_title = models.CharField(max_length=200, blank=True, db_index=True)
    news_photo = models.ImageField(upload_to='news/', blank=True)
    news_body = RichTextField(verbose_name=u'News')
    news_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, blank=True)

    def get_next(self):
        next = News.objects.filter(id__gt=self.id)
        if next:
            return next.first()

    def get_prev(self):
        prev = News.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.news_title)
        super(News, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-news_created',)


class Gallery(models.Model):
    category = models.ForeignKey(Menyu, related_name='gallery')
    photo = models.ImageField(upload_to='gallery/')
    description = RichTextField(verbose_name=u'Description')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


class Library(models.Model):
    lib_name = models.CharField(max_length=255, blank=True)
    lib_photo = models.ImageField(upload_to='library/', blank=True)
    lib_file = models.FileField(upload_to='library/', blank=True)
    lib_description = RichTextField(verbose_name=u'Text')
    lib_created = models.DateTimeField(auto_now_add=True, blank=True)

    @property
    def get_url(self):
        return self.lib_file.url

    class Meta:
        ordering = ['-lib_created']


class Feedback(models.Model):
    name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    comment = RichTextField(verbose_name=u'Text')


class MostVisited(models.Model):
    title = models.CharField(max_length=200)
    region = models.ForeignKey(Regions, related_name='most_visiteds')
    photo = models.ImageField(upload_to='most-visited/', null=True)
    body = RichTextField(verbose_name=u'Text', null=True)
    n_slug = models.SlugField(max_length=250, blank=True)
    r_slug = models.SlugField(max_length=250, blank=True)

    def save(self, *args, **kwargs):
        self.n_slug = slugify(self.title)
        self.r_slug = slugify(self.region.title)
        super(MostVisited, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Maqollar(models.Model):
    title = models.CharField(blank=True, max_length=512)
    body = RichTextField(verbose_name=u'Maqol')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Tale(models.Model):
    tale = models.ForeignKey(SubArticle, related_name='tales', blank=True, null=True)
    file = models.FileField(blank=True, upload_to='tales/')
    author = models.CharField(max_length=100, blank=True)
