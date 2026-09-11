from django.db import transaction
from rest_framework import serializers

from .models import Supplier, Supply, SupplyProduct
from storage.models import Product


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'id',
            'company',
            'title',
            'inn',
        ]
        read_only_fields = [
            'id',
            'company',
        ]


class SupplyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyProduct
        fields = [
            'id',
            'supply',
            'product',
            'quantity',
        ]

class SupplySerializer(serializers.ModelSerializer):
    supply_products = SupplyProductSerializer(many=True, read_only=True)

    class Meta:
        model = Supply
        fields = [
            'id',
            'supplier',
            'delivery_date',
            'supply_products',
        ]
        read_only_fields = [
            'id',
            'delivery_date',
        ]

class SupplyProductInputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

class SupplyCreateSerializer(serializers.Serializer):
    supplier_id = serializers.IntegerField()
    products = SupplyProductInputSerializer(many=True)

    @transaction.atomic
    def create(self, validated_data):
        supplier_id = validated_data['supplier_id']
        products_data = validated_data['products']

        request = self.context['request']
        user = request.user

        try:
            supplier = Supplier.objects.get(id=supplier_id, company=user.company)
        except Supplier.DoesNotExist:
            raise serializers.ValidationError({'supplier_id': 'Поставщик не найден в вашей компании'})

        supply = Supply.objects.create(supplier=supplier)

        for product_data in products_data:
            product_id = product_data['id']
            quantity = product_data['quantity']
            try:
                product = Product.objects.get(id=product_id, storage__company=user.company)
            except Product.DoesNotExist:
                raise serializers.ValidationError(
                    {'products': f'Товар с id={product_id} не найден в вашей компании'}
                )
            SupplyProduct.objects.create(supply=supply, product=product, quantity=quantity)
            product.quantity += quantity
            product.save(update_fields=['quantity'])

        return supply

