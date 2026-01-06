from django.urls import path
from . import views

app_name = 'poorguy'

urlpatterns = [
    # Main feed
    path('', views.tech_feed, name='tech_feed'),
    
    # Single review detail
    path('review/<int:review_id>/', views.review_detail, name='review_detail'),
    
    # Comparison view
    path('compare/', views.compare_specs, name='compare_specs'),
    
    # Category filtering
    path('category/<str:category_slug>/', views.category_filter, name='category_filter'),
    
    # Grade filtering
    path('grade/<str:grade>/', views.grade_filter, name='grade_filter'),
    
    # CRUD operations
    path('add-review/', views.add_review, name='add_review'),
    path('edit-review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete-review/<int:review_id>/', views.delete_review, name='delete_review'),
]