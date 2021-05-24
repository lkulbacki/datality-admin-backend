from rest_framework import serializers
from .models import Offer

class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = ('id', 
                  'brand_id', 
                  'product_id',
                  'shop_id',
                  'heading',
                  'heading_clean',
                  'product_url',
                  'product_url_slug',
                  'category_slug',
                  'f_eol',
                  'f_sol',
                  'created_at',
                  'updated_at',
                  'checked_at')
