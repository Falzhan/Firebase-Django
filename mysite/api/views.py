from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from blog.models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Post instances.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    @action(detail=False, methods=['get'], url_path='list')
    def list_posts(self, request):
        """
        List all posts with pagination support
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='detail')
    def get_post(self, request, id=None):
        """
        Get detailed information about a specific post
        """
        try:
            post = self.get_object()
            serializer = self.get_serializer(post)
            return Response(serializer.data)
        except:
            return Response(
                {"error": "Post not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=['put', 'patch'], url_path='update')
    def update_post(self, request, id=None):
        """
        Update a specific post
        """
        try:
            post = self.get_object()
            serializer = self.get_serializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(
                {"error": "Post not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=['delete'], url_path='delete')
    def delete_post(self, request, id=None):
        """
        Delete a specific post
        """
        try:
            post = self.get_object()
            post.delete()
            return Response(
                {"message": "Post deleted successfully"},
                status=status.HTTP_204_NO_CONTENT
            )
        except:
            return Response(
                {"error": "Post not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=False, methods=['post'], url_path='create')
    def create_post(self, request):
        """
        Create a new post
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)