from django.urls import path
from . import views
from divulgar.models import Pet

urlpatterns = [
    path('', views.listar_pets, name="listar_pets"),
    path('pedido_adocao/<int:id_pet>', views.pedido_adocao, name="pedido_adocao"),
    path('processa_pedido_adocao/<int:id_pedido>', views.processa_pedido_adocao, name="processa_pedido_adocao"),
]