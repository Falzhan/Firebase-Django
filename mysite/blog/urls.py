from django.urls import path
from .views import blog_list, blog_detail, blog_delete, blog_create, blog_update

urlpatterns = [
    path('create/', blog_create, name='blog_create'),
    path('<int:id>/update/', blog_update, name='blog_update'),
    path('<int:id>/', blog_detail, name='blog_detail'),
    path('<int:id>/delete/', blog_delete, name='blog_delete'),
    path('posts/', blog_list, name='blog_list'),
    path('', blog_list),
]
