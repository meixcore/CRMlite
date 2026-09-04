from rest_framework import serializers

from .models import Storage

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = [
            'id',
            'address',
            'company_id',
        ]
        read_only_fields = [
            'company_id',
        ]