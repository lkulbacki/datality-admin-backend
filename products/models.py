from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brands'

class BrandKey(models.Model):
    key = models.CharField(max_length=255, blank=True, null=True)
    brand = models.ForeignKey('Brand', models.PROTECT, related_name='keys', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brand_keys'


class Product(models.Model):
    brand_repr = models.TextField(blank=True, null=True)
    commercial_code = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    official = models.BooleanField(blank=True, null=True)
    brand = models.ForeignKey('Brand', models.PROTECT, related_name='products', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    first_active = models.DateTimeField(blank=True, null=True)
    last_active = models.DateTimeField(blank=True, null=True)
    merge = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class ModelKey(models.Model):
    key = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey('Product', models.PROTECT, related_name='keys', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model_keys'


class Shop(models.Model):
    name = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shops'


class ShopKey(models.Model):
    key = models.TextField(blank=True, null=True)
    shop = models.ForeignKey('Shop', models.PROTECT, related_name='keys', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_keys'
