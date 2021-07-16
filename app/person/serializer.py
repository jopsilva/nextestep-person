from rest_framework import serializers
from person.models import Type

class TypeSerializar(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']