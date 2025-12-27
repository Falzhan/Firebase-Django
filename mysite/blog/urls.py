from django.urls import path
from .views import blog_list, blog_detail, blog_delete, blog_create, blog_update

urlpatterns = [
   path('',blog_list),
   path('create/',blog_create),
   path('<int:id>/update/',blog_update),
   path('<int:id>/',blog_detail),
   path('<int:id>/delete/',blog_delete)

]
