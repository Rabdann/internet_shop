from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from product.views import ProductViewSet, AddToCartAPIView, SentOrderAPIView

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')

url_patterns = [
    path("", include(router.urls)),
    path("auth/", include('rest_framework.urls')),
    path("products/<int:pk>/add-to-cart/", AddToCartAPIView.as_view()),
    path("sent-order/", SentOrderAPIView.as_view()),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(url_patterns)),
]
