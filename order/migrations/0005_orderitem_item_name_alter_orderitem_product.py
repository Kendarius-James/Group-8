# Generated by Django 4.1.7 on 2023-04-30 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_quantity'),
        ('order', '0004_orderitem_return_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='item_name',
            field=models.CharField(default='Unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='product.product'),
        ),
    ]