# Generated by Django 3.2.4 on 2021-06-27 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stores', '0005_stores_sslug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='c_category',
            new_name='ccategory',
        ),
        migrations.RenameField(
            model_name='stores',
            old_name='sslug',
            new_name='slug',
        ),
    ]