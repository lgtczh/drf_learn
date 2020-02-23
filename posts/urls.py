from posts import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'topics', views.TopicViewSet)
router.register(r'posts', views.PostViewSet, basename="posts")

urlpatterns = router.urls
