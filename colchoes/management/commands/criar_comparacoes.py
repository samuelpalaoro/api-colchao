import itertools
from django.core.management.base import BaseCommand
from django.db.models import Q
from colchoes.models import Product, Comparison

class Command(BaseCommand):
    help = 'Cria páginas de comparação para todas as combinações de produtos existentes, sem duplicatas.'

    def handle(self, *args, **options):
        self.stdout.write('Iniciando a criação de comparações faltantes...')

        products = Product.objects.filter(is_active=True)
        product_pairs = itertools.combinations(products, 2)

        created_count = 0

        for product1, product2 in product_pairs:
            comparison_exists = Comparison.objects.filter(
                Q(product1=product1, product2=product2) |
                Q(product1=product2, product2=product1)
            ).exists()

            if not comparison_exists:
                Comparison.objects.create(product1=product1, product2=product2)
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'  -> Criada comparação: {product1.name} vs {product2.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'  -- Comparação já existe: {product1.name} vs {product2.name}'))

        self.stdout.write(self.style.SUCCESS(f'\nOperação concluída! {created_count} novas comparações foram criadas.'))
