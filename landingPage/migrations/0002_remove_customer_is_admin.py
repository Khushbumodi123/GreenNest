# Generated by Django 5.0.6 on 2024-07-16 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingPage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='is_admin',
        ),
    ]