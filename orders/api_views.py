from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MedicalProduct
from .serializers import MedicalProductSerializer, OrderSerializer
from rest_framework import generics
from rest_framework import viewsets
from orders.models import Order
import datetime
import json
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

@api_view(['GET',])
def OrdersView(request, **kwargs):
    #manager_name= kwargs['manager_name']
    #products_name= kwargs['products_name']

    #orders = Order.objects.filter(manager__name = manager_name, products__name = products_name)
    kwargs = json.loads(kwargs['json_dict'])
        
    if 'time' in kwargs:
        kwargs['time'] = datetime.datetime.fromisoformat(kwargs['time'])
    orders = Order.objects.filter(**kwargs)
    serializer = OrderSerializer(orders, many =True)
    return Response(serializer.data)