from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Material
from ..serializers import MaterialSerializer
from drf_yasg.utils import swagger_auto_schema


@api_view(['GET'])
def materials(request):
    materials = Material.objects.all()
    serializer = MaterialSerializer(materials, many=True)
    return Response({'materials': serializer.data})

@swagger_auto_schema(methods=['POST'], request_body=MaterialSerializer)
@api_view(['POST'])
def createMaterial(request):
    serializer = MaterialSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def materialDetail(request, material_id):
    try:
        material = Material.objects.get(pk=material_id)
    except Material.DoesNotExist:
        return Response(status=404)
    serializer = MaterialSerializer(material)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=MaterialSerializer)
@api_view(['PUT'])
def updateMaterial(request, material_id):
    try:
        material = Material.objects.get(pk=material_id)
    except Material.DoesNotExist:
        return Response(status=404)
    serializer = MaterialSerializer(material, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteMaterial(request, material_id):
    try:
        material = Material.objects.get(pk=material_id)
    except Material.DoesNotExist:
        return Response(status=404)
    material.delete()
    return Response(status=204)