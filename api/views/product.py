from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Product
from ..serializers import ProductSerializer
from drf_yasg.utils import swagger_auto_schema

@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response({'orders': serializer.data})

@swagger_auto_schema(methods=['POST'], request_body=ProductSerializer)
@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def productDetail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=ProductSerializer)
@api_view(['PUT'])
def updateProduct(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteProduct(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response(status=404)
    product.delete()
    return Response(status=204)
