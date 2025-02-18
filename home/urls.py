from django.urls import path
from home.views import home, agregar_autor, agregar_categoria, agregar_post, buscar_post

urlpatterns = [
    path("", home, name="home"),
    path("buscar-post/", buscar_post, name="buscar_post"),
    path("agregar-post/", agregar_post, name="agregar_post"),
    path("agregar-autor/", agregar_autor, name="agregar_autor"),
    path("agregar-categoria/", agregar_categoria, name="agregar_categoria"),
]