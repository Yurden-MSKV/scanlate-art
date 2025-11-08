from django.db import models

'''Роль, которую ищет коллектив'''
class JobRole(models.Model):
    role_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Роли'

class Vacancy(models.Model):
    role = models.ForeignKey(JobRole, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вакансии'