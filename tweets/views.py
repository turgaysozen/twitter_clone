from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from rest_framework.response import Response
from .models import Tweet
from .forms import TweetForm
from .serializers import TweetSerializer
from django.conf import settings
from django.contrib.auth.models import User as UserModel
from random import randint
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

User = settings.AUTH_USER_MODEL

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tweet_list_dtf_Serializers(self):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tweet_detail_view_drf_serializer(self, tweet_id):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs:
        return Response({}, 404)
    obj = qs.first()
    serializer = TweetSerializer(obj)
    return Response(serializer.data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_tweet_drf_serializers(request):
    tweet_serializer = TweetSerializer(data=request.data)
    print(tweet_serializer)
    if tweet_serializer.is_valid():
        tweet_serializer.save(user=request.user)
        return JsonResponse(tweet_serializer.data, status=201)
    return Response(tweet_serializer.data)

def tweet_list_pure_django(request):
    tweets = Tweet.objects.all()
    tweet_list = [tweet.serialize() for  tweet in tweets]
    print(tweet_list)
    data = {
        "tweets": tweet_list
    }
    #return render(request, 'pages/home.html', context={"tweets": tweet_list})
    return Response(data, safe=False, content_type="application/json")

def create_tweet_django_forms(request):
    if not request.user.is_authenticated: 
        return redirect(settings.LOGIN_URL)
    form = TweetForm(request.POST or None)
    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = request.user
        tweet.save()
        form = TweetForm()
    return render(request, 'components/form.html', context={"form": form})

def tweet_detail(request, tweet_id):
    try:
        tweet = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404
    return HttpResponse(f'Tweet: {tweet.content}, img:{tweet.image}')