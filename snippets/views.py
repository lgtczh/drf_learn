# Create your views here.
# --------------------------------------------------- 1 ---------------------------------------------------
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer


# @csrf_exempt
# def snippet_list(request):
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializers = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializers.data, safe=False)
#
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201, safe=False)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def snippet_detail(request, pk):
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)
#
#     if request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     if request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)

# --------------------------------------------------- 2 ---------------------------------------------------
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
#
#
# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializers = SnippetSerializer(snippets, many=True)
#         return Response(serializers.data)
#
#     if request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk):
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# --------------------------------------------------- 3 ---------------------------------------------------
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
#
#
# class SnippetList(APIView):
#
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         ss = SnippetSerializer(data=request.data)
#         if ss.is_valid():
#             ss.save()
#             return Response(ss.data, status=status.HTTP_201_CREATED)
#         return Response(ss.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class SnippetDetail(APIView):
#
#     def get_object(self, pk):
#         try:
#             snippet = Snippet.objects.get(pk=pk)
#             return snippet
#         except Snippet.DoesNotExist:
#             raise Http404
#             # return None  # Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, pk, format=None):
#         obj = self.get_object(pk)
#         return Response(SnippetSerializer(obj).data)
#
#     def put(self, request, pk, format=None):
#         obj = self.get_object(pk)
#         ss = SnippetSerializer(obj, data=request.data)
#         if ss.is_valid():
#             ss.save()
#             return Response(ss.data)
#         return Response(ss.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         self.get_object(pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# --------------------------------------------------- 4 ---------------------------------------------------
# from rest_framework import mixins, generics
#
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
#
#
# class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class SnippetDetail(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, args, kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# --------------------------------------------------- 5 ---------------------------------------------------
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
#
# from snippets.models import Snippet
# from snippets.permissions import IsOwnerOrReadOnly
# from snippets.serializers import SnippetSerializer, UserSerializer
#
#
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
#
#
# class UserList(generics.ListAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = UserSerializer


# --------------------------------------------------- 6 ---------------------------------------------------
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import UserSerializer, SnippetSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
