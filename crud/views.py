from django.shortcuts import render
from django.http import HttpResponse
from crud.forms import UserForm


# def index(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')  # получить значение поля Имя
#         age = request.POST.get('age')  # получить значение поля Возраст
#         return HttpResponse(f'<h2>Привет, {name}, твой возраст {age}</h2>')
#     userform = UserForm()
#     return render(request, 'index.html', {'form': userform})

def index(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid:
            name = userform.cleaned_data['name']  # получить очищенные данные, через объект cleaned_data
            return HttpResponse(f'<h2>Hello, {name}</h2>')
        return HttpResponse(f'Invalid date')
    userform = UserForm()
    return render(request, 'index.html', {'form': userform})

