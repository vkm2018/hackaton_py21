from django.shortcuts import render

# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from applications.product.models import Category, Product
from applications.product.permissions import CustomIsAdmin
from applications.product.serializers import CategorySerializer, ProductSerializer


class LargeResultSetPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 1000


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LargeResultSetPagination
    permission_classes = CustomIsAdmin


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer






