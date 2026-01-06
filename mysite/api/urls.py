from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from .poorguy_views import ReviewViewSet

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'reviews', ReviewViewSet, basename='review')

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]

# Additional custom API endpoints
additional_api_urls = [
    path('posts/', PostViewSet.as_view({'get': 'list_posts'}), name='post-list'),
    path('posts/create/', PostViewSet.as_view({'post': 'create_post'}), name='post-create'),
    path('posts/<int:id>/detail/', PostViewSet.as_view({'get': 'get_post'}), name='post-detail'),
    path('posts/<int:id>/update/', PostViewSet.as_view({'put': 'update_post', 'patch': 'update_post'}), name='post-update'),
    path('posts/<int:id>/delete/', PostViewSet.as_view({'delete': 'delete_post'}), name='post-delete'),
]