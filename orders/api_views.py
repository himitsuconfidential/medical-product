from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MedicalProduct
from .serializers import MedicalProductSerializer
from rest_framework import generics
from rest_framework import viewsets

@api_view(['GET',])
def total_products(request):
    count = MedicalProduct.objects.count()
    return Response({'total_products': count})


class all_products(generics.ListAPIView):
    queryset = MedicalProduct.objects.all()
    serializer_class = MedicalProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = MedicalProduct.objects.all()
    serializer_class = MedicalProductSerializer
