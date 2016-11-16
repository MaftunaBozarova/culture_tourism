from django import forms
from .models import Feedback
from django.utils.translation import ugettext as _


class FeedBackForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'id': 'usr',
        'class': 'form-control', 'placeholder': 'Name'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'id': 'email', 'placeholder': 'Email'}), required=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Comment', 'cols': '47'}), required=False)

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'comment']


class SearchForm(forms.Form):
    search_query = forms.CharField(label='', max_length=512, required=False, widget=forms.TextInput(attrs={
        'type': 'search', 'placeholder': _('Search')}))
