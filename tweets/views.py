from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Tweet
from .forms import TweetForm
from django.conf import settings
from django.contrib.auth.models import User as UserModel

User = settings.AUTH_USER_MODEL

def home(request):
    tweets = Tweet.objects.all()
    return render(request, 'pages/home.html', context={"tweets": tweets})

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