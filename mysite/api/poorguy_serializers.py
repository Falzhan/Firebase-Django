from rest_framework import serializers
from poorguy.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id', 'title', 'price_php', 'grade', 'category', 
            'specs', 'cover_image', 'verdict', 'content', 
            'is_wishlist', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']