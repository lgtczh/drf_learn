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
from rest_framework import viewsets

from users.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

