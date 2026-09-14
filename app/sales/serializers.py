from rest_framework import serializers
from django.db import transaction

from storage.models import Product
from .models import Sale, ProductSale


class ProductSaleInputSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

class SaleCreateSerializer(serializers.Serializer):
    buyer_name = serializers.CharField(max_length=100)
    product_sales = ProductSaleInputSerializer(many=True)

    @transaction.atomic
    def create(self, validated_data):
        buyer_name = validated_data['buyer_name']
        product_sales_data = validated_data['product_sales']
        request = self.context['request']
        user = request.user

        sale = Sale.objects.create(buyer_name=buyer_name, company=user.company)

        for item in product_sales_data:
            product_id = item['product_id']
            quantity = item['quantity']

            try:
                product = Product.objects.get(id=product_id, storage__company=user.company)
            except Product.DoesNotExist:
                raise serializers.ValidationError(
                    {'product_sales': f'Товар с id={product_id} не найден в вашей компании'}
                )

            if product.quantity < quantity:
                raise serializers.ValidationError(
                    {'product_sales': f'Недосточно товара id={product_id}. Доступно: {product.quantity}'}
                )

            ProductSale.objects.create(
                sale=sale,
                product=product,
                quantity=quantity
            )
            product.quantity -= quantity
            product.save(update_fields=['quantity'])
        return sale

class ProductSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSale
        fields = [
            'product',
            'quantity',
        ]

class SaleSerializer(serializers.ModelSerializer):
    product_sales = ProductSaleSerializer(many=True, read_only=True)
    class Meta:
        model = Sale
        fields = [
            'id',
            'buyer_name',
            'company',
            'sale_date',
            'product_sales',
        ]

class SaleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = [
            'buyer_name',
            'sale_date',
        ]