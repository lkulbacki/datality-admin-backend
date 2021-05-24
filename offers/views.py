from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import Offer
from .serializers import OfferSerializer

class OfferViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin, 
                   viewsets.GenericViewSet):
    """
    Retrieves offers as a list or single entry
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (AllowAny,)
