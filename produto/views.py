from django.shortcuts import HttpResponse, render
from django.views import View
from django.views.generic.list import ListView

# Create your views here.


class ListaProdutos(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('ListaProdutos')


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
