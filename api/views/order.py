from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Order
from ..serializers import OrderSerializer
from drf_yasg.utils import swagger_auto_schema

@api_view(['GET'])
def orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response({'orders': serializer.data})

@swagger_auto_schema(methods=['POST'], request_body=OrderSerializer)
@api_view(['POST'])
def createOrder(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def orderDetail(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return Response(status=404)
    serializer = OrderSerializer(order)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=OrderSerializer)
@api_view(['PUT'])
def updateOrder(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return Response(status=404)
    serializer = OrderSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteOrder(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return Response(status=404)
    order.delete()
    return Response(status=204)
