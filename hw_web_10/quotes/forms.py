from django import forms


class AuthorsForm(forms.Form):
    fullname = forms.CharField(max_length=100)
    born_date = forms.CharField(max_length=100)
    born_location = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)

class QuotesForm(forms.Form):
    quote = forms.CharField(widget=forms.Textarea)
    author = forms.CharField(max_length=100)
    tags = forms.CharField(max_length=100)

