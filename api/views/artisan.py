from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Artisan
from ..serializers import ArtisanSerializer
from drf_yasg.utils import swagger_auto_schema


@api_view(['GET'])
def artisans(request):
    artisans = Artisan.objects.all()
    serializer = ArtisanSerializer(artisans, many=True)
    return Response({'artisans': serializer.data})

@swagger_auto_schema(methods=['POST'], request_body=ArtisanSerializer)
@api_view(['POST'])
def createArtisan(request):
    serializer = ArtisanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def artisanDetail(request, artisan_id):
    try:
        artisan = Artisan.objects.get(pk=artisan_id)
    except Artisan.DoesNotExist:
        return Response(status=404)
    serializer = ArtisanSerializer(artisan)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=ArtisanSerializer)
@api_view(['PUT'])
def updateArtisan(request, artisan_id):
    try:
        artisan = Artisan.objects.get(pk=artisan_id)
    except Artisan.DoesNotExist:
        return Response(status=404)
    serializer = ArtisanSerializer(artisan, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteArtisan(request, artisan_id):
    try:
        artisan = Artisan.objects.get(pk=artisan_id)
    except Artisan.DoesNotExist:
        return Response(status=404)
    artisan.delete()
    return Response(status=204)