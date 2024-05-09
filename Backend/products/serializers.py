from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import Category, Product, CarouselProduct

class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
        }


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'category', 'description', 'price', 'price_type')
        filterset_class = ProductFilter


class CategorySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)

    def get_image_url(self, obj):
        return obj.image_url()

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'image_url', 'products']


class CarouselProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselProduct
        fields = ['id', 'name', 'description', 'image']