# Generated by Django 4.2.7 on 2023-11-28 02:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="created",
            field=models.DateTimeField(
                auto_created=True, default=django.utils.timezone.now
            ),
        ),
    ]