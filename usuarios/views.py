from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .forms import RegistroUsuarioForm, PerfilForm
from django.shortcuts import render, get_object_or_404
from .models import Post, Perfil


def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.is_active = True 
            user.save()

            Perfil.objects.create(user=user)

            return redirect("login")
    else:
        form = RegistroUsuarioForm()
    return render(request, "usuarios/registro.html", {"form": form})


def iniciar_sesion(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get("next", "home")
            return redirect(next_url)
        else:
            print("Usuario o contraseña incorrectos")
            context = {'error': 'Usuario o contraseña incorrectos'}
            return render(request, "usuarios/login.html", context)
    return render(request, "usuarios/login.html")

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect("login")

class PerfilView(LoginRequiredMixin, DetailView):
    template_name = "usuarios/perfil.html"

    def get_object(self):
        return self.request.user

@login_required
def editar_perfil(request):
    perfil = request.user.usuarios_perfil

    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():           
            perfil = form.save(commit=False)           
            password = form.cleaned_data.get("password")
            
            if password:
                user = request.user
                user.set_password(password)  
                user.save()  
                login(request, user)  
            
            perfil.save()  
            return redirect("perfil")  
    else:
        form = PerfilForm(instance=perfil)

    return render(request, "usuarios/editar_perfil.html", {"form": form})


@login_required
def perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    print(f"Perfil encontrado: {perfil}")
    print(f"Biografía: {perfil.biografia}")
    if not perfil.avatar:
        perfil.avatar = 'avatars/default_avatar.png'
    return render(request, "usuarios/perfil.html", {"perfil": perfil})

@login_required
def detalle_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detalle_post.html', {'post': post})