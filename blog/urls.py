from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear_post/', views.crear_post, name='crear_post'),
    path('crear_comentario/<int:post_id>/', views.crear_comentario, name='crear_comentario'),
    path('buscar/', views.buscar, name='buscar'),
]
