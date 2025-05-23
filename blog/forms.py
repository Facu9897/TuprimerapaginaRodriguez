from django import forms
from .models import Categoria, Post, Comentario

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__' 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'  

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'  


class PostSearchForm(forms.Form):
    query = forms.CharField(label='Buscar en Posts', max_length=100)
