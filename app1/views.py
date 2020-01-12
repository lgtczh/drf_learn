from app1.models import Post
from app1.serializers import PostSerializers
from rest_framework import generics


# Create your views here.
class PostList(generics.RetrieveAPIView):
    serializer_class = PostSerializers
    lookup_url_kwarg = "ns"

    def get_queryset(self):
        return Post.objects.all()

