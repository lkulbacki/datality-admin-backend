from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id',
                  'brand_repr',
                  'commercial_code',
                  'category',
                  'official',
                  'brand',
                  'created_at',
                  'updated_at',
                  'first_active',
                  'last_active')
