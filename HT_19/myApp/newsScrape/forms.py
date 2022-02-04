from django import forms

categories = ('askstories', 'showstories', 'newstories', 'jobstories')
categories = [(i, i) for i in categories]


class CategoryForm(forms.Form):
    category = forms.CharField(label="", max_length=20, widget=forms.Select(choices=categories))
