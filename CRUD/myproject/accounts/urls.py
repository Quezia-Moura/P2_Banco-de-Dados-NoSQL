from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    path('eventos/criar/', views.criar_evento, name='criar_evento'),
    path('eventos/<int:id>/atualizar/', views.atualizar_evento, name='atualizar_evento'),
    path('eventos/<int:id>/deletar/', views.deletar_evento, name='deletar_evento'),
]
