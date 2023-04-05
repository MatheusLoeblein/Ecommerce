from django.contrib import admin

from .models import Produto, Variacao

# Register your models here.


class Variacaoinline(admin.TabularInline):
    model = Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        Variacaoinline
    ]


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)
