from django.contrib import admin
from django.urls import path
from blog.views import PostListView, PostDetailView, CategoryView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", PostListView.as_view(), name="post_list"),
    path("post/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("category/<slug:slug>/", CategoryView.as_view(), name="category_posts"),
]