from rest_framework import serializers

from product.models import Product
from order.models import Order, OrderProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'phone',
                  'mail', 'adrress', 'payment_method']

    def create(self, validated_data):
        order = Order.objects.get(
            session_key=self.context.get('request').session.session_key)
        print(order)
        order.status = Order.Status.ordered.value
        # order.name = validated_data.get('name')
        # order.surname = validated_data.get('surname')
        # order.phone = validated_data.get('phone')
        # order.mail = validated_data.get('mail')
        for field in self.__class__.Meta.fields:
            setattr(order, field, validated_data.get(field))
        order.save()
        return order


class AddtoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['weight', 'count']

    def create(self, validated_data):
        session = self.context.get('request').session
        print(session.session_key, '------------------------')
        if session:
            session.save()
        order, _ = Order.objects.get_or_create(session_key=session.session_key)
        validated_data.update({
            'order': order
        })
        instance = super().create(validated_data)
        return instance
