"""twitter_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tweets.views import tweet_list_dtf_Serializers, tweet_detail, create_tweet_django_forms, create_tweet_drf_serializers, tweet_detail_view_drf_serializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tweet_list_dtf_Serializers),
    path('tweet/<int:tweet_id>', tweet_detail_view_drf_serializer),
    path('create-tweet', create_tweet_drf_serializers)
]
