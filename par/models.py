# from django.utils import timezone
from django.urls import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Company(models.Model):
    """This model will hold company names"""

    name = models.CharField(max_length=200, verbose_name=_("Company"))

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

    def __str__(self):
        return "{}".format(self.name)


class Skill(models.Model):
    """This model will hold available skills"""

    name = models.CharField(max_length=200, verbose_name=_("Skill"))

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")

    def __str__(self):
        return "{}".format(self.name)


class PAR(models.Model):
    """This model will wrap all components of the PAR together"""

    name = models.CharField(max_length=200, verbose_name=_("PAR"))
    problem = models.TextField(blank=True, verbose_name=_("Problem"))
    action = models.TextField(blank=True, verbose_name=_("Action"))
    result = models.TextField(blank=True, verbose_name=_("Result"))
    number = models.PositiveSmallIntegerField(default=0,
                                              blank=False,
                                              null=False,
                                              db_index=True)
    skills = models.ManyToManyField(Skill,
                                    blank=True,
                                    verbose_name=_("Skills"))
    company = models.ForeignKey(Company,
                                blank=True,
                                null=True,
                                on_delete=models.SET_NULL,
                                verbose_name=_("Company"))

    class Meta:
        ordering = ['number']
        verbose_name = _("PAR")
        verbose_name_plural = _("PARs")

    def skill_count(self):
        return self.skills.count()

    def get_absolute_url(self):
        return reverse('par-detail', args=[str(self.id)])

    def __str__(self):
        return "{:03d} - {}".format(self.number + 1, self.name)


class Job(models.Model):
    """This model will list the core skills needed for a job"""

    name = models.CharField(max_length=200, verbose_name=_("Job"))
    core_skills = models.ManyToManyField(Skill, verbose_name=_("Core Skills"))

    class Meta:
        verbose_name = _("Job")
        verbose_name_plural = _("Jobs")

    def __str__(self):
        return "{}".format(self.name)
