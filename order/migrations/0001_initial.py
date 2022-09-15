# Generated by Django 4.1 on 2022-08-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Имя')),
                ('surname', models.CharField(max_length=60, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('mail', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('adrress', models.CharField(max_length=255, verbose_name='Адрес')),
                ('status', models.CharField(choices=[('ordered', 'оформлен'), ('delivered', 'доставлен'), ('canceled', 'отменен')], max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.CharField(choices=[('cash', 'наличные'), ('terminal', 'оплата картой через терминал'), ('mobil_bank', 'оплата переводом через мобильный банк')], max_length=30)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
