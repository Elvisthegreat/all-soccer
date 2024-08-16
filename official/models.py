from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Official(models.Model):
    """
    store a single text about the official
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="official_football"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='official_likes', blank=True)
    class Meta:
        """To display the posts by created_on in ascending order"""
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    official = models.ForeignKey(Official, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    officials = models.ForeignKey(
        Official, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Mata:
        ordering= ["created_on"]
    def __str__(self):
        return f"Comment {self.body} by {self.author}"