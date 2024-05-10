from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('quotes/', views.main, name='quotes_list'),
    path('author/<str:author_fullname>/', views.author_detail, name='author_detail'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
]

