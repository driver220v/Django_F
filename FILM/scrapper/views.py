from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, View
import json

from .models import Film


class FilterListView(View):
    def get(self, request, *args, **kwargs):
        queryset = Film.objects.values_list('title', flat=True)

        if 'title' in request.GET:
            queryset=queryset.filter(title__startswith=request.GET['title'])

        return HttpResponse(json.dumps(list(queryset)), content_type='application/json')


# Create your views here.
class ListAllView(TemplateView):
    template_name = "scrapper/list.html"
    context = {
        'film': Film.objects.all()
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class ListDetailView(TemplateView):
    template_name = "scrapper/detail.html"
    context = {
        'film': Film
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
