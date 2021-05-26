from rest_framework import viewsets, mixins, views, status
from rest_framework.permissions import AllowAny
from .models import Product, ModelKey
from .serializers import ProductSerializer, ProductSerializerCustom

from rest_framework.response import Response
from rest_framework import authentication, permissions
from IPython import embed

class ProductViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin, 
                   viewsets.GenericViewSet):
    """
    Retrieves products as a list or single entry
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)


class ProductViewCustom(views.APIView):
    """
    Retrieves selected product
    """
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializerCustom

    def get(self, request, pk, format=None):
        product = Product.objects.filter(id=pk).order_by('id').first()
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            keys = []
            for key in product.keys.all():
                keys.append(key.key)
            
            returned_product = {
                'id': pk,
                'brand': product.brand.name,
                'brand_id': product.brand.id,
                'commercial_code': product.commercial_code,
                'category': product.category,
                'created_at': product.created_at,
                'keys': keys,
                'created_at': product.created_at,
                'updated_at': product.updated_at,
                'first_active': product.first_active,
                'last_active': product.last_active,
                'official': product.official,
            }
            return Response(returned_product)
