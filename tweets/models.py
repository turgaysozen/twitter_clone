from django.db import models
from django.conf import settings
from random import randint

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.pk,
            "content": self.content,
            "like": randint(20, 200)
        }