# Generated by Django 4.1 on 2022-08-28 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_dummy"),
    ]

    operations = [
        migrations.DeleteModel(name="Dummy",),
    ]
