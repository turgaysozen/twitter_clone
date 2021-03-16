from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)