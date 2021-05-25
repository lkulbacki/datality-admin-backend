from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin, 
                   viewsets.GenericViewSet):
    """
    Retrieves products as a list or single entry
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
