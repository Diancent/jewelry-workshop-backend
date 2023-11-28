import uuid

from django.db import models
from django.utils import timezone

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_created=True,default=timezone.now)

class Customer(models.Model):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    material_id = models.UUIDField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_id = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('new', 'New'), ('inProgress', 'In Progress'), ('cancelled', 'Cancelled'), ('completed', 'Completed')])
    # Додайте зв'язок з OrderItem тут

class OrderItem(models.Model):
    order_id = models.UUIDField()
    product_id = models.UUIDField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Artisan(models.Model):
    artisan_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    specialization = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

class Material(models.Model):
    material_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()