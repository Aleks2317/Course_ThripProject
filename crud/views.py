from django.shortcuts import render
from crud.forms import UserForm


def index(request):
    userform = UserForm()
    return render(request, 'index.html', {'form': userform})
