from django.db import models


class Offer(models.Model):
    product_url = models.TextField(unique=True)
    product_id = models.IntegerField(blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    checked_at = models.DateTimeField(blank=True, null=True)
    product_url_slug = models.TextField(blank=True, null=True)
    brand_id = models.IntegerField(blank=True, null=True)
    heading = models.TextField(blank=True, null=True)
    category_slug = models.TextField(blank=True, null=True)
    f_eol = models.BooleanField(blank=True, null=True)
    f_sol = models.BooleanField(blank=True, null=True)
    heading_clean = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offers'


class Price(models.Model):
    product_id = models.IntegerField(blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    checked_at = models.DateTimeField(blank=True, null=True)
    offer_id = models.ForeignKey('Offer', models.CASCADE, blank=True, null=True)
    brand_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prices'


class EntriesCrs(models.Model):
    c_url_source = models.TextField(blank=True, null=True)
    c_url_product = models.TextField(blank=True, null=True)
    c_heading = models.TextField(blank=True, null=True)
    c_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    brand_id = models.IntegerField(blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    f_duplicate = models.BooleanField(blank=True, null=True)
    f_eol = models.BooleanField(blank=True, null=True)
    f_moved = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    checked_at = models.DateTimeField(blank=True, null=True)
    offer = models.ForeignKey('Offer', models.SET_NULL, blank=True, null=True)
    f_sol = models.BooleanField(blank=True, null=True)
    category_slug = models.TextField(blank=True, null=True)
    migration_source = models.TextField(blank=True, null=True)
    heading_clean = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entries_crs'
