from django.urls import path
from .views import CategoryViewSet, ProductViewSet, CarouselProductListViewSet, ProductSearchView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')
router.register('carousel', CarouselProductListViewSet, basename='carousel')

urlpatterns = [
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
]

urlpatterns += router.urls