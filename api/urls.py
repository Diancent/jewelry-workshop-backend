from django.urls import path
from . import views

urlpatterns = [

    # Customers
    path('customers', views.customer.customers, name='getAllCustomers'),
    path('customers/create', views.customer.createCustomer, name='createCustomer'),
    path('customers/<uuid:customer_id>', views.customer.customerDetail, name='getCustomer'),
    path('customers/<uuid:customer_id>/update', views.customer.updateCustomer, name='updateCustomer'),
    path('customers/<uuid:customer_id>/delete', views.customer.deleteCustomer, name='deleteCustomer'),

    # Orders
    path('orders', views.order.orders, name='getAllOrders'),
    path('orders/create', views.order.createOrder, name='createOrder'),
    path('orders/<uuid:order_id>', views.order.orderDetail, name='getOrder'),
    path('orders/<uuid:order_id>/update', views.order.updateOrder, name='updateOrder'),
    path('orders/<uuid:order_id>/delete', views.order.deleteOrder, name='deleteOrder'),

    # Products
    path('products', views.product.products, name='getAllProducts'),
    path('products/create', views.product.createProduct, name='createProduct'),
    path('products/<uuid:product_id>', views.product.productDetail, name='getProduct'),
    path('products/<uuid:product_id>/update', views.product.updateProduct, name='updateProduct'),
    path('products/<uuid:product_id>/delete', views.product.deleteProduct, name='deleteProduct'),

    # Artisans
    path('artisans', views.artisan.artisans, name='getAllArtisans'),
    path('artisans/create', views.artisan.createArtisan, name='createArtisan'),
    path('artisans/<uuid:artisan_id>', views.artisan.artisanDetail, name='getArtisan'),
    path('artisans/<uuid:artisan_id>/update', views.artisan.updateArtisan, name='updateArtisan'),
    path('artisans/<uuid:artisan_id>/delete', views.artisan.deleteArtisan, name='deleteArtisan'),

    # Materials
    path('materials', views.material.materials, name='getAllMaterials'),
    path('materials/create', views.material.createMaterial, name='createMaterial'),
    path('materials/<uuid:material_id>', views.material.materialDetail, name='getMaterial'),
    path('materials/<uuid:material_id>/update', views.material.updateMaterial, name='updateMaterial'),
    path('materials/<uuid:material_id>/delete', views.material.deleteMaterial, name='deleteMaterial'),
]