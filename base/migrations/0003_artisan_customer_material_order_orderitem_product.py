# Generated by Django 4.2.7 on 2023-11-28 04:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_alter_item_created"),
    ]

    operations = [
        migrations.CreateModel(
            name="Artisan",
            fields=[
                (
                    "artisan_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("surname", models.CharField(max_length=255)),
                ("address", models.TextField()),
                ("phone_number", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("specialization", models.CharField(max_length=255)),
                ("salary", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "customer_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("surname", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("address", models.TextField()),
                ("phone_number", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Material",
            fields=[
                (
                    "material_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "order_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("customer_id", models.UUIDField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("inProgress", "In Progress"),
                            ("cancelled", "Cancelled"),
                            ("completed", "Completed"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_id", models.UUIDField()),
                ("product_id", models.UUIDField()),
                ("quantity", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "product_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("material_id", models.UUIDField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]