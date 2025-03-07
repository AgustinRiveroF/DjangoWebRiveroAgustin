from django.contrib import admin
from .models import Categoria, Post, Perfil


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "autor", "fecha_publicacion", "categoria")
    search_fields = ("titulo", "subtitulo", "contenido")
    list_filter = ("fecha_publicacion", "autor", "categoria")
    date_hierarchy = "fecha_publicacion"


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "biografia")
    search_fields = ("user__username", "user__email", "biografia")

