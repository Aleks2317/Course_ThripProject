# from django import forms


# class UserForm(forms.Form):
#     name = forms.CharField(label='Имя',
#                            initial='undefined',
#                            help_text='Введите свое имя',
#                            )
#     age = forms.IntegerField(label='Ваш вош возраст?',
#                              initial=18,
#                              help_text='Введите свой возраст',
#                              )
#     filed_order = ['age', 'name']  # меняем порядок следования полей


# class UserForm(forms.Form):
#     name = forms.CharField(label='Имя', help_text='Введите ваше имя!', min_length=2, max_length=10)
#     age = forms.IntegerField(label='Ваш Возраст', help_text='Введите свой возраст')
#     reklama = forms.BooleanField(label='Согласны получать рекламу?', required=False)


from django.forms import ModelForm, CharField, IntegerField
from .models import Person


class PersonForm(ModelForm):
    name = CharField(label='Введите имя')
    age = IntegerField(label='Введите возраст')

    class Meta:
        # зададим имя модели на основе которой будет создана форма и укажем используемые поля fields = ['name', 'age'].
        model = Person
        fields = ['name', 'age']
