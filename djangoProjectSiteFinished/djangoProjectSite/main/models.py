from django.db import models

# Create your models here.

class Description(models.Model):
    title = models.CharField('Название',max_length=50)
    demand = models.TextField('Востребованность')
    geography = models.TextField('География')
    skills = models.TextField('Навыки')
    lastvac = models.TextField('Последние вакансии')

    def __str__(self):
        return self.title
