from django.urls import path
from scrapper.views import ListAllView, ListDetailView
from . import views

urlpatterns = [
    path('all/', ListAllView.as_view(), name='scraper-all'),
    path('one/', ListDetailView.as_view(), name='scrapper-one'),
    # path('', views.hello, name='scrapper-hello')
]