from django.forms import ModelForm
from blog.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        # fields = ('user_name', 'user_email', 'text')
        exclude = ["post"]
        labels={
            'user_name': "Your Name", 
            'user_email': "Your Email", 
            'text' : "Your Comment"
        }