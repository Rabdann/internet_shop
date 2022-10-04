from django.db import models


class Product(models.Model):
    class Type(models.TextChoices):
        fruit = 'fruit', 'фрукт'
        vegetable = 'vegetable', 'овощ'

    name = models.CharField(max_length=60, verbose_name='Название')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель')
    price = models.IntegerField(verbose_name='Цена', help_text='в рублях')
    decription = models.TextField(verbose_name='Описание', blank=True, null=True)
    type = models.CharField(max_length=30, choices=Type.choices)

    @property
    def is_fruit(self):
        return self.type == self.__class__.Type.fruit.value

    @property
    def is_vegetable(self):
        return self.type == self.__class__.Type.vegetable.value

    def __str__(self):
        return f'{self.name} от {self.manufacturer}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
