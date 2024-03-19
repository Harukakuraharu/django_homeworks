from django.shortcuts import render, reverse
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def main_page(request):
    links={
        'Рецепт омлета': reverse('omlet'),
        'Рецепт пасты': reverse('pasta'),
        'Рецепт бутерброда': reverse('buter')
    }
    return HttpResponse("<br>".join(f"<a href='{link}'>{name}</a>" for name, link in links.items()))
    # return HttpResponse('Рецепты омлета, пасты и бутерброда')


def recipes(request):  
    meal = DATA[request.path.replace('/', '')]
    servings = int(request.GET.get('servings', 1))
    recipe = {key: value * servings for key, value in meal.items()}
    context = {
      'recipe': recipe
    }

    return render(request, 'calculator/index.html', context)
