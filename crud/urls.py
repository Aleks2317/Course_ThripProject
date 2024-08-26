from django.urls import path
from crud.views import index, create, edit, delete


urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete')

]
