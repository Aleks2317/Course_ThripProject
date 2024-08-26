# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponseNotFound
# from .models import Person
# from .forms import PersonForm
# from django.forms.models import model_to_dict
#
#
# # Получение данных из бд
# def index(request):
#     form = PersonForm()
#     people = Person.objects.all()
#     return render(request, 'index.html', {'form': form, 'people': people})
#
#
# # Сохранение данных в бд
# def create(request):
#     if request.method == 'POST':
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             person = Person()
#             person.name = request.POST.get('name')
#             person.age = request.POST.get('age')
#             person.save()
#     return HttpResponseRedirect('/')
#
# ''' через класс временной переадресации HttpResponseRedirect, перенаправляем пользователя по пути '/',
# т.е. выполняем редирект в корневую директорию сайта. Где он, согласно маршруту, будет обрабатываться функцией index(),
# которая в свою очередь отобразит данные всех пользователей(в том числе и только что добавленные)
# на главной странице сайта в шаблоне index.html.'''
#
#
# # Изменение данных в БД
# def edit(request, id):  # в качестве параметра, принимает идентификатор объекта id из маршрута
#     try:
#         person = Person.objects.get(id=id)
#         if request.method == 'POST':
#             form = PersonForm(request.POST)
#             if form.is_valid():
#                 person.name = request.POST.get('name')
#                 person.age = request.POST.get('age')
#                 person.save()
#             return HttpResponseRedirect('/')
#         else:
#             '''Если запрос был методом GET, тогда мы передаём в форму выбранный объект person,
#             который преобразуем в словарь, с помощью функции model_to_dict()'''
#             form = PersonForm(model_to_dict(person))
#             return render(request, 'edit.html', {'form': form})
#     except Person.DoesNotExist:  # DoesNotExist (объект не найден)
#         return HttpResponseNotFound('<h2> Person not found</h2>')
#
#
# # Удаление данных из БД
# def delete(request, id):  # в качестве параметра, принимает идентификатор объекта id из маршрута
#     try:
#         person = Person.objects.get(id=id)
#         person.delete()
#         return HttpResponseRedirect('/')
#     except Person.DoesNotExist:
#         return HttpResponseNotFound('<h2> Person not found</h2>')

"""Применение модельных форм в CRUD проекте"""

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Person
from .forms import PersonForm


# Получение данных из БД
def index(request):
    form = PersonForm()
    people = Person.objects.all()
    return render(request, 'index.html', {'form': form, 'people': people})


# Сохранение данных в БД
def create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/')


# Изменение данных в БД
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == 'POST':
            """В отличие от обычной формы (унаследованной от django.forms.Form), 
            у модельной формы (унаследованной от django.forms.ModelForm) есть параметр 
            instance. Он позволяет связать форму с объектом модели. Это полезно, когда 
            нужно изменить объект модели через форму."""
            form = PersonForm(request.POST, instance=person)  # необходимо передать в форму выбранный объект person
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/')
        else:
            form = PersonForm(instance=person)
            return render(request, 'edit.html', {'form': form})
    except Person.DoesnNotExist:
        return HttpResponseNotFound('<h2>Person not found</h2>')


# Удаление данных из БД
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect('/')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person not found</h2>')

