# Generated by Django 5.0.6 on 2024-07-13 00:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("landingPage", "0005_alter_product_description_alter_product_rating_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
