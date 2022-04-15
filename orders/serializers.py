from rest_framework import serializers
from .models import MedicalProduct
class MedicalProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalProduct
        fields = ['name', 'description']
