# Generated by Django 4.1.7 on 2023-04-30 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0006_orderitem_buyeruser_orderitem_selleruser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='buyerUser',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='sellerUser',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer_order_item', to=settings.AUTH_USER_MODEL),
        ),
    ]
