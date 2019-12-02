# from django.shortcuts import render
from django.views import generic
from .models import PAR


class IndexView(generic.ListView):
    template_name = 'par/index.html'

    def get_queryset(self):
        return PAR.objects.all().order_by('-number')[:10]


class PARDetail(generic.DetailView):
    model = PAR
