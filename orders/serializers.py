from rest_framework import serializers
from .models import MedicalProduct, Order
class MedicalProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalProduct
        fields = ['name', 'description']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"