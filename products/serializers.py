from rest_framework import serializers
from .models import Product, Brand, ModelKey, BrandKey


class BrandKeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandKey
        fields = ('key',)


class BrandSerializerNoKeys(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')


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
    keys = ModelKeysSerializer(many=True, read_only=True)
    brand = BrandSerializerNoKeys(read_only=True)
    class Meta:
        model = Product
        model._meta.ordering = ['-id']
        
        fields = ('id',
                  'commercial_code',
                  'category',
                  'official',
                  'brand',
                  'keys',
                  'created_at',
                  'updated_at',
                  'first_active',
                  'last_active')

