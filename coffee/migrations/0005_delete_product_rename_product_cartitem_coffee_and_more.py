# Generated by Django 5.1.4 on 2024-12-26 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0004_remove_cartitem_cart_alter_cartitem_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='product',
            new_name='coffee',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='coffee.cart'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coffee',
            name='image',
            field=models.URLField(max_length=2038),
        ),
    ]
