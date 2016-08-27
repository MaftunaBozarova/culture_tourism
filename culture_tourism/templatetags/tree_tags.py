from django import template
from culture_tourism.models import Menyu, OtherInfo, MostVisited, News
from culture_tourism.forms import SearchForm, FeedBackForm
from django.core.urlresolvers import resolve, reverse
from django.utils.translation import activate, get_language
from django.utils import timezone
from taggit.models import Tag
import random
register = template.Library()


def tree_show():
    return Menyu.get_root_nodes()
register.assignment_tag(tree_show)


def search():
    return SearchForm()
register.assignment_tag(search)


@register.simple_tag(takes_context=True)
def change_lang(context, lang=None, *args, **kwargs):
    """
    Get active page's url by a specified language
    Usage: {% change_lang 'en' %}
    """

    path = context['request'].path
    url_parts = resolve( path )

    url = path
    cur_language = get_language()
    try:
        activate(lang)
        url = reverse( url_parts.view_name, kwargs=url_parts.kwargs )
    finally:
        activate(cur_language)


    return "%s" % url


def other_info():
    return OtherInfo.objects.last()
register.assignment_tag(other_info)


def most_visited():
    return MostVisited.objects.all()[:5]
register.assignment_tag(most_visited)


def clock():
    return timezone.now
register.assignment_tag(clock)


def feedback():
    return FeedBackForm()
register.assignment_tag(feedback)


def news():
    return News.objects.all()[:3]
register.assignment_tag(news)


def all_tags():
    return Tag.objects.all()
register.assignment_tag(all_tags)


def random_num():
    return random
register.assignment_tag(random_num)
