from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MedicalProduct
from .serializers import MedicalProductSerializer

@api_view(['GET',])
def total_products(request):
    count = MedicalProduct.objects.count()
    return Response({'total_products': count})

@api_view(['GET',])
def all_products(request):
    products = MedicalProduct.objects.all()
    product_serializer = MedicalProductSerializer(products, many=True)
    return Response(product_serializer.data)
