from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from order.models import OrderProduct
from product.models import Product
from product.serializers import ProductSerializer, AddtoCardSerializer, CreateOrderSerializer


class IsAdmingOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.is_staff
        )


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdmingOrReadOnly,)


class AddToCartAPIView(GenericAPIView):
    serializer_class = AddtoCardSerializer

    def post(self, request, pk):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product_id = self.kwargs.get("pk")
        product = Product.objects.get(id=product_id)
        serializer.save(product=product)
        return Response(data=serializer.data)


class SentOrderAPIView(GenericAPIView):
    serializer_class = CreateOrderSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
