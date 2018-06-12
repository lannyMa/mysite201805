# get所需的
from snippets.serializers import SnippetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response  # 是drf的response

# post所需的
from snippets.models import Snippet
from django.http import Http404
from rest_framework import status

# class SnippetList(APIView):
#     """
#     这是SnippetList接口的一些描述信息
#     List all snippets, or create a new snippet.
#     """
#
#     def get(self, request, format=None):
#         """获取"""
#         snippets = Snippet.objects.all()
#         snippets_serializer = SnippetSerializer(snippets, many=True)
#         return Response(snippets_serializer.data)
#
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data) # drf的request,可以直接取出用户过来的body数据 / post数据
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 优化list
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from rest_framework import mixins
# from rest_framework import generics

# class SnippetList(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs): #写了才有get
#         return self.list(request, *args, **kwargs) # list 分页,序列化等

# listapiview
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from rest_framework import mixins
# from rest_framework import generics
#
#
# class SnippetList(generics.ListAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer


# 看下源码
# class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs): #写了才有get
#         return self.list(request, *args, **kwargs) # list 分页,序列化等
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 10  # http://127.0.0.1:8000/snippets/snippets?p=2&page_size=2 可以自定义参数 http://www.django-rest-framework.org/api-guide/pagination/


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    pagination_class = LargeResultsSetPagination


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
