from rest_framework import serializers


class GDdriveSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    data = serializers.CharField()
