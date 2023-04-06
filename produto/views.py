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
        variacao_estoque = variacao.estoque
        produto = variacao.produto

        produto_id = produto.id
        produto_nome = produto.nome
        variacao_nome = variacao.nome or ''
        variacao_id = variacao.id
        preco_unitario = variacao.preco
        preco_unitario_promocional = variacao.preco_promocional
        slug = produto.slug
        imagem = produto.imagem

        if imagem:
            imagem = imagem.name
        else:
            imagem = ''

        if variacao.estoque < 1:
            messages.error(self.request, "Indisponivel em Estoque")

            return redirect(http_referer)

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()

        carrinho = self.request.session['carrinho']

        if variacao_id in carrinho:
            quantidade_carrinho = carrinho[variacao_id]['quatidade']
            quantidade_carrinho += 1

            if variacao_estoque < quantidade_carrinho:
                messages.warning(
                    self.request,
                    f'Estoque insuficiente para {quantidade_carrinho}x no produto'
                    f'produto "{produto_nome}". adcionamos {variacao_estoque}x'
                    f'no seu carrinho.'
                )
                quantidade_carrinho = variacao_estoque
                carrinho[variacao_id]['quatidade'] = quantidade_carrinho
                carrinho[variacao_id]['preco_quantitativo'] = preco_unitario * \
                    quantidade_carrinho
                carrinho[variacao_id]['preco_quantitativo_promocional'] = preco_unitario_promocional * \
                    quantidade_carrinho


        else:
            carrinho[variacao_id] = {
                'produto_id': produto_id,
                'produto_nome': produto_nome,
                'variacao_nome': variacao_nome,
                'variacao_id': variacao_id,
                'preco_unitario': preco_unitario,
                'preco_unitario_promocional': preco_unitario_promocional,
                'preco_quantitativo': preco_unitario,
                'preco_quantitativo_promocional': preco_unitario_promocional,
                'quantidade': 1,
                'slug': slug,
                'imagem': imagem
            }

        self.request.session.save()
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
        return HttpResponse('Finalizar')
