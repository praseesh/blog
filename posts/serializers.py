from rest_framework import serializers
from .models import Posts, Category

class PostCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['title', 'content', 'categories','created_at']
    
    def validate_title(self,value):
        if len(value) < 4:
            serializers.ValidationError('title must be 4 character')
        return value
    
    def validate_content(self, value):
        if len(value) < 20:
            raise serializers.ValidationError("Content must be at least 10 characters long.")
        return value
        
        
class PostModifySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Posts
        fields = ['title', 'content', 'categories']
        
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 4 characters long.")
        return value

    def validate_content(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Content must be at least 10 characters long.")
        return value