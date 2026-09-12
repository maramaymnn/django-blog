from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<str:category_name>/', CategoryListView.as_view(), name='category_posts'),
]