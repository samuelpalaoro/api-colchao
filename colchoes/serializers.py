from rest_framework import serializers
from .models import Brand, MattressType, Product

# Estes serializers simples são usados para a LEITURA (GET)
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'logo_url', 'description']

class MattressTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MattressType
        fields = ['name', 'description']

# O Serializer principal do Produto, agora com a lógica correta
class ProductSerializer(serializers.ModelSerializer):

    # --- CAMPOS PARA LEITURA (read_only=True) ---
    # Quando você fizer um GET, estes campos mostrarão os dados completos da marca e do tipo.
    brand = BrandSerializer(read_only=True)
    mattress_type = MattressTypeSerializer(read_only=True)

    # --- CAMPOS PARA ESCRITA (write_only=True) ---
    # Quando você fizer um POST, você usará estes campos para enviar apenas o NOME.
    brand_name = serializers.CharField(write_only=True)
    mattress_type_name = serializers.CharField(write_only=True)

    class Meta:
        model = Product
        # Incluímos todos os campos do modelo, mais os nossos campos customizados de escrita.
        fields = '__all__'

    def create(self, validated_data):
        """
        Este método agora funciona como esperado, pois a validação não nos bloqueia mais.
        """
        # 1. Retiramos os nomes dos dados validados.
        brand_name = validated_data.pop('brand_name')
        mattress_type_name = validated_data.pop('mattress_type_name')

        # 2. Usamos a lógica "get_or_create" para buscar ou criar as instâncias.
        brand_instance, _ = Brand.objects.get_or_create(name=brand_name)
        mattress_type_instance, _ = MattressType.objects.get_or_create(name=mattress_type_name)

        # 3. Criamos o produto, passando as INSTÂNCIAS corretas para os campos ForeignKey.
        product = Product.objects.create(
            brand=brand_instance,
            mattress_type=mattress_type_instance,
            **validated_data
        )
        return product

    def to_representation(self, instance):
        """
        Garante que os campos de escrita não apareçam na resposta.
        """
        representation = super().to_representation(instance)
        representation.pop('brand_name', None)
        representation.pop('mattress_type_name', None)
        return representation
