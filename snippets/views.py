from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins, viewsets

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 10


class SnippetList(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    pagination_class = LargeResultsSetPagination
