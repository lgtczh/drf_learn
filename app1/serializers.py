from rest_framework import serializers

from app1.models import Post


class PostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', "created")

    def validate_title(self, value):
        if 'drf' not in value.lower():
            raise serializers.ValidationError('Post必须和DRF相关, 不要灌水')
        return value
