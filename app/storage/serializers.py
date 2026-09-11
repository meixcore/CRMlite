from rest_framework import serializers

from .models import Storage, Product


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = [
            'id',
            'address',
            'company',
        ]
        read_only_fields = [
            'company',
        ]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'purchase_price',
            'sale_price',
            'quantity',
            'storage',
        ]
        read_only_fields = [
            'id',
            'quantity',
        ]

        def validate_storage(self, storage):
            request = self.context["request"]

            if storage.company_id != request.user.company_id:
                raise serializers.ValidationError("Этот склад не принадлежит вашей компании")

            return storage