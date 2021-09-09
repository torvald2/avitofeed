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
