from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from crud.models import Person


# Получение данных из бд
def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})


# Сохранение данных в бд
def create(request):
    if request.method == 'POST':
        person = Person()
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.save()
        return HttpResponseRedirect('/')

''' через класс временной переадресации HttpResponseRedirect, перенаправляем пользователя по пути '/', 
т.е. выполняем редирект в корневую директорию сайта. Где он, согласно маршруту, будет обрабатываться функцией index(), 
которая в свою очередь отобразит данные всех пользователей(в том числе и только что добавленные) 
на главной странице сайта в шаблоне index.html.'''
