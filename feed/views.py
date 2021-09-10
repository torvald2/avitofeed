from rest_framework.views import APIView
from rest_framework.response import Response
from feed import serializers
from feed.models import Platform, Category
from rest_framework import status
from feed.serializers import PlatformSerializer
from rest_framework import generics
from feed.serializers import CategorySerializer
import json
from rest_framework.exceptions import ValidationError

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


class CategoryList(APIView):
    
    def get(self, request):
        platform = request.query_params.get('platform')
        if platform:
            cats = Category.objects.filter(Platform=platform)
        else:
            cats = Category.objects.all()
        
        serializer = CategorySerializer(cats, many=True)
        return Response(serializer.data)
    
    def post(self,request, *args, **kwargs):
        try:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                serializer.data
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs ):
        pk = request.query_params.get('id')
        if pk:
            try:
                cat = Category.objects.get(pk=pk)
                cat.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                Response(str(e), status= status.HTTP_404_NOT_FOUND)
        else:
            Response("Bad PK", status= status.HTTP_400_BAD_REQUEST)


        
