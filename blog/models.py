from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
APPROVED = ((0, "Refused"), (1, "Approved"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
        )
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
  
    class Meta: # Order by creation date, most recent first and then per author, to always put at the end of the class
        ordering = ["-created_on", "author"]
    def __str__(self):# To change post name in the post list, adds the phrase bellow
        return f"The title of this post is {self.content} written by {self.author}"

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comment_done_on"
        )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_done_by"
        )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    class Meta: # Order by creation date, oldest first and then per author, to always put at the end of the class
        ordering = ["created_on"]
    def __str__(self):# To change comment name in comment list, adds the phrase bellow
        return f"Comment {self.content} by {self.author}"

  
