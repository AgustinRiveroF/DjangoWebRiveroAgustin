from django.urls import path
from home.views import HomeView, agregar_autor, agregar_categoria, agregar_post, buscar_post, portada, aboutme
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", portada, name="portada"),
    path("inicio/", HomeView.as_view(), name="home"),
    path("aboutme/", aboutme, name="aboutme"),
    path("buscar-post/", buscar_post, name="buscar_post"),
    path("agregar-post/", agregar_post, name="agregar_post"),
    path("agregar-autor/", agregar_autor, name="agregar_autor"),
    path('lista-posts/', PostListView.as_view(), name='lista_posts'),
    path('crear-post/', PostCreateView.as_view(), name='crear_post'),
    path("agregar-categoria/", agregar_categoria, name="agregar_categoria"),
    path('editar-post/<int:pk>/', PostUpdateView.as_view(), name='editar_post'),
    path('borrar-post/<int:pk>/', PostDeleteView.as_view(), name='borrar_post'),
    path('detalle-post/<int:pk>/', PostDetailView.as_view(), name='detalle_post'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
