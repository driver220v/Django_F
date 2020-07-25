from django.shortcuts import render, HttpResponse
from .models import Film


# Create your views here.

def all_films(request):
    context = {
        'film': Film.objects.all()
    }
    return render(request, 'scrapper/list.html', context)

# def hello(request):
#     return HttpResponse('ok')
#
# # def one_film(request):
# #     pass
# #     context = {
# #         'film': Film.
# #     }
# #     return render(request, context)
