from rest_framework import serializers
from feed.models import Platform, Table, Category, Cell


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    parentCategory = serializers.PrimaryKeyRelatedField(read_only=True)
    subcategories = SubCategorySerializer(read_only=True)
    platform = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Category
        fields = ('parentCategory',"platform","Name","Description","XML_Value","Table")
