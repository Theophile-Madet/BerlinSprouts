from django.db import models


class Ingredient(models.Model):
    name = models.CharField('Name', max_length=200)
    last_used_date = models.DateField('Date of last use')

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField('Name', max_length=200)
    date = models.DateField('Date')
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name + " " + str(self.date)
