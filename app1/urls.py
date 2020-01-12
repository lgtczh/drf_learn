from django.urls import path

from app1 import views

urlpatterns = [
    path('posts/<int:ns>', views.PostList.as_view(), name="posts")
]
