from rest_framework.views import APIView
from rest_framework.response import Response
from feed.models import Platform, Category, Table, Cell
from rest_framework import status
from feed.serializers import CategorySerializer, PlatformSerializer, TableSerializer, CellSerializer

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

    def delete(self, request, *args, **kwargs ):
        pk = request.query_params.get('id')
        if pk:
            try:
                cat = Platform.objects.get(pk=pk)
                cat.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                Response(str(e), status= status.HTTP_404_NOT_FOUND)
        else:
            Response("Bad PK", status= status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = request.query_params.get('id')
        if pk:
            try:
                cat = Platform.objects.get(pk=pk)
                serializer = PlatformSerializer(cat,request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                Response(str(e), status= status.HTTP_404_NOT_FOUND)
        else:
            Response("Bad PK", status= status.HTTP_400_BAD_REQUEST)


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

    def put(self, request, *args, **kwargs):
        pk = request.query_params.get('id')
        if pk:
            try:
                cat = Category.objects.get(pk=pk)
                serializer = CategorySerializer(cat,request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                Response(str(e), status= status.HTTP_404_NOT_FOUND)
        else:
            Response("Bad PK", status= status.HTTP_400_BAD_REQUEST)


class TableList(APIView):
    
    def get(self, request):
        platform = request.query_params.get('platform')
        if platform:
            tables = Table.objects.filter(Platform=platform)
        else:
            tables = Table.objects.all()
        
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data)
    
    def post(self,request, *args, **kwargs):
        try:
            serializer = TableSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs ):
        pk = request.query_params.get('id')
        if pk:
            try:
                tbl = Table.objects.get(pk=pk)
                tbl.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                Response(str(e), status= status.HTTP_404_NOT_FOUND)
        else:
            Response("Bad PK", status= status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = request.query_params.get('id')
        if pk:
            try:
                tbl = Table.objects.get(pk=pk)
                serializer = TableSerializer(tbl,request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                Response(str(e), status= status.HTTP_404_NOT_FOUND)
        else:
            Response("Bad PK", status= status.HTTP_400_BAD_REQUEST)


class CellList(APIView):
    
    def get(self, request):
        table = request.query_params.get('table')
        if table:
            cels = Cell.objects.filter(table=table)
        else:
            cels = Cell.objects.all()
        
        serializer = CellSerializer(cels, many=True)
        return Response(serializer.data)
    
    def post(self,request, *args, **kwargs):
        try:
            serializer = CellSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs ):
        pk = request.query_params.get('id')
        if pk:
            try:
                tbl = Cell.objects.get(pk=pk)
                tbl.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                Response(str(e), status= status.HTTP_404_NOT_FOUND)
        else:
            Response("Bad PK", status= status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = request.query_params.get('id')
        if pk:
            try:
                tbl = Cell.objects.get(pk=pk)
                serializer = CellSerializer(tbl,request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                Response(str(e), status= status.HTTP_404_NOT_FOUND)
        else:
            Response("Bad PK", status= status.HTTP_400_BAD_REQUEST)