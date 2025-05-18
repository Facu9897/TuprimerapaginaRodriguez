from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoriaForm, PostForm, ComentarioForm, PostSearchForm
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-fecha')
    return render(request, 'blog/home.html', {'posts': posts})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'blog/form.html', {'form': form, 'titulo': 'Crear Categoría'})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/form.html', {'form': form, 'titulo': 'Crear Post'})

def crear_comentario(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('home')
    else:
        form = ComentarioForm()
    return render(request, 'blog/form.html', {'form': form, 'titulo': 'Crear Comentario'})

def buscar(request):
    form = PostSearchForm(request.GET)
    resultados = []
    if form.is_valid():
        query = form.cleaned_data['query']
        resultados = Post.objects.filter(titulo__icontains=query)
    return render(request, 'blog/buscar.html', {'form': form, 'resultados': resultados})

