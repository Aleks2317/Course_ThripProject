from django.urls import path
from crud.views import index, create


urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create')

]
