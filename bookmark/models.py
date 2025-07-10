# bookmark/models.py
from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(default="No description available")
    url = models.URLField()
    image_url = models.URLField(default="http://example.com/default-image.jpg")  # Default value added

    def __str__(self):
        return self.title
