# from django.shortcuts import render
from django.views import generic
from .models import PAR, Skill


class IndexView(generic.ListView):
    template_name = 'par/index.html'

    def get_queryset(self):
        return PAR.objects.all()[:10]


class PARDetail(generic.DetailView):
    model = PAR


class SkillList(generic.ListView):
    model = Skill


class SkillDetail(generic.DetailView):
    model = Skill
