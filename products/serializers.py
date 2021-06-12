from rest_framework import serializers
from .models import Product, Brand, ModelKey, BrandKey


class BrandKeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandKey
        fields = ('key',)


class BrandSerializer(serializers.ModelSerializer):
    keys = BrandKeysSerializer(many=True, read_only=True)
    class Meta:
        model = Brand
        fields = ('id', 'name', 'keys')


class ModelKeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelKey
        fields = ('key', 'created_at')


class ProductSerializer(serializers.ModelSerializer):
    keys = serializers.SlugRelatedField(many=True, read_only=True, slug_field="key")
    brand = serializers.SlugRelatedField(read_only=True, slug_field="name")
    class Meta:
        model = Product
        model._meta.ordering = ['-id']
        
        fields = ('id',
                  'commercial_code',
                  'category',
                  'official',
                  'brand',
                  'brand_id',
                  'keys',
                  'created_at',
                  'updated_at',
                  'first_active',
                  'last_active')
