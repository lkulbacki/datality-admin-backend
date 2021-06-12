import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..serializers import ProductSerializer
from ..models import Product, ModelKey, Brand
from IPython import embed

from rest_framework.test import APIClient

# initialize the APIClient app
client = Client()
api_client = APIClient()

class GetAllProductsTest(TestCase):
    """ Test module for GET all products API """
    databases = {'products'}

    def setUp(self):
        brand = Brand.objects.create(name='Bosch')
        product1 = Product.objects.create(commercial_code='A', brand=brand)
        ModelKey.objects.create(key='a', product=product1)
        product2 = Product.objects.create(commercial_code='B', brand=brand)
        ModelKey.objects.create(key='b', product=product2)

    def test_get_all_products(self):
        # get API response
        response = client.get(reverse('product-list'))

        # testing for exact data structure - after api stabilization
        # products = Product.objects.all()
        # serializer = ProductSerializer(products, many=True)
        # self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

class GetProductTest(TestCase):
    databases = {'products'}

    def setUp(self):
        self.product = Product.objects.create(
            commercial_code='A'
        )

    def test_get_all_products(self):
        response = api_client.get('/api/v1/products/{}/'.format(self.product.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # testing for exact data structure - after api stabilization
        # self.assertEqual(response.data, {'id': self.product.id, 'commercial_code':'A'})
