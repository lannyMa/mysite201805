from django.shortcuts import render

# Create your views here.
from .models import Articles

from app06.serializers import ArticlesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ArticlesListView(APIView):
    """
    list all articles
    """

    def get(self, request, format=None):
        articles = Articles.objects.all()
        articles_serializer = ArticlesSerializer(articles, many=True)  # 返回多个对象
        print(articles_serializer)
        print(type(articles_serializer))

        return Response(articles_serializer.data)

    # def post(self, request, format=None):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
