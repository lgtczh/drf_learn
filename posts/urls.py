from posts import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts/users', views.UserViewSet)
router.register(r'posts/topics', views.TopicViewSet)
router.register(r'posts/posts', views.PostViewSet, basename="posts")

urlpatterns = router.urls
