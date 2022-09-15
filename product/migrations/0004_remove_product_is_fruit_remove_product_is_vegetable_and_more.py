# Generated by Django 4.1 on 2022-08-23 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_fruit',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_vegetable',
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('fruit', 'фрукт'), ('vegetable', 'овощ')], default='fruit', max_length=30),
            preserve_default=False,
        ),
    ]