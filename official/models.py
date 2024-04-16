from django.db import models
from django.contrib.auth.models import User

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
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)

    class Meta:
        """To display the posts by created_on in ascending order"""
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title}"
