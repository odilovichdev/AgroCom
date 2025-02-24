from rest_framework import permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from drugs.models import AgroProduct, Category
from drugs.serializers import ProductSerializer, CategorySerializer


class CategoryListAPIView(APIView):
    """
        🛍️ Category API
        ---
        - **GET** `/agro-product/categories/` - Barcha categoriyalarni olish

        """

    def get(self, request):
        all_ctg = Category.objects.all()
        serializer = CategorySerializer(all_ctg, many=True)
        data = {
            "success": True,
            "all_ctg": serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)


class AgroProductListView(APIView):
    """
        🛍️ Barcha turdagi dorilar uchun API
        ---
        - **GET** `/agro-product/` - Barcha mahsulotlarni olish

        """

    def get(self, request):
        products = AgroProduct.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class AgroProductDetailView(APIView):
    """
        🛍️ Bitta dori uchun API
        ---
        - **GET** `/agro-product/1/` - Bitta mahsulotlarni olish

        """

    def get(self, request, id):
        product = get_object_or_404(AgroProduct, id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)




class DrugListAPIView(APIView):
    """
        🛍️ Statusi Dori bo'lgan mavsulot uchun API
        ---
        - **GET** `/agro-product/drugs/` - Barcha mahsulotlarni olish

        """

    def get(self, request):
        all_drugs = AgroProduct.objects.filter(status=AgroProduct.Status.DRUG)
        srl_category = ProductSerializer(all_drugs, many=True)
        data = {
            "status": True,
            "data": srl_category.data
        }
        return Response(data)


class FertilizerListApiView(APIView):
    """
        🛍️ Statusi O'g'it bo'lgan mahsulotlar uchun API
        ---
        - **GET** `/agro-product/fertilizers/` - Barcha mahsulotlarni olish

        """

    def get(self, request):
        all_fertilizers = AgroProduct.objects.filter(status=AgroProduct.Status.FERTILIZER)
        srl_category = ProductSerializer(all_fertilizers, many=True)
        data = {
            "status": True,
            "data": srl_category.data
        }
        return Response(data)