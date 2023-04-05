from django.urls import path

from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name="lista"),
    path('<slug>', views.DetalheProdutos.as_view(), name="detalhe"),
    path('adicionaraocarrinho/', views.AdicionarAoCarinho.as_view(),
         name="adicionaraoCarinho"),
    path('removerdocarinhos/', views.RemoverDoCarinho.as_view(),
         name="removerdocarinhos"),
    path('carinho/', views.Carinho.as_view(), name="carinho"),
    path('finalizar/', views.Finalizar.as_view(), name="finalizar"),
]
