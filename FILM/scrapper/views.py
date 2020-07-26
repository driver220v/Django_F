from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Film


# Create your views here.
class ListAllView(TemplateView):
    template_name = "scrapper/list.html"
    context = {
        'film': Film.objects.all()
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass

#
class ListDetailView(TemplateView):
    template_name = "scrapper/detail.html"
    context = {
        'film': Film
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
