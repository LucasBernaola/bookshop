from rest_framework import viewsets
from .models import Category, Product, CarouselProduct
from .serializers import CategorySerializer, ProductSerializer, CarouselProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CarouselProductListViewSet(viewsets.ModelViewSet):
    queryset = CarouselProduct.objects.all()
    serializer_class = CarouselProductSerializer



class ProductSearchView(APIView):
    def get(self, request):
        search_query = request.query_params.get('q', '')
        if search_query:
            products = Product.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
            serialized_products = []
            for product in products:
                serialized_product = ProductSerializer(product).data
                serialized_product['image'] = request.build_absolute_uri(product.image.url)
                serialized_products.append(serialized_product)
            return Response(serialized_products)
        else:
            return Response("No search query provided", status=status.HTTP_400_BAD_REQUEST)


