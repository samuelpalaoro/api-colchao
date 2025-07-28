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

