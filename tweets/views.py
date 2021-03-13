from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Tweet
from .forms import TweetForm

def home(request):
    tweets = Tweet.objects.all()
    return render(request, 'pages/home.html', context={"tweets": tweets})

def create_tweet(request):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.save()
        form = TweetForm()
    return render(request, 'components/form.html', context={"form": form})


def tweet_detail(request, tweet_id):
    try:
        tweet = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404
    return HttpResponse(f'Tweet: {tweet.content}, img:{tweet.image}')