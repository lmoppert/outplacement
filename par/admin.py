from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from par import models


@admin.register(models.PAR)
class PARAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('__str__', 'company', 'skill_count')
    filter_horizontal = ('skills',)
    list_filter = ('company', 'skills')
    models.PAR


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    models.Job


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    models.Skill


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    models.Company
