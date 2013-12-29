__author__ = 'Mpourreza'
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select an image',
        help_text='max. 42 megabytes'
    )

# class Document(forms.Form):
#     docfile = forms.FileField(upload_to='documents/%Y/%m/%d')