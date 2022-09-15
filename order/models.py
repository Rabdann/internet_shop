from django.db import models

from product.models import Product


class Order(models.Model):
    class Status(models.TextChoices):
        new = 'new', 'новый'
        ordered = 'ordered', 'оформлен'
        delivered = 'delivered', 'доставлен'
        canceled = 'canceled', 'отменен'

    class PaymentMethod(models.TextChoices):
        cash = 'cash', 'наличные'
        terminal = 'terminal', 'оплата картой через терминал'
        mobil_bank = 'mobil_bank', 'оплата переводом через мобильный банк'

    name = models.CharField(max_length=60, verbose_name='Имя', blank=True, null=True)
    surname = models.CharField(max_length=60, verbose_name='Фамилия', blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name='Телефон', blank=True, null=True)
    mail = models.EmailField(blank=True, null=True, verbose_name='Почта')
    adrress = models.CharField(max_length=255, verbose_name='Адрес', blank=True, null=True)
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.new.value)
    created = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=30, choices=PaymentMethod.choices, verbose_name='Способ оплаты', blank=True, null=True)
    session_key = models.CharField(max_length=60)

    def __str__(self):
        return f'Заказ {self.status} от {self.created} для {self.name} {self.surname}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, models.CASCADE, related_name='products', verbose_name='Заказы')
    product = models.ForeignKey(Product, models.CASCADE, related_name='orders', verbose_name='Продукты')
    count = models.PositiveSmallIntegerField(verbose_name='Количество', null=True, blank=True)
    weight = models.PositiveSmallIntegerField(verbose_name='Вес', null=True, blank=True)

    def __str__(self):
        return f'{self.count or self.weight} этого {self.product}'

    class Meta:
        verbose_name = 'Продукт в заказе'
        verbose_name_plural = 'Продукты в заказе'
