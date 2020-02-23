from rest_framework.viewsets import ModelViewSet

from .models import User, Topic, Post
from .serializers import UserSerializer, TopicSerializer, PostsSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
