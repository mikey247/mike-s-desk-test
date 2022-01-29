from django.urls import path
from blog.views import IndexPage,AllPosts, PostDetail, ReadLaterView  #remove_post

urlpatterns = [
  path( "",IndexPage.as_view(), name="index"),
  path('posts',AllPosts.as_view(), name="posts-page" ),
  path("posts/<slug:slug>", PostDetail.as_view(), name="post-detail-page") ,
  path("read-later", ReadLaterView.as_view(), name="read-later" ),
 ]
