from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Football(models.Model):
    """
    Stores a single football related to :model:`auth.User`
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="soccer_football" 
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)


    class Meta:
        """To display the posts by created_on in ascending order"""
        ordering = ["-created_on"]

    def __str__(self):
        """Return a string representation of the object (the post's title and author)."""
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):

    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    ball = models.ForeignKey(
        ball, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField() # the comment body field section
    created_on = models.DateTimeField(auto_now_add=True)


    class Mata:
        ordering= ["created_on"]
    def __str__(self):
        return f"Comment {self.body} by {self.author}"
    
