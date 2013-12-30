__author__ = 'Mpourreza'
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.ImageField(
        label='Select an image',
        help_text='max. 42 megabytes'
    )
