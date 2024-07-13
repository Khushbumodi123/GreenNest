# Generated by Django 5.0.6 on 2024-07-13 00:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("landingPage", "0006_delete_customuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="customer",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="customer",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
    ]