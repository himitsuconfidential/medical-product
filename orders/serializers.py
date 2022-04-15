from rest_framework import serializers

class MedicalProductSerializer(serializers.Serializer):
    #id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField()
