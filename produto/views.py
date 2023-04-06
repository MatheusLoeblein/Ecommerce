from django.shortcuts import HttpResponse, render
from django.views import View
from django.views.generic.list import ListView

from . import models

# Create your views here.


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10


class DetalheProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse('DetalheProdutos')


class AdicionarAoCarinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('AdicionarAoCarinho')


class RemoverDoCarinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('RemoverDoCarinho')


class Carinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
