from rest_framework import serializers
from Product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product.objects.all()
        fields = '__all__'

