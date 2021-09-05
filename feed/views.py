from rest_framework.views import APIView
from rest_framework.response import Response
from feed.models import Platform
from rest_framework import status
from feed.serializers import PlatformSerializer


class PlatformList(APIView):
    def get(self, request, format=None):
        platforms = Platform.objects.all()
        sefializer = PlatformSerializer(platforms, many=True)
        return  Response(sefializer.data)

    def post(self, request, format=None):
        serializer = PlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

