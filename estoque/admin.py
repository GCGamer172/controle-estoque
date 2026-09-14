from django.contrib import admin
from .models import Ingrediente
# Register your models here.


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'unidade',
        'meta',
        'estoque_atual',
        'consumo',
        'venceu',
        'acabou_antes'
    )