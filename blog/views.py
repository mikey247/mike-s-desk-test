from django.shortcuts import redirect, render
from django.template import context
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.views import View
from blog.forms import CommentForm
from blog.models import Post
from django.http import HttpResponseRedirect



# all_posts = [
  
# ]


def get_date(post):
    return post['date']



# Create your views here.

class IndexPage(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-Date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

# def index(request):
#     latest_posts = Post.objects.all().order_by("-Date")[:5]
#     return render(request, "blog/index.html", {
#        "posts": latest_posts
#     } )

class AllPosts(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-Date"]
    context_object_name = "all_posts"



# def posts(request):
#     all_posts= Post.objects.all().order_by("-Date")
#     return render(request, "blog/all-posts.html" , {
#         "all_posts": all_posts
#     } )

class PostDetail(View):

    def is_stored(self,request,post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
          is_saved = post_id in stored_posts
        else:
          is_saved = False 

        return is_saved


    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        
        context = {
            "post":post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved":self.is_stored(request,post.id)
        }
        return render (request, "blog/post-detail.html",context)
    



    def post(self,request,slug ):  
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)


        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(reverse("post-detail-page", args=[slug]))
        
        context = {
            "post":post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved":self.is_stored(request,post.id)
        }
        
        return render (request, "blog/post-detail.html",context)

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
          posts = Post.objects.filter(id__in=stored_posts)
          context["posts"] = posts
          context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
          stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
          stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/")

