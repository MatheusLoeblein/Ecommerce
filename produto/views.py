from django.contrib import messages
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from . import models

# Create your views here.


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10


class DetalheProdutos(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'


class AdicionarAoCarinho(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
        )
        variacao_id = self.request.GET.get('vid')
        print(variacao_id)

        if not variacao_id:
            messages.error(self.request, "Produto não existe")

            return redirect(http_referer)

        variacao = get_object_or_404(models.Variacao, id=variacao_id)

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()

        carrinho = self.request.session['carrinho']

        if variacao_id in carrinho:
            # TODO: variação existe no carrinho
            pass
        else:
            # TODO: variação nao existe no carrinho
            pass
        return HttpResponse(f'{variacao.produto}{variacao.name}')


class RemoverDoCarinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('RemoverDoCarinho')


class Carinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
