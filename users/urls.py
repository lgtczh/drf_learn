# ---------------------------- 1 ----------------------------
# from django.urls import path
#
# from users.views import UserList, UserDetail
#
# urlpatterns = [
#     path('', UserList.as_view()),
#     path('<int:pk>/', UserDetail.as_view())
# ]

# ---------------------------- 2 ----------------------------
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls
