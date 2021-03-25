from django.db import models
from django.conf import settings
from random import randint

User = settings.AUTH_USER_MODEL

class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Tweet(models.Model):
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='tweet_user' , blank=True, through=TweetLike)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    @property
    def is_retweet(self):
        return self.parent != None

    # no need anymore! (for drf)
    def serialize(self):
        return {
            "id": self.pk,
            "content": self.content,
            "like": randint(20, 200)
        }