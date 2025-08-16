# colchoes/signals.py

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, Comparison

@receiver(post_save, sender=Product)
def create_comparison_on_new_product(sender, instance, created, **kwargs):
    """
    Cria uma comparação automática quando um novo produto é criado.
    - Prioriza `main_competitor` se definido.
    - Caso contrário, compara com o último produto criado.
    - Evita duplicações de comparações.
    """
    if not created:
        return  # só roda na criação de um produto novo

    # Define concorrente: main_competitor se existir, senão último produto criado
    competitor = instance.main_competitor
    if not competitor:
        competitor = Product.objects.exclude(pk=instance.pk).order_by('-created_at').first()
    
    if competitor:
        # Evita duplicação: verifica A vs B e B vs A
        if not Comparison.objects.filter(
            models.Q(product1=instance, product2=competitor) |
            models.Q(product1=competitor, product2=instance)
        ).exists():
            Comparison.objects.create(product1=instance, product2=competitor)
