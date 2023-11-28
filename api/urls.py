from django.urls import path
from . import views

urlpatterns = [
    # Customers
    path('customers', views.customers, name='getAllCustomers'),
    path('customers/create', views.createCustomer, name='createCustomer'),
    path('customers/<uuid:customer_id>', views.customerDetail, name='getCustomer'),
    path('customers/<uuid:customer_id>/update/', views.updateCustomer, name='updateCustomer'),
    path('customers/<uuid:customer_id>/delete', views.deleteCustomer, name='deleteCustomer'),

    # # Orders
    # path('orders', views.getAllOrders, name='get_all_orders'),
    # path('orders/<int:order_id>', views.getOrder, name='get_order'),
    # path('orders', views.createOrder, name='create_order'),
    # path('orders/<int:order_id>', views.updateOrder, name='update_order'),
    # path('orders/<int:order_id>', views.deleteOrder, name='delete_order'),
    #
    # # Products
    # path('products', views.getAllProducts, name='get_all_products'),
    # path('products/<uuid:product_id>', views.getProduct, name='get_product'),
    # path('products', views.createProduct, name='create_product'),
    # path('products/<uuid:product_id>', views.updateProduct, name='update_product'),
    # path('products/<uuid:product_id>', views.deleteProduct, name='delete_product'),
]