from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.all_films, name='scraper-all'),
    # path('one', views.all_films, name='scrapper-one'),
    # path('', views.hello, name='scrapper-hello')
]