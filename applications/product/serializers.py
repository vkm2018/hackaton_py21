from rest_framework import serializers

from applications.product.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'




class ProductSerializer(serializers.ModelSerializers):

    class Meta:
        model = Product
        fields = '__all__'



