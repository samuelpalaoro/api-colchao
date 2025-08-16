
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, Comparison

@receiver(post_save, sender=Product)
def create_comparison_on_new_product(sender, instance, created, **kwargs):
    if created:
        last_product = Product.objects.exclude(pk=instance.pk).order_by('created_at').first()
        if last_product:
            if not Comparison.objects.filter(product1=instance, product2=last_product).exists() and \
               not Comparison.objects.filter(product1=last_product, product2=instance).exists():
                Comparison.objects.create(product1=instance, product2=last_product)
