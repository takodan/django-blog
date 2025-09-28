from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blog_index"),
    path("posts/", views.posts, name="blog_posts"),
    path("posts/<slug:slug>", views.post_detail, name="blog_post_detail"),
]