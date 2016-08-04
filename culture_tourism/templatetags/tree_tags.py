from django import template
from culture_tourism.models import Menyu
from culture_tourism.forms import SearchForm

register = template.Library()


def tree_show():
    return Menyu.get_root_nodes()

register.assignment_tag(tree_show)


def search():
    return SearchForm()
register.assignment_tag(search)