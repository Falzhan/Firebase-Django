from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from poorguy.models import Review
from .poorguy_serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Review instances.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

    @action(detail=False, methods=['get'], url_path='list')
    def list_reviews(self, request):
        """
        List all reviews with pagination support
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='detail')
    def get_review(self, request, id=None):
        """
        Get detailed information about a specific review
        """
        try:
            review = self.get_object()
            serializer = self.get_serializer(review)
            return Response(serializer.data)
        except:
            return Response(
                {"error": "Review not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=['put', 'patch'], url_path='update')
    def update_review(self, request, id=None):
        """
        Update a specific review
        """
        try:
            review = self.get_object()
            serializer = self.get_serializer(review, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(
                {"error": "Review not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=['delete'], url_path='delete')
    def delete_review(self, request, id=None):
        """
        Delete a specific review
        """
        try:
            review = self.get_object()
            review.delete()
            return Response(
                {"message": "Review deleted successfully"},
                status=status.HTTP_204_NO_CONTENT
            )
        except:
            return Response(
                {"error": "Review not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=False, methods=['post'], url_path='create')
    def create_review(self, request):
        """
        Create a new review
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)