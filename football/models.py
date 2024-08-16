from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Football(models.Model):
    """
    Stores a single football related to :model:`auth.User`
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        """To display the posts by created_on in ascending order"""
        ordering = ["-created_on"]

    def __str__(self):
        """Return a string representation of the object (the post's title and author)."""
        return f"{self.title} | written by {self.author}"


