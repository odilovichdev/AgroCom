from rest_framework import serializers

from drugs.models import AgroProductImage
from drugs.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    """
        🛒 Categoriya uchun serializer.
        - `id`: Categoriyani ID raqami
        - `name`: Category nomi
        - `desc`: Category tavsifi
        """
    class Meta:
        model = Category
        fields = ["id", "name", 'desc']


class ProductSerializer(serializers.Serializer):
    """
        🛒 Mahsulotlar uchun serializer.
        - `id`: Mahsulotning ID raqami
        - `name`: Mahsulot nomi
        - `price`: Mahsulot narxi
        """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    status = serializers.CharField()
    desc = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    category = serializers.SerializerMethodField()
    icon = serializers.ImageField(required=False)
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = AgroProductImage.objects.filter(product=obj)
        return [img.image.url for img in images] if images.exists() else []

    def get_category(self, obj):
        return CategorySerializer(instance=obj.category).data