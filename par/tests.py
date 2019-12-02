from django.test import TestCase
from django.apps import apps
from par.apps import ParConfig
from par import models


class ParConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(ParConfig.name, 'par')
        self.assertEqual(apps.get_app_config('par').name, 'par')


class CompanyModelTest(TestCase):
    def test_string_representation(self):
        company = models.Company(name="TestCompany")
        self.assertEqual(str(company), company.name)


class SkillModelTest(TestCase):
    def test_string_representation(self):
        skill = models.Skill(name="TestSkill")
        self.assertEqual(str(skill), skill.name)


class PARModelTest(TestCase):
    def setUp(self):
        par = models.PAR.objects.create(name="TestPAR", number=0)
        skill = models.Skill.objects.create(name="TestSkill1")
        par.skills.add(skill)
        skill = models.Skill.objects.create(name="TestSkill2")
        par.skills.add(skill)
        par.save()

    def test_string_representation(self):
        par = models.PAR.objects.get(name="TestPAR")
        self.assertEqual(str(par), "001 - TestPAR")

    def test_skill_count(self):
        par = models.PAR.objects.get(name="TestPAR")
        self.assertEqual(par.skill_count(), 2)


class JobModelTest(TestCase):
    def test_string_representation(self):
        job = models.Job(name="TestJob")
        self.assertEqual(str(job), job.name)
