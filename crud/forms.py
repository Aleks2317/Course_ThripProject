from django import forms


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


class UserForm(forms.Form):
    name = forms.CharField(label='Имя', help_text='Введите ваше имя!', min_length=2, max_length=10)
    age = forms.IntegerField(label='Ваш Возраст', help_text='Введите свой возраст')
    reklama = forms.BooleanField(label='Согласны получать рекламу?', required=False)
