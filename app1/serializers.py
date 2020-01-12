from rest_framework import serializers

from app1.models import Post


class PostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', "created")
