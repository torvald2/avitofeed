from django.db import models
from rest_framework import serializers
from feed.models import Platform, Table, Category, Cell


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Category
        fields = ("id","Platform","Name","Description","XML_Value","Table","subcategory", "Parent")
        extra_kwargs = { 'Table': {'required': False},'subcategory': {'required': False}, 'Parent': {'required': False}}

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields='__all__'

class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = '__all__'
        extra_kwargs= {'values':{"required":False},"max_len":{"required":False},"fieldForDisplay":{"required":False},"valueForDisplay":{"required":False}}