from django.shortcuts import render, redirect
from .models import Post
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm

def home(request):
    return render(request, "home.html")

def agregar_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AutorForm()
    return render(request, "formulario.html", {"form": form})

def agregar_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CategoriaForm()
    return render(request, "formulario.html", {"form": form})

def agregar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "formulario.html", {"form": form})

def buscar_post(request):
    posts = []
    if request.GET.get("titulo"):
        titulo = request.GET["titulo"]
        posts = Post.objects.filter(titulo__icontains=titulo)
    
    form = BusquedaPostForm()
    return render(request, "busqueda.html", {"form": form, "posts": posts})

