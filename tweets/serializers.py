from rest_framework import serializers
from .models import Tweet
from django.conf import settings

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH
TWEET_ACTION_OPTIONS = settings.TWEET_ACTION_OPTIONS

class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError("This action is not a valid for tweets")
        return value



class TweetSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Tweet
        fields = '__all__'

    def get_likes(self, obj):
        return obj.likes.count()

    def validated_content(self, value):
        if len(value) > MAX_TWEET_LENGTH:
            raise serializers.ValidationError('This tweet is too long!')
        return value
