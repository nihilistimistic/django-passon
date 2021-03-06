# Generated by Django 2.1.1 on 2018-10-06 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20181006_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='buyer',
            field=models.ForeignKey(default=None, on_delete=models.SET(None), related_name='bike_buyer', to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bike_seller', to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='book',
            name='buyer',
            field=models.ForeignKey(default=None, on_delete=models.SET(None), related_name='book_buyer', to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='book',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_seller', to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='item',
            name='buyer',
            field=models.ForeignKey(default=None, on_delete=models.SET(None), related_name='item_buyer', to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='item',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_seller', to='accounts.Profile'),
        ),
    ]
