# ---------------------------- 1 ----------------------------
# from django.contrib.auth.models import User
# from rest_framework import generics
#
# from users.serializers import UserSerializer
#
#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# ---------------------------- 2 ----------------------------
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from users.serializers import UserSerializer
from django.conf import settings
from django.db.models.signals import post_save


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # user: admin, password: 123456
    # other user: user: xxx, password: xxx123456
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

