from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MedicalProduct

@api_view(['GET',])
def total_products(request):
    count = MedicalProduct.objects.count()
    return Response({'total_products': count})
