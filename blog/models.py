

from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator


# Create your models here.

class Author (models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField(max_length = 250)

    def __str__(self):
        return f"{self.First_name}, {self.Last_name}"



class Tag(models.Model):
    Caption = models.CharField(max_length=100)

    
    def __str__(self):
        return self.Caption
    
class Post(models.Model):
    Title = models.CharField(max_length=100)
    Excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "posts", null=True)
    Date= models.DateField(auto_now=True)
    slug= models.SlugField(unique=True,  db_index=True)
    Content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True, related_name="posts")
    tags= models.ManyToManyField(Tag)
   

    def save(self, *args, **kwargs):
        self.slug=slugify(self.Title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Title


class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

# class UserComment(models.Model):
#     post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True, related_name='comments')
#     name = models.CharField(max_length=80,null=True)
#     email = models.EmailField(null=True,)
#     body = models.TextField(null=True,)
#     created_on = models.DateTimeField(auto_now_add=True,null=True,)
#     active = models.BooleanField(default=False,)

#     # class Meta:
#     #     ordering = ['created_on']

#     def __str__(self):
#         return f'Comment {self.body} by {self.name}'
    


    


