from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget = forms.TextInput(attrs={'class': 'form-input'})) 
    password = forms.CharField(label='Пароль', widget = forms.PasswordInput(attrs={'class': 'form-input'}))

class AddPostArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['article_title', 'article_text', 'pub_date']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['article_title'].widget.attrs.update({'class':'form-control', 'placeholder': 'Введите название статьи'})
        self.fields['article_title'].required = True
        self.fields['article_text'].widget.attrs.update({'class':'form-control', 'placeholder': 'Введите текст'})
        self.fields['article_text'].required = True
        self.fields['pub_date'].widget.attrs.update({'class':'form-control', 'type':'date', 'placeholder': 'ДД.ММ.ГГГГ'})
        self.fields['pub_date'].widget.input_type = 'date'
        self.fields['pub_date'].required = True