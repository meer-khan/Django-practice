# Generated by Django 4.1 on 2022-08-28 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Products", new_name="Product",),
    ]
