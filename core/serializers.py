from rest_framework import serializers
from .models import Category, Door

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class DoorSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    image_url = serializers.ImageField(source='image', read_only=True)
    
    class Meta:
        model = Door
        fields = ['id', 'name', 'price', 'image', 'image_url', 'category', 'category_name', 'description', 'created_at']
        read_only_fields = ['created_at']
        extra_kwargs = {
            'image': {'write_only': True}
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Remove the image field from the response since we're using image_url
        if 'image' in representation:
            del representation['image']
        return representation
