from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import User, Topic, Post
from .serializers import UserSerializer, TopicSerializer, PostsSerializer
from users.auth import MyAuthentication


# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class PostViewSet(ModelViewSet):
    authentication_classes = (MyAuthentication, SessionAuthentication, )
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
