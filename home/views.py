from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CategoriaForm, PostForm, BusquedaPostForm, AutorForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import View


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/lista_posts.html"
    context_object_name = "posts"
    paginate_by = 10

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/detalle_post.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["titulo", "subtitulo", "contenido", "imagen"]
    template_name = "blog/formulario.html"
    success_url = reverse_lazy("lista_posts")

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["titulo", "subtitulo", "contenido", "imagen"]
    template_name = "blog/formulario.html"
    success_url = reverse_lazy("lista_posts")

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/confirmar_borrar.html"
    success_url = reverse_lazy("lista_posts")  

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        posts = Post.objects.all().order_by("-fecha_publicacion")[:5]
        return render(request, "home.html", {"posts": posts})

@login_required
def agregar_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("home")
    else:
        form = AutorForm()
    return render(request, "formulario.html", {"form": form})

@login_required
def agregar_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CategoriaForm()
    return render(request, "formulario.html", {"form": form})

@login_required
def agregar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) 
            post.autor = request.user 
            post.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "formulario.html", {"form": form})


@login_required
def buscar_post(request):
    posts = []
    if request.GET.get("titulo"):
        titulo = request.GET["titulo"]
        posts = Post.objects.filter(titulo__icontains=titulo)
    
    form = BusquedaPostForm()
    return render(request, "busqueda.html", {"form": form, "posts": posts})

@login_required
def detalle_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detalle_post.html', {'post': post})

def portada(request):
    return render(request, 'portada.html')

def aboutme(request):
    return render(request, 'aboutme.html')