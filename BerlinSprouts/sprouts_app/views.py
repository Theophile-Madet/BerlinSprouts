import datetime

from django.http import HttpResponse
from django.shortcuts import render

from .models import Ingredient, Meal


def index(request):
    context = {
        'oldest_ingredients': Ingredient.objects.order_by('-last_used_date')[:10]
    }
    return render(request, 'sprouts_app/index.html', context)


def add_meal(request):
    ingredient_index = 1

    ingredients = []
    while 'meal_ingredient_' + str(ingredient_index) in request.POST:
        ingredient_name = request.POST['meal_ingredient_' + str(ingredient_index)]
        ingredient_index = ingredient_index + 1
        if Ingredient.objects.filter(name=ingredient_name).count() == 0:
            ingredient = Ingredient(name=ingredient_name, last_used_date=datetime.date.today())
            ingredient.save()
        ingredients.append(Ingredient.objects.get(name=ingredient_name))

    meal_name = request.POST['meal_name']
    meal_date = request.POST['meal_date']
    meal = Meal(name=meal_name, date=meal_date)
    meal.save()
    for ingredient in ingredients:
        meal.ingredients.add(ingredient)
    meal.save()
