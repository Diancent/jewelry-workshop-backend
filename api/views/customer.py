from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Customer
from ..serializers import CustomerSerializer
from drf_yasg.utils import swagger_auto_schema


@api_view(['GET'])
def customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response({'customers': serializer.data})

@swagger_auto_schema(methods=['POST'], request_body=CustomerSerializer)
@api_view(['POST'])
def createCustomer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def customerDetail(request, customer_id):
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        return Response(status=404)
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=CustomerSerializer)
@api_view(['PUT'])
def updateCustomer(request, customer_id):
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        return Response(status=404)
    serializer = CustomerSerializer(customer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteCustomer(request, customer_id):
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        return Response(status=404)
    customer.delete()
    return Response(status=204)