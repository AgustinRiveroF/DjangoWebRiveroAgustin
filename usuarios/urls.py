from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("login/", views.iniciar_sesion, name="login"),
    path("registro/", views.registro, name="registro"),
    path("logout/", views.cerrar_sesion, name="logout"),
    path("perfil/", views.perfil, name="perfil"),
    path("editar_perfil/", views.editar_perfil, name="editar_perfil"),
    path('detalle_post/<int:id>/', views.detalle_post, name='detalle_post'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

