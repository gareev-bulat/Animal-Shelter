from django.http import HttpResponse
from django.shortcuts import render
from page.models import NewsItem
from .models import Animal

def index(request):
    data = {"title": "Приют для животных 'Дом надежды' - Главная"}
    return render(request, "index.html", context=data)

def news(request):
    news = NewsItem.objects.all()[::-1]
    data = {"title": "Приют для животных 'Дом надежды' - Новости", "news": news}
    return render(request, "news.html", context=data)

def volunteering(request):
    data = {"title": "Приют для животных 'Дом надежды' - Стань волонтёром"}
    return render(request, "volunteering.html", context=data)


def pet_list(request):
    pets = Animal.objects.all()
    context = {'pets': pets, "title": "Приют для животных 'Дом надежды' - Выбери друга"}
    return render(request, 'pets.html', context)

def pet_detail(request, pk):
    animal = Animal.objects.get(pk=pk)
    context = {'animal': animal}
    return render(request, 'pet_detail.html', context)



