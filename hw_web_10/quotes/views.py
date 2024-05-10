from django.shortcuts import render,redirect
from django.http import Http404
from .models import Quotes,Authors
from django.contrib.auth.decorators import login_required
from .forms import AuthorsForm, QuotesForm

from .forms import AuthorsForm, QuotesForm
from .models import Authors, Quotes


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorsForm(request.POST)
        if form.is_valid():
            author_data = form.cleaned_data
            author = Authors(
                fullname=author_data['fullname'],
                born_date=author_data['born_date'],
                born_location=author_data['born_location'],
                description=author_data['description']
            )
            author.save()
            return redirect('quotes:quotes_list')  
    else:
        form = AuthorsForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuotesForm(request.POST)
        if form.is_valid():
            quote_data = form.cleaned_data
            author_name = quote_data.pop('author')  
            author = Authors.objects.get(fullname=author_name)  
            tags = quote_data.pop('tags').split(',')  
            quote = Quotes(
                author=author,
                tags=tags,
                quote=quote_data['quote']
            )
            quote.save()
            return redirect('quotes:quotes_list')  
    else:
        form = QuotesForm()
    return render(request, 'quotes/add_quote.html', {'form': form})


def main(request):
    quotes = Quotes.objects.all()
    return render(request, 'quotes/quotes_list.html', {'quotes': quotes})

def author_detail(request, author_fullname):
    try:
        author = Authors.objects.get(fullname=author_fullname)
    except Authors.DoesNotExist:
        raise Http404("Автор не знайдений")
    return render(request, 'quotes/author_detail.html', {'author': author})