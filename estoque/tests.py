from django.test import TestCase
from .models import Ingrediente
# Create your tests here.

class ControleEstoqueTest(TestCase):

    def test_reposicao_normal(self):

        ingrediente = Ingrediente.objects.create(
            nome='Farinha',
            unidade='Kg',
            meta=20,
            estoque_atual=8,
            consumo=12,
            venceu=False,
            acabou_antes=False
        )

        quantidade = ingrediente.meta - ingrediente.estoque_atual

        self.assertEqual(quantidade, 12)

    def test_ingrediente_vencido(self):

        ingrediente = Ingrediente.objects.create(
            nome='Leite',
            unidade='Litro',
            meta=30,
            estoque_atual=10,
            consumo=20,
            venceu=True,
            acabou_antes=False
        )

        if ingrediente.venceu:
            quantidade = ingrediente.meta

        self.assertEqual(quantidade, 30)

    def test_ingrediente_acabou_antes(self):

        ingrediente = Ingrediente.objects.create(
            nome='Ovo',
            unidade='Unidade',
            meta=100,
            estoque_atual=0,
            consumo=100,
            venceu=False,
            acabou_antes=True
        )

        quantidade = ingrediente.consumo * 1.20

        self.assertEqual(quantidade, 120)