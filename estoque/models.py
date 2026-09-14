from django.db import models

# Create your models here.
class Ingrediente(models.Model):

    UNIDADES = [
        ('Kg', 'Kg'),
        ('Litro', 'Litro'),
        ('Unidade', 'Unidade'),
    ]

    nome = models.CharField(max_length=100)
    unidade = models.CharField(max_length=20, choices=UNIDADES)
    meta = models.DecimalField(max_digits=10, decimal_places=2)
    estoque_atual = models.DecimalField(max_digits=10, decimal_places=2)
    consumo = models.DecimalField(max_digits=10, decimal_places=2)
    venceu = models.BooleanField(default=False)
    acabou_antes = models.BooleanField(default=False)

    def __str__(self):
        return self.nome