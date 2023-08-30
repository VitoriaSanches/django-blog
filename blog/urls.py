from django.urls import path

from blog.views import index, ola

urlpatterns = [
    path("index/", index, name="index"),
    path("ola/", ola, name="ola"),
    path("posts/all", ola, name="posts_list"),
]

from blog.views import index, ola, post_show  # Nesta linha importamos as views

urlpatterns = [
    path("index/", index, name="index"),
    path("ola/", ola, name="ola"),
    path("posts/all", ola, name="posts_list"),
    path("post/<int:post_id>", post_show, name="exibe_post"),
]

from blog.views import index, ola, post_show, PostDetailView

urlpatterns = [
    path("index/", index, name="index"),
    path("ola/", ola, name="ola"),
    path("posts/all", ola, name="posts_list"),  # a view responsável é ola()
    path("post/<int:post_id>", post_show, name="exibe_post"),
    path("post/<int:pk>/show", PostDetailView.as_view(), name="post_detail"),
]
