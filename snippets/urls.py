from rest_framework.routers import DefaultRouter

from snippets import views

# --------------------------- 1 & 2 ---------------------------
# urlpatterns = [
#     path('snippets', views.snippet_list),
#     path('snippets/<int:pk>', views.snippet_detail)
# ]

# --------------------------- 3 & 4 & 5 ---------------------------
# urlpatterns = [
#     path('snippets', views.SnippetList.as_view()),
#     path('snippets/<int:pk>', views.SnippetDetail.as_view())
# ]
#
# urlpatterns += [
#     path('users', views.UserList.as_view()),
#     path('users/<int:pk>', views.UserDetail.as_view())
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

# --------------------------- 6.1 ---------------------------
# from snippets.views import SnippetViewSet, UserViewSet
# from django.urls import path
# from rest_framework import renderers
#
# snippet_list = SnippetViewSet.as_view(
#     {'get': 'list',
#      'post': 'create'}
# )
#
# snippet_detail = SnippetViewSet.as_view(
#     {'get': 'retrieve',
#      'put': 'update',
#      'patch': 'partial_update',
#      'delete': 'destroy'}
# )
#
# snippet_highlight = SnippetViewSet.as_view(
#     {
#         'get': 'highlight'
#     }, renderer_classes=[renderers.StaticHTMLRenderer]
# )
#
# user_list = UserViewSet.as_view(
#     {'get': 'list'}
# )
#
# user_detail = UserViewSet.as_view(
#     {'get': 'retrieve'}
# )
#
# urlpatterns = [
#     path('snippets', snippet_list),
#     path('snippets/<int:pk>', snippet_detail)
#     path('users', user_list),
#     path('users/<int:pk>', user_detail)
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight')
# ]


# --------------------------- 6.2 ---------------------------
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from snippets import views

router = DefaultRouter()

router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
