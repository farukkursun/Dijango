# Generated by Django 4.1.5 on 2023-01-05 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='clarusway.png', null=True, upload_to='product/'),
        ),
    ]
