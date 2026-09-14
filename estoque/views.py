from django.shortcuts import render
from .models import Ingrediente
# Create your views here.

def lista_compras(request):

    ingredientes = Ingrediente.objects.all()

    compras = []

    for ingrediente in ingredientes:

        if ingrediente.venceu:

            quantidade = ingrediente.meta

        elif ingrediente.acabou_antes:

            quantidade = ingrediente.consumo * 1.20

        else:

            quantidade = ingrediente.meta - ingrediente.estoque_atual

        if quantidade > 0:

            compras.append({
                'nome': ingrediente.nome,
                'unidade': ingrediente.unidade,
                'quantidade': quantidade
            })

    return render(
        request,
        'estoque/lista_compras.html',
        {'compras': compras}
    )