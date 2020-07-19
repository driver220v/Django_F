from django.shortcuts import render, HttpResponse
from .models import Film


# Create your views here.

def all_films(request):
    # pass
    # context = {
    #     'film': Film.objects.all()
    # }
    for i in Film.objects.all():
        print(i)
    return HttpResponse('ok printed')

def hello(request):
    return HttpResponse('ok')

# def one_film(request):
#     pass
#     context = {
#         'film': Film.
#     }
#     return render(request, context)
