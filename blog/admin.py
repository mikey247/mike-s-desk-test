from django.contrib import admin
from blog.models import Post,Author,Tag , Comment

class PostAdmin(admin.ModelAdmin):
    list_filter=("author", "tags", "Date")
    list_display=("Title", "Date", "author")
    # prepopulated_fields = {"slug": ("Title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")
    list_filter=("post", "user_name")

# Register your models here.

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)