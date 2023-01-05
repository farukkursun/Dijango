# Generated by Django 4.1.5 on 2023-01-05 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.CharField(blank=True, choices=[('TR', 'Turkey'), ('EN', 'England'), ('DE', 'Germany'), ('FR', 'France')], default='DE', max_length=2, null=True),
        ),
    ]
