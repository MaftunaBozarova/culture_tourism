from django.db.models import Count
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import FeedBackForm, SearchForm
from django.db.models import Q


def search(request):
    if request.method == 'POST':
        search_form = SearchForm(data=request.POST)
        if search_form.is_valid():
            search_query = search_form.cleaned_data['search_query']
            results_n = News.objects.filter(
                Q(news_title__icontains=search_query) | Q(news_body__icontains=search_query)).order_by('news_created')
            results_s = SubArticle.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
            results_r = Regions.objects.filter(
                Q(title__icontains=search_query) | Q(body__icontains=search_query))
            results_w = Writer.objects.filter(Q(description__icontains=search_query) | Q(name__icontains=search_query))

            gallereya = Gallery.objects.all()[:9]

            return render(request, 'search.html',
                          {'searchN': results_n, 'searchS': results_s, 'searchR': results_r, 'searchW': results_w,
                           'search_query': search_query, 'gallery': gallereya})


def feedback(request):
    if request.method == 'POST':
        feedback_form = FeedBackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            return redirect('/')


def index(request):
    slides = Slide.objects.all()
    main_articles = MainArticle.objects.all()[:5]

    return render(request, 'index.html', {'main_articles': main_articles,
                                          'slides': slides
                                          })


def mainarticle(request, pk):
    main_article = get_object_or_404(MainArticle, pk=pk)
    content = main_article.subarticle.last()
    gallery = Gallery.objects.all()[:9]

    post_tags_ids = content.tags.values_list('id', flat=True)
    related_topics = SubArticle.objects.filter(tags__in=post_tags_ids).exclude(id=content.id)
    related_topics = related_topics.annotate(same_tags=Count('tags')).order_by('-same_tags', '-created')

    return render(request, 'big-text.html', {'content': content,
                                             'related_topics': related_topics,
                                             'gallery': gallery,
                                             })


def maqollar(request):
    maqol = Maqollar.objects.all()
    gallery = Gallery.objects.all()[:9]
    ertaklar = Tale.objects.all()[:3]

    paginator = Paginator(maqol, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'maqol.html', {'maqollar': maqol, 'page': page, 'posts': posts,
                                          'gallery': gallery, 'tales': ertaklar
                                          })


def menu(request, pk):
    men = Menyu.objects.get(pk=pk)
    general = GeneralInfo.objects.filter(menu=men).last().subarticle
    gallery = Gallery.objects.filter(category=men)[:9]

    if general.count() < 4:
        last = general.last()
        post_tags_ids = last.tags.values_list('id', flat=True)
        related_topics = SubArticle.objects.filter(tags__in=post_tags_ids).exclude(id=last.id)
        related_topics = related_topics.annotate(same_tags=Count('tags')).order_by('-same_tags', '-created')[:3]

        return render(request, 'big-text.html', {'content': last, 'menu_pk': pk,
                                                 'related_topics': related_topics,
                                                 'gallery': gallery
                                                 })
    else:
        paginator = Paginator(general.all(), 4)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return render(request, 'small-text.html', {'page': page, 'posts': posts,
                                                   'second': men.name,
                                                   'gallery': gallery
                                                   })


def adiblar(request):
    gallereya = Gallery.objects.all()[:9]
    general = Writer.objects.all()
    paginator = Paginator(general, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'small-text.html', {'page': page, 'posts': posts, 'gallery': gallereya
                                               })


def small_to_big(request, pk):
    gallery = Gallery.objects.all()[:9]
    content = SubArticle.objects.get(pk=pk)

    post_tags_ids = content.tags.values_list('id', flat=True)
    related_topics = SubArticle.objects.filter(tags__in=post_tags_ids).exclude(id=content.id)
    related_topics = related_topics.annotate(same_tags=Count('tags')).order_by('-same_tags', '-created')
    related_topics = related_topics[:3]
    return render(request, 'big-text.html', {'content': content, 'related_topics': related_topics,
                                             'gallery': gallery
                                             })


def news(request, pk):
    chosen_news = News.objects.get(pk=pk)
    gallery = Gallery.objects.all()[:9]

    return render(request, 'news.html', {
        'content': chosen_news,
        'gallery': gallery
    })


def most_visited(request, pk):
    most_visited_obj = MostVisited.objects.get(pk=pk)
    gallery = Gallery.objects.all()[:9]

    return render(request, 'big-text.html', {'content': most_visited_obj,
                                             'gallery': gallery
                                             })


def regions(request, pk=None):
    gallery = Gallery.objects.all()[:9]
    if pk:
        chosen_region = Regions.objects.get(pk=pk)
        return render(request, 'big-text.html', {'content': chosen_region, 'gallery': gallery()})
    all_regions = Regions.objects.all()[:13]
    return render(request, 'regions.html', {'regions': all_regions, 'gallery': gallery})


def about_us(request):
    return render(request, 'about.html')


def gallery(request):
    menus = Menyu.objects.all()
    gallereya = Gallery.objects.all()[:9]

    # TODO: Exclude PICTURES from sidebar
    return render(request, 'galleriya.html', {'menus': menus, 'gallery': gallereya})


def library(request):
    gallereya = Gallery.objects.all()[:9]
    all_libraries = Library.objects.all()
    paginator = Paginator(all_libraries, 18)
    page = request.GET.get('page')
    try:
        all_libraries = paginator.page(page)
    except PageNotAnInteger:
        all_libraries = paginator.page(1)
    except EmptyPage:
        all_libraries = paginator.page(paginator.num_pages)
    return render(request, 'kutubxona.html', {'page': page, 'libraries': all_libraries, 'gallery': gallereya})


def tales(request):
    gallereya = Gallery.objects.all()[:9]
    all_tales = Tale.objects.all()
    paginator = Paginator(all_tales, 6)
    page = request.GET.get('page')
    try:
        all_tales = paginator.page(page)
    except PageNotAnInteger:
        all_tales = paginator.page(1)
    except EmptyPage:
        all_tales = paginator.page(paginator.num_pages)

    return render(request, 'small-text-for-tales.html', {'page': page, 'posts': all_tales, 'gallery': gallereya})
