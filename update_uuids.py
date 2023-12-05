import os
import django

# Налаштування Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jewelry_workshop.settings')
django.setup()

# Залишений код
from base.models import Order

def update_order_uuids():
    orders = Order.objects.all()

    for order in orders:
        order.customer_id = order.customer.customer_id
        order.save()

if __name__ == "__main__":
    update_order_uuids()
