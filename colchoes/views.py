from colchoes.models import Product
from rest_framework import generics
from colchoes.serializers import ProductSerializer

# Create your views here.
class ColchaoCreateListView(generics.ListCreateAPIView):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer

class ColchaoRetrieveUpdateDestroyView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'  # Usando slug como campo de lookup


from django.shortcuts import render, get_object_or_404
from .models import Comparison

def comparison_detail_view(request, slug):
    comparison = get_object_or_404(Comparison, slug=slug)
    product1 = comparison.product1
    product2 = comparison.product2

    context = {
        'product1': product1,
        'product2': product2,
        'comparison': comparison
    }
    return render(request, 'web/comparison_template.html', context)
