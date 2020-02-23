from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # request header: {USERNAME: XXX}
        username = request.META.get("HTTP_USERNAME")
        if not username:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed("没有这个用户")
        else:
            return user, None  # (request.user, request.auth)
